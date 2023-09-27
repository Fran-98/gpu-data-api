import db
from models import gpuBenchmarks

from flask import Flask

app = Flask(__name__)

def run():
    
    pass


if __name__ == '__main__':
    db.Base.metadata.create_all(db.engine) # Start engine and create models/tables
    run()