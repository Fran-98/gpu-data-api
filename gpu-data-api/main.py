import db
from models import gpuBenchmarks
from flask import Flask, request, jsonify
from sqlalchemy.orm import sessionmaker
import pandas as pd




app = Flask(__name__)

def run():
    app.run()
    pass
"""
@app.route('/gpu_info', methods=['GET'])
def gpu_info():
    args = request.args
    return args
"""
@app.route('/')
def buenas():
    return jsonify({"message": "Buenas!!!"})


@app.route('/gpu_info', methods=['GET'])
def gpu_info():
    try:
        Session = sessionmaker(bind=db.engine)
        session = Session()
        query=f'SELECT * FROM gpu_spec'
        gpu_info = pd.read_sql_query(query, db.engine)
        gpu_info_json=gpu_info.to_dict()
        return jsonify({'datos':gpu_info_json})
    except Exception as ex:
        return 'error'






@app.route('/gpu_info/<manufacturer>', methods=['GET'])
def manufacture(manufacturer):
    try:
        Session = sessionmaker(bind=db.engine)
        session = Session()
        query=f"SELECT * FROM gpu_spec WHERE manufacturer = '{manufacturer}' "
        gpu_info = pd.read_sql_query(query, db.engine)
        gpu_info_json=gpu_info.to_dict()
        return jsonify({'datos':gpu_info_json})
    except Exception as ex:
        return 'error'


@app.route('/gpu_in_rank/<rank>', methods=['GET'])
def manufacture(rank):
    try:
        Session = sessionmaker(bind=db.engine)
        session = Session()
        if rank == 1:
            query="SELECT * FROM gpu_benchmark ORDER BY score DESC LIMIT 1 ; "
            gpu_info = pd.read_sql_query(query, db.engine)
            gpu_info_json=gpu_info.to_dict()
            return jsonify({'datos':gpu_info_json})
        else:
            query=f"SELECT * FROM gpu_benchmark ORDER BY score DESC LIMIT 1 OFFSET {rank - 1}; "
            gpu_info = pd.read_sql_query(query, db.engine)
            gpu_info_json=gpu_info.to_dict()
            return jsonify({'datos':gpu_info_json})

    except Exception as ex:
        return 'error'





def error_404(error):
    return "<h1>Página inexistente...</h1>"


if __name__ == '__main__':
    db.Base.metadata.create_all(db.engine) # Start engine and create models/tables
    app.register_error_handler(404, error_404)
    app.run(debug=True)