from src.backend.classificators_module.classificators_controller import algorithms
from src.backend import db
import pickle

for k in algorithms:
    record = db.models.find_one({"_id": k})
    if record is not None:
        algorithms[k].model = pickle.loads(record["pickle"])
        algorithms[k].mask_ = record["mask"]

