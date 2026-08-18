import copy,time,uuid
class OfflineStore:
 def __init__(self,forms):self.forms=forms;self.records={};self.queue=[];self.audit=[]
 def create(self,form_id,data,user):
  form=self.forms[form_id];missing=[x for x in form["required"] if not data.get(x)]
  if missing:raise ValueError("missing: "+",".join(missing))
  rid=str(uuid.uuid4());r={"id":rid,"form_id":form_id,"data":copy.deepcopy(data),"version":1,"updated_at":time.time(),"updated_by":user,"sync_state":"PENDING"};self.records[rid]=r;self.queue.append(copy.deepcopy(r));self.audit.append({"action":"CREATE","record_id":rid,"user":user});return r
 def sync(self,server):
  conflicts=[]
  for local in list(self.queue):
   remote=server.get(local["id"])
   if remote and remote["version"]>=local["version"] and remote["data"]!=local["data"]:local["sync_state"]="CONFLICT";conflicts.append({"local":local,"remote":remote});continue
   server[local["id"]]={**local,"sync_state":"SYNCED"};self.records[local["id"]]["sync_state"]="SYNCED";self.queue.remove(local)
  return conflicts
 def resolve(self,rid,chosen,server,user):
  if chosen not in {"local","remote"}:raise ValueError("resolution must be local or remote")
  selected=self.records[rid] if chosen=="local" else server[rid];merged={**selected,"version":max(self.records[rid]["version"],server[rid]["version"])+1,"updated_by":user,"updated_at":time.time(),"sync_state":"SYNCED"};self.records[rid]=server[rid]=merged;self.queue=[x for x in self.queue if x["id"]!=rid];self.audit.append({"action":"RESOLVE_"+chosen.upper(),"record_id":rid,"user":user});return merged
