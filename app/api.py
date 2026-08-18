from fastapi import FastAPI
from pydantic import BaseModel
from .core import OfflineStore
app=FastAPI(title="OpenRelief")
store=OfflineStore({"assessment":{"required":["location","needs"]}});server={}
class Record(BaseModel):form_id:str;data:dict;user:str
@app.post("/records")
def create(x:Record):return store.create(x.form_id,x.data,x.user)
@app.post("/sync")
def sync():return {"conflicts":store.sync(server),"queued":len(store.queue)}
