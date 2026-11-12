"""Two finite anonymous public reads; no retries, profiles, or credentials."""
import concurrent.futures
import datetime as dt
import hashlib
import json
from pathlib import Path
import urllib.request
import urllib.error

BASE = Path(__file__).resolve().parent
JOBS = {
    "SEC_SCTX": "https://data.sec.gov/submissions/CIK0001853921.json",
    "CTG_NCT07428473": "https://clinicaltrials.gov/api/v2/studies/NCT07428473",
}

def collect(item):
    name, url = item
    r = {"name": name, "url": url, "started_utc": dt.datetime.now(dt.timezone.utc).isoformat(), "attempts": 1}
    try:
        with urllib.request.urlopen(url, timeout=16) as response:
            raw = response.read(2 * 1024 * 1024 + 1)
            if len(raw) > 2 * 1024 * 1024:
                raise ValueError("public read cap exceeded")
            r.update(status=response.status, bytes=len(raw), sha256=hashlib.sha256(raw).hexdigest())
            (BASE / (name + ".json")).write_bytes(raw)
    except urllib.error.HTTPError as e:
        r.update(status=e.code, error="HTTPError; refused body not read; stop")
    except Exception as e:
        r.update(status=None, error=type(e).__name__ + ": " + str(e))
    r["ended_utc"] = dt.datetime.now(dt.timezone.utc).isoformat()
    (BASE / (name + ".receipt.json")).write_text(json.dumps(r, ensure_ascii=False, indent=2))
    return r

with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
    for result in pool.map(collect, JOBS.items()):
        print(json.dumps(result, ensure_ascii=False))
