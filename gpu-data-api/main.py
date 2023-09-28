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
        datos_guardados = pd.read_sql_query(query, db.engine)
        datos_guardados_json=datos_guardados.to_dict()
        return jsonify({'datos':datos_guardados_json})
    except Exception as ex:
        return 'error'





def error_404(error):
    return "<h1>Página inexistente...</h1>"


if __name__ == '__main__':
    db.Base.metadata.create_all(db.engine) # Start engine and create models/tables
    app.register_error_handler(404, error_404)
    app.run(debug=True)