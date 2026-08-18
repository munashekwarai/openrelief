from app.core import OfflineStore
def test_offline_create_and_sync():
 s=OfflineStore({"f":{"required":["name"]}});r=s.create("f",{"name":"site"},"worker");remote={};assert r["sync_state"]=="PENDING" and s.sync(remote)==[] and remote[r["id"]]["sync_state"]=="SYNCED"
def test_conflict_resolution():
 s=OfflineStore({"f":{"required":["name"]}});r=s.create("f",{"name":"local"},"w");remote={r["id"]:{**r,"data":{"name":"remote"},"version":2}};assert s.sync(remote);assert s.resolve(r["id"],"remote",remote,"manager")["data"]["name"]=="remote"
