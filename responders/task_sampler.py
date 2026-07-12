from psyflow.sim.contracts import Action
class TaskSamplerResponder:
 def __init__(self,accuracy=.9,rt_s=.02):self.accuracy=accuracy;self.rt_s=rt_s;self.rng=None
 def start_session(self,session,rng):self.rng=rng
 def on_feedback(self,fb):pass
 def end_session(self):pass
 def act(self,obs):
  keys=[str(k) for k in (obs.valid_keys or [])]
  if not keys:return Action(key=None,rt_s=None)
  f=dict(getattr(obs,"task_factors",{}) or {});stage=str(f.get("stage",getattr(obs,"phase","")));phase=stage
  if phase=="feedback":return Action(key=None,rt_s=None)
  if stage in {"instruction","combined_intro","good_bye"}:return Action(key="space",rt_s=.02)
  if stage in {"feedback","letter"}:return Action(key=None,rt_s=None)
  if stage=="solve":return Action(key="space",rt_s=self.rt_s)
  correct=str(f.get("correct_key",keys[0])); choose=float(self.rng.random())<=self.accuracy if self.rng else True; return Action(key=correct if choose else next((k for k in keys if k!=correct),keys[0]),rt_s=self.rt_s)
