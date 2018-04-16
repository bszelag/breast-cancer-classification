# breast-cancer-classification

Avaible end-points:
  - http://0.0.0.0:5000/dev/status (GET)
  - http://0.0.0.0:5000/bayes/predict (POST)
  - http://0.0.0.0:5000/bayes/train (POST)
  - http://0.0.0.0:5000/bayes/stats (GET)
  - http://0.0.0.0:5000/tree/predict (POST)
  - http://0.0.0.0:5000/tree/train (POST)
  - http://0.0.0.0:5000/tree/stats (GET)
  - http://0.0.0.0:5000/svm/predict (POST)
  - http://0.0.0.0:5000/svm/train (POST)
  - http://0.0.0.0:5000/svm/stats (GET)
  
Example request in curl:

 - `curl -F 'file=@./train.data' http://0.0.0.0:5000/bayes/train`
 - `-X POST -F "file=@./test.data" -F "with_target=true" 0.0.0.0:5000/bayes/predict`
