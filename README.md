# breast-cancer-classification

Avaible end-points:
  - http://0.0.0.0:5000/dev/status (GET)
  - http://0.0.0.0:5000/bayes/predict (POST)
  - http://0.0.0.0:5000/bayes/train (POST)
  - http://0.0.0.0:5000/bayes/stats (GET)
  
  
Example request in curl:

 - `curl -F 'file=@./train.data' http://0.0.0.0:5000/bayes/train`
 - `curl -F 'curl -F 'file=@./test.data' http://0.0.0.0:5000/bayes/predict`
