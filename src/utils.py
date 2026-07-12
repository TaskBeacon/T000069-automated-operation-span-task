from __future__ import annotations
import hashlib, random, statistics
from typing import Any
LETTERS=tuple("FHJKLNPQRSTY")
SET_SIZES=(3,4,5,6,7)
class SetPlan(str):
    def __new__(cls,*,items:list[dict[str,Any]],set_size:int,is_practice:bool,index:int):
        label=f"set_{set_size}_{'practice' if is_practice else 'scored'}"; o=str.__new__(cls,label); o.items=items;o.set_size=set_size;o.is_practice=is_practice;o.index=index;return o
    def to_dict(self): return {"condition":str(self),"condition_id":str(self),"items":self.items,"set_size":self.set_size,"is_practice":self.is_practice,"trial_index_in_block":self.index}
def _seed(base:int,label:str): return int.from_bytes(hashlib.blake2b(f"{base}|ospan|{label}".encode(),digest_size=8).digest(),"big")
def _math(rng:random.Random):
    a,b,c=rng.randint(1,9),rng.randint(1,9),rng.randint(1,5); op=rng.choice(("+","-")); result=a*b+c if op=="+" else a*b-c; expression=f"({a} x {b}) {op} {c}"; truth=bool(rng.randrange(2)); proposed=result if truth else result+rng.choice((-3,-2,-1,1,2,3)); return {"expression":expression,"proposed":proposed,"math_true":truth,"math_correct_key":"j" if truth else "f"}
def generate_math_practice(count:int,seed:int):
    rng=random.Random(_seed(seed,"math")); return [SetPlan(items=[{**_math(rng),"letter":""}],set_size=0,is_practice=True,index=i) for i in range(count)]
def generate_sets(*,seed:int,is_practice:bool):
    rng=random.Random(_seed(seed,"combined-practice" if is_practice else "scored")); sizes=[2]*3 if is_practice else [s for s in SET_SIZES for _ in range(3)]; rng.shuffle(sizes); out=[]
    for i,size in enumerate(sizes): out.append(SetPlan(items=[{**_math(rng),"letter":letter} for letter in rng.sample(LETTERS,size)],set_size=size,is_practice=is_practice,index=i))
    return out
def deadline_from_rows(rows,default=5.0):
    rts=[float(r.get("solve_mean_rt")) for r in rows if r.get("solve_mean_rt") not in (None,"")]; return min(10.0,max(1.0,(statistics.mean(rts)+2.5*statistics.pstdev(rts)) if rts else default))
def summarize(rows):
    scored=[r for r in rows if not bool(r.get("is_practice")) and int(r.get("set_size",0))>0]; total=sum(int(r.get("letters_correct",0)) for r in scored); absolute=sum(int(r.get("set_size",0)) for r in scored if bool(r.get("perfect_recall"))); mtotal=sum(int(r.get("math_count",0)) for r in scored); mcorrect=sum(int(r.get("math_correct",0)) for r in scored); acc=mcorrect/mtotal if mtotal else 0.0; return {"absolute_span":absolute,"total_correct":total,"math_accuracy":acc,"valid":acc>=.85}
