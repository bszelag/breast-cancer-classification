# breast-cancer-classification

Avaible end-points:
  - http://0.0.0.0:5000/dev/status (GET)
  - http://0.0.0.0:5000/<alg_name>/predict (POST)
  - http://0.0.0.0:5000/<alg_name>/train (POST)
  
  - http://0.0.0.0:5000/stats/<alg_name> (GET)
  - http://0.0.0.0:5000/stats/<alg_name>/history/\<num\> (GET)
  - http://0.0.0.0:5000/stats/<alg_name>/total_accuracy (GET)
  - http://0.0.0.0:5000/stats/<alg_name>/total_accuracy/reset (GET)
  
  
Example request in curl:

 - `curl -F 'file=@./train.data' -F options='{"dist": "MultinominalNB"}' http://0.0.0.0:5000/bayes/train `
 - `curl -X POST -F "file=@./test.data" -F "with_target=true" 0.0.0.0:5000/bayes/predict`
 - `curl http://0.0.0.0:5000/bayes/history/2` (returns maximum 2 last records)
