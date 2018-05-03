from src.backend.classificators_module.classificators_controller import algorithms
from src.backend import db
import pickle
import bson.json_util as json_util

for k in algorithms:
    record = db.models.find_one({"_id": k})
    if record is not None:
        algorithms[k].model = pickle.loads(record["pickle"])
        if "mask" in record:
            algorithms[k].mask_ = json_util.loads(record["mask"])
