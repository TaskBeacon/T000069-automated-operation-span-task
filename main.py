from __future__ import annotations
from contextlib import nullcontext
from functools import partial
from pathlib import Path
from typing import Any
import pandas as pd
from psychopy import core
from psyflow import BlockUnit,StimBank,StimUnit,SubInfo,TaskSettings,context_from_config,initialize_exp,initialize_triggers,load_config,parse_task_run_options,runtime_context
from src import deadline_from_rows,generate_math_practice,generate_sets,run_trial,summarize
MODES=("human","qa","sim"); DEFAULT_CONFIG_BY_MODE={"human":"config/config.yaml","qa":"config/config_qa.yaml","sim":"config/config_scripted_sim.yaml"}
def block(name,idx,plans,s,w,k,b,t,sink): (BlockUnit(block_id=name,block_idx=idx,settings=s,window=w,keyboard=k).add_condition(plans).on_start(lambda _:t.send(s.triggers.get("block_start"))).on_end(lambda _:t.send(s.triggers.get("block_end"))).run_trial(partial(run_trial,stim_bank=b,trigger_runtime=t,block_id=name,block_idx=idx)).to_dict(sink))
def run(o):
 root=Path(__file__).resolve().parent; cfg=load_config(str(o.config_path)); output,scope,ctx=None,nullcontext(),None
 if o.mode in ("qa","sim"): ctx=context_from_config(task_dir=root,config=cfg,mode=o.mode);output,scope=ctx.output_dir,runtime_context(ctx)
 with scope:
  subject={"subject_id":"qa"} if o.mode=="qa" else ({"subject_id":str(ctx.session.participant_id or "sim")} if o.mode=="sim" else SubInfo(cfg["subform_config"]).collect()); s=TaskSettings.from_dict(cfg["task_config"]);s.add_subinfo(subject)
  if output is not None:s.save_path=str(output)
  if o.mode=="qa" and output is not None: output.mkdir(parents=True,exist_ok=True);s.res_file=str(output/"qa_trace.csv");s.log_file=str(output/"qa_psychopy.log");s.json_file=str(output/"qa_settings.json")
  s.triggers=cfg["trigger_config"];t=initialize_triggers(mock=True) if o.mode in ("qa","sim") else initialize_triggers(cfg);w,k=initialize_exp(s);b=StimBank(w,cfg["stim_config"]).preload_all();s.save_to_json();t.send(s.triggers.get("experiment_start"));StimUnit("instruction",w,k,runtime=t).add_stim(b.get("instruction")).wait_and_continue()
  math_rows=[];block("math_practice",-2,generate_math_practice(int(s.math_practice_count),int(s.plan_seed)),s,w,k,b,t,math_rows);s.math_deadline=deadline_from_rows(math_rows,float(s.math_deadline));StimUnit("combined_intro",w,k,runtime=t).add_stim(b.get_and_format("combined_intro",deadline=f"{s.math_deadline:.2f}")).wait_and_continue()
  practice_rows=[];block("combined_practice",-1,generate_sets(seed=int(s.plan_seed),is_practice=True),s,w,k,b,t,practice_rows);rows=[];block("scored",0,generate_sets(seed=int(s.plan_seed),is_practice=False),s,w,k,b,t,rows);x=summarize(rows);StimUnit("good_bye",w,k,runtime=t).add_stim(b.get_and_format("good_bye",absolute=x["absolute_span"],total=x["total_correct"],math=f"{x['math_accuracy']:.1%}",valid="VALID" if x["valid"] else "INVALID (<85% math)")).wait_and_continue(terminate=True);t.send(s.triggers.get("experiment_end"));pd.DataFrame(rows).to_csv(s.res_file,index=False);t.close();core.quit()
def main(): run(parse_task_run_options(task_root=Path(__file__).resolve().parent,description="Run automated operation span",default_config_by_mode=DEFAULT_CONFIG_BY_MODE,modes=MODES))
if __name__=="__main__":main()
