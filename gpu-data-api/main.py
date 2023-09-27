import db
from models import gpuBenchmarks

from flask import Flask, request, jsonify

app = Flask(__name__)

def run():
    app.run()
    pass

@app.route('/gpu_info', methods=['GET'])
def gpu_info():
    args = request.args
    return args


if __name__ == '__main__':
    db.Base.metadata.create_all(db.engine) # Start engine and create models/tables
    run()