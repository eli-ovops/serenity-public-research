from pathlib import Path
import json,sys,hashlib
B=Path(__file__).resolve().parent;P=B.parents[2]
sys.path.insert(0,str(P/'tools'))
import suoha_research as w
lens=w.project_path(str(B/'lens.json'),must_exist=True)
d=json.loads(lens.read_text());w.validate_snapshot_reference(d,lens);w.check_valuation_inputs(d)
out=w.project_path(str(B/'skill-finish'));out.mkdir(exist_ok=True)
receipt=B/'LENS_RUN_RECEIPT.json'
if receipt.exists():
 i=1
 while (out/f'prior-attempt-{i}.json').exists():i+=1
 (out/f'prior-attempt-{i}.json').write_bytes(receipt.read_bytes())
code=w.run_upstream('scripts/serenity_lens.py',['finish',str(lens),'--out-dir',str(out),'--stem','RMBS-research'],receipt)
if code==0:
 d=json.loads(lens.read_text());pv=w.discounted_scenarios(d,.12)
 pv.update(valuation_anchor='2026-10-22 frozen horizon2.195756; not mechanically rolled to lift values',future_diluted_shares=110000000,base_common_shares=108461603,PE_cash_treatment='EPS already contains persistentSBC, interest/tax; no extra netcash. Future110m applied once through common-to-future dilution.',source_lens_sha256=hashlib.sha256(lens.read_bytes()).hexdigest())
 (B/'present-values.json').write_text(json.dumps(pv,ensure_ascii=False,indent=2)+'\n')
 r=json.loads(receipt.read_text());r['outputs']=[{'path':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size} for p in [lens,B/'present-values.json',out/'RMBS-research.md',out/'RMBS-research.html']];r['upstream_finish_includes']=['TODO check','compute','validate','Markdown render','HTML render','Markdown verify','HTML verify'];r['snapshot_guard']='tools/suoha_research.py.validate_snapshot_reference passed; no bypass';r['research_tier']=d['research_tier'];receipt.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
sys.exit(code)
