from src.backend import app
from flask_cors import CORS

CORS(app)
app.run(host='0.0.0.0', port=5000, debug=True)
