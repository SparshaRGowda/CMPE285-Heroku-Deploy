from distutils import debug
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "CMPE 285 HW2"

if __name__ == "__mian__":
    app.run(debug==True)