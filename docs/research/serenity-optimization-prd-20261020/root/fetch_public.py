"""Finite unauthenticated public-source retrieval, one attempt per explicit URL.

Only caller-provided URLs. No credential files, cookies, environment inspection,
browser profiles, retries, schedules, models, or trading interfaces.
"""
import concurrent.futures
import hashlib
import json
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urljoin

from bs4 import BeautifulSoup

BASE = Path(__file__).resolve().parents[1]


def one(job):
    ident = job['id']
    assert ident.replace('_', '').replace('-', '').isalnum()
    dest = BASE / 'public' / ident
    assert not dest.with_suffix('.receipt.json').exists(), 'Do not repeat a recorded request'
    receipt = dict(job, retrieved_at=datetime.now(timezone.utc).isoformat())
    req = urllib.request.Request(job['url'], headers={'User-Agent': 'SerenityResearch/1.0 public-source review'})
    try:
        with urllib.request.urlopen(req, timeout=22) as resp:
            raw = resp.read(12 * 1024 * 1024 + 1)
            if len(raw) > 12 * 1024 * 1024:
                raise ValueError('Document exceeds 12 MiB finite retrieval bound')
            receipt.update(http_status=resp.status, final_url=resp.url,
                           content_type=resp.headers.get('Content-Type', ''), bytes=len(raw),
                           sha256=hashlib.sha256(raw).hexdigest())
        suffix = '.pdf' if raw.startswith(b'%PDF') else '.raw'
        out = dest.with_suffix(suffix)
        out.write_bytes(raw)
        receipt['raw_path'] = str(out.relative_to(BASE))
        if suffix != '.pdf':
            decoded = raw.decode('utf-8', errors='replace')
            if 'json' in receipt['content_type']:
                value = json.loads(decoded)
                dest.with_suffix('.json').write_text(json.dumps(value, ensure_ascii=False, indent=2))
                receipt['parsed_json'] = True
            elif '<' in decoded[:1000]:
                soup = BeautifulSoup(decoded, 'html.parser')
                receipt['title'] = soup.title.get_text(' ', strip=True) if soup.title else ''
                links = [{'text': a.get_text(' ', strip=True), 'url': urljoin(job['url'], a['href'])}
                         for a in soup.find_all('a', href=True)]
                dest.with_suffix('.links.json').write_text(json.dumps(links, ensure_ascii=False, indent=2))
                for tag in soup(['script', 'style', 'nav', 'footer', 'header']):
                    tag.decompose()
                for row in soup.find_all('tr'):
                    row.replace_with(' | '.join(c.get_text(' ', strip=True) for c in row.find_all(['td', 'th'])))
                text = soup.get_text('\n', strip=True)
                dest.with_suffix('.txt').write_text(text)
                receipt['text_chars'] = len(text)
        receipt['retrieval_status'] = 'retrieved; semantic review separate'
    except urllib.error.HTTPError as error:
        receipt.update(http_status=error.code, retrieval_status='failed; no retry or alternate identity', error=str(error))
    except Exception as error:
        receipt.update(retrieval_status='failed; no retry', error=str(error))
    dest.with_suffix('.receipt.json').write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + '\n')
    return {k: receipt[k] for k in ['id', 'http_status', 'bytes', 'text_chars', 'retrieval_status', 'error'] if k in receipt}


if __name__ == '__main__':
    jobs = json.loads(Path(sys.argv[1]).read_text())
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        for result in pool.map(one, jobs):
            print(json.dumps(result, ensure_ascii=False), flush=True)
