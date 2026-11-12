import collections
import hashlib
import json
from pathlib import Path

B = Path(__file__).resolve().parents[1]


def read(p):
    return json.loads((B / p).read_text())


def sha(t):
    return hashlib.sha256(t.encode()).hexdigest()


def dump(p, value):
    (B / p).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')


normal = read('root/finals_index.json')
archived = [json.loads(s) for s in (B / 'root/archived/conversation_messages.jsonl').read_text().splitlines()]
archived = [r for r in archived if r['role'] == 'assistant' and r['channel'] == 'final_answer']
early = read('legacy/early_advice.json')
late = read('root/root_review.json')
ar = read('legacy/archived_advice.json')
all_com = read('legacy/commentary_review.json')
rest_com = read('legacy/commentary_remaining_review.json')

assert len(normal) == 433 and len(archived) == 74
assert [r['final_id'] for r in normal] == ['F' + str(n) for n in range(1, 434)]
assert [r['final_id'] for r in early['review_manifest']] == ['F' + str(n) for n in range(1, 282)]
assert [r['final_id'] for r in late] == ['F' + str(n) for n in range(282, 434)]
assert [r['archive_id'] for r in ar['review_manifest']] == ['A' + str(n) for n in range(1, 75)]

emap = {r['final_id']: r for r in early['review_manifest']}
lmap = {r['final_id']: r for r in late}
edirect = {r['final_id']: r for r in early['direct_user_advice_records']}
areview = {r['archive_id']: r for r in ar['review_manifest']}
records = []
for original in normal:
    fid = original['final_id']
    review = emap.get(fid) or lmap[fid]
    if fid in emap:
        assert review['sha256_text'] == sha(original['text']), fid
        cls = review['classification']
        direct = fid in edirect
        advice_date = edirect.get(fid, {}).get('advice_date')
        note = ''
        excerpts = edirect.get(fid, {}).get('action_excerpt_lines', [])
        if isinstance(excerpts, str):
            note = excerpts[:1400]
        else:
            note = '\n'.join(str(s) for s in excerpts)[:1400]
    else:
        assert review['text'] == original['text'], fid
        cls = review['audit_category']
        direct = cls == '\u5efa\u8bae\u6216\u6301\u4ed3\u98ce\u9669\u590d\u6838'
        advice_date = original['timestamp'][:10]
        note = review['root_review_note']
    records.append(dict(id=fid, source=original['source'], source_line=original['line'],
                        thread_id=original['thread_id'], archive_timestamp=original['timestamp'],
                        advice_date=advice_date or 'UNKNOWN', classification=cls,
                        in_advice_group=direct, note=note, text_sha256=sha(original['text']),
                        original_text=original['text']))

for n, original in enumerate(archived, 1):
    fid = 'A' + str(n)
    rev = areview[fid]
    assert rev['text_sha256'] == sha(original['text']), fid
    records.append(dict(id=fid, source=original['source'], source_line=original['line'],
                        thread_id=original['thread_id'], archive_timestamp=original['timestamp'],
                        advice_date=rev['advice_date'], classification=rev['classification'],
                        in_advice_group=fid == 'A52', note='\n'.join(str(s) for s in rev.get('action_word_lines', []))[:1400],
                        text_sha256=sha(original['text']), original_text=original['text']))

advice = [r for r in records if r['in_advice_group']]
assert len(records) == 507 and len(advice) == 125
dump('ALL_FINALS_INDEX.json', records)
dump('ADVICE_LEDGER.json', advice)

title = '# \u5168\u90e8507\u6761\u6700\u7ec8\u7b54\u590d\u7d22\u5f15\n\n'
intro = ('\u8fd9\u662f\u6d88\u606f\u5206\u7c7b\uff0c\u4e0d\u662f\u4ea4\u6613\u7b14\u6570\u3002\u65e5\u671f\u51b2\u7a81\u4fdd\u7559UNKNOWN\uff0c\u5f52\u6863\u65f6\u95f4\u4e0d\u5f3a\u884c\u5f53\u4f5c\u771f\u5b9e\u5efa\u8bae\u65e5\u3002\u6bcf\u6761\u94fe\u63a5\u6307\u5411\u539f\u6587\u53ca\u539f\u65e5\u5fd7\u5b9a\u4f4d\u3002\n\n')
table = '| ID | \u5f52\u6863\u65e5 | \u5efa\u8bae\u65e5/\u72b6\u6001 | \u4e92\u65a5\u5206\u7c7b |\n|---|---|---|---|\n'
for r in records:
    date = str(r['advice_date']).replace('|', '/')
    table += f"| [{r['id']}](ALL_FINALS_TEXT.md#{r['id'].lower()}) | {r['archive_timestamp'][:10]} | {date} | {r['classification']} |\n"
(B / 'ALL_FINALS_INDEX.md').write_text(title + intro + table)

full = '# \u5168\u90e8\u6700\u7ec8\u7b54\u590d\u539f\u6587\n\n\u539f\u6587\u4fdd\u7559\u5f53\u65f6\u53e3\u5f84\uff0c\u4e0d\u4ee3\u8868\u5ba1\u8ba1\u80cc\u4e66\u6216\u5f53\u524d\u5efa\u8bae\u3002\n\n'
for r in records:
    full += f"<a id=\"{r['id'].lower()}\"></a>\n\n## {r['id']}\n\n"
    full += f"- \u5f52\u6863\u65f6\u95f4\uff1a{r['archive_timestamp']}\n- \u5efa\u8bae\u65e5\uff1a{r['advice_date']}\n"
    full += f"- \u5206\u7c7b\uff1a{r['classification']}\n- \u539f\u59cb\u7ebf\u7d22\uff1a{r['source']}:{r['source_line']}\n"
    full += f"- thread\uff1a`{r['thread_id']}`\n- text SHA-256\uff1a`{r['text_sha256']}`\n\n{r['original_text']}\n\n"
(B / 'ALL_FINALS_TEXT.md').write_text(full)

ledger = ('# \u53ef\u884c\u52a8\u5efa\u8bae\u53ca\u6301\u4ed3\u590d\u6838\u6d88\u606f\u53f0\u8d26\n\n'
          '\u5171125\u6761\u6700\u7ec8\u6d88\u606f\uff1a69\u65e9\u671f+55\u540e\u671f+1\u5f52\u6863\u3002\u5305\u62ec\u4e0d\u4e70\u3001\u4e0d\u52a0\u3001\u6761\u4ef6\u65b9\u6848\u53ca\u6301\u4ed3\u590d\u6838\uff0c\u4e0d\u662f125\u7b14\u4ea4\u6613\u3002\u6bcf\u4e2a\u6761\u76ee\u94fe\u63a5\u5747\u6709\u5b8c\u6574\u539f\u6587\u53ca\u539f\u65e5\u5fd7\u4f4d\u7f6e\u3002\n\n'
          '\u4e2d\u95f4\u56de\u590d\u9996\u6b21\u63d0\u9192\u53e6\u89c1 `legacy/commentary_review.json` \u548c `legacy/commentary_remaining_review.json`\uff0c\u4e0d\u91cd\u590d\u8ba1\u4ea4\u6613\u3002\u8be6\u7ec6\u5904\u7f6e\u7ed3\u679c\u89c1[\u9010\u80a1\u590d\u76d8](CASEBOOK.md)\u3002\n\n')
for r in advice:
    ledger += f"## [{r['id']}](ALL_FINALS_TEXT.md#{r['id'].lower()}) | {r['advice_date']}\n\n"
    ledger += f"\u5206\u7c7b\uff1a{r['classification']}\u3002\u5f52\u6863\u65f6\u95f4\uff1a{r['archive_timestamp']}\u3002\n\n"
    ledger += (r['note'] or '\u8bf7\u70b9\u51fbID\u8bfb\u53d6\u5b8c\u6574\u539f\u6587\u3002') + '\n\n'
ledger += ('## \u6df7\u5408\u6d88\u606f\u4e0e\u6210\u4ea4\u767b\u8bb0\u8865\u5145\n\n'
           '\u6210\u4ea4\u767b\u8bb0\u6216\u7ea0\u6b63\u4e2d\u4e5f\u53ef\u542b\u505c\u6b62\u65b0\u589e\u7b49\u9650\u5236\uff1b\u4ee5\u4e0b\u4fdd\u7559\u5168\u6587\u94fe\u63a5\uff0c\u4e0d\u56e0\u4e3b\u5206\u7c7b\u800c\u4e22\u5f03\u3002\u65b0\u6210\u4ea4\u6570\u91cf\u53ea\u7528\u7528\u6237\u6700\u65b0\u4e3b\u52a8\u786e\u8ba4\uff0c\u4e0d\u7528\u52a9\u624b\u81ea\u8ff0\u4f5c\u72ec\u7acb\u6210\u4ea4\u8bc1\u636e\u3002\n\n')
for r in records:
    if 'acknowledgement' in r['classification'] or r['classification'] == '\u7528\u6237\u6210\u4ea4/\u6301\u4ed3\u786e\u8ba4\u4e0e\u66f4\u6b63':
        ledger += f"- [{r['id']}](ALL_FINALS_TEXT.md#{r['id'].lower()}) | {r['archive_timestamp']} | {r['classification']}\n"
ledger += '\n\u5176\u4f59\u7814\u7a76\u8349\u6848\u3001\u6392\u5e8f\u3001\u4e8b\u540e\u66f4\u6b63\u53ca\u6cbb\u7406\u7c7b\u6d88\u606f\u4e5f\u5168\u90e8\u4fdd\u7559\u5728[507\u6761\u5168\u7d22\u5f15](ALL_FINALS_INDEX.md)\uff0c\u4e0d\u4ee5\u7814\u7a76\u6392\u540d\u5012\u63a8\u4ea4\u6613\u3002\n'
(B / 'ADVICE_LEDGER.md').write_text(ledger)

messages = []
for p in ['root/conversation_messages.jsonl', 'root/archived/conversation_messages.jsonl']:
    messages.extend(json.loads(s) for s in (B / p).read_text().splitlines())
commentary = [r for r in messages if r['role'] == 'assistant' and r['channel'] == 'commentary']


def key(r):
    return (r.get('source', r.get('source_file')), r.get('line', r.get('source_line', r.get('source_jsonl_line'))))


cmanifest = all_com['records'] + rest_com['remaining_records']
assert len(cmanifest) == 1186
assert len({key(r) for r in cmanifest}) == 1186
assert {key(r) for r in cmanifest} == {key(r) for r in commentary}
source_by_key = {key(r): r for r in commentary}
hash_checks = 0
for r in cmanifest:
    source_text = source_by_key[key(r)]['text']
    if 'text' in r:
        assert r['text'] == source_text
    for field in ['text_sha256', 'sha256_text', 'sha256']:
        if field in r:
            assert r[field] == sha(source_text)
            hash_checks += 1

threads = []
for p in ['root/history_coverage.json', 'root/archived/history_coverage.json']:
    threads += read(p)['coverage']
assert len(threads) == 93 and len({r['thread_id'] for r in threads}) == 93
recovery = read('root/parse_recovery.json')['records']
assert sum(r['physical_lines'] for r in recovery) == 113
assert len(recovery) == 21
assert not any(r.get('role') == 'assistant' for r in recovery)
counts = collections.Counter(r['classification'] for r in records)
validation = dict(final_count=len(records), final_id_unique=len({r['id'] for r in records}),
                  direct_or_position_review_messages=len(advice), finals_original_text_hash_checks=507,
                  commentary_count=len(commentary), commentary_manifest_count=len(cmanifest),
                  commentary_uncovered=0, commentary_duplicate_source_keys=0,
                  commentary_hash_checks=hash_checks, source_threads=93, source_threads_unique=93,
                  source_messages=len(messages), source_role_phase_counts={str(k): v for k, v in collections.Counter((r['role'], r['channel']) for r in messages).items()},
                  final_classification_counts=dict(counts), malformed_physical_lines=113, malformed_groups=21,
                  malformed_assistant_messages=0, verdict='PASS within declared text corpus; no actual-return audit claimed')
dump('root/validation.json', validation)
print(json.dumps(validation, ensure_ascii=False, indent=2))
