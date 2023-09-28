import db
import utils.misc
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


@app.route('/gpu_info_all', methods=['GET'])
def gpu_info_all():
    
    try:
        Session = sessionmaker(bind=db.engine)
        session = Session()
        query=f'SELECT * FROM gpu_spec'
        datos_guardados = pd.read_sql_query(query, db.engine)
        datos_guardados_json=datos_guardados.to_dict()
        return jsonify({'datos':datos_guardados_json})
    except Exception as e:
        return 'error'



@app.route('/gpu_info', methods=['GET'])
def gpu_info():
    """
    Endpoint to retrieve gpu info by its name
    {
    "gpus":[
        {   
            "name":
            "manufacturer":
            "release":
            "memory_size":
            "memory_bus_width":
            "gpu_clock":
            "memory_clock":
            "unified_shader":
            "tmu":
            "rop":
            "pixel_shader":
            "vertex_shader":
            "igp":
            "bus":
            "memory_type":
            "gpu_chip":
        },
            ]
    }

    """
    try:
        gpus = request.args.getlist('name')
        Session = sessionmaker(bind=db.engine)
        session = Session()

        gpus_obtained = []
        for gpu in gpus:
            query=f'SELECT * FROM gpu_spec WHERE gpuName LIKE "%{gpu}%"'
            db_query = pd.read_sql_query(query, db.engine)
            # From all the querys select the most appropiate

            matched_name = utils.misc.get_closest_match(gpu, db_query['gpuName'].to_list())
            gpu_data = db_query.loc[db_query['gpuName'] == matched_name].to_dict(orient= 'list')

            gpu_data_formated = {   
                                "name": gpu_data['gpuName'][0],
                                "manufacturer": gpu_data['manufacturer'][0],
                                "release": gpu_data['releaseYear'][0],
                                "memory_size": gpu_data['memSize'][0],
                                "memory_bus_width": gpu_data['memBusWidth'][0],
                                "gpu_clock": gpu_data['gpuClock'][0],
                                "memory_clock": gpu_data['memClock'][0],
                                "unified_shader": gpu_data['unifiedShader'][0],
                                "tmu": gpu_data['tmu'][0],
                                "rop": gpu_data['rop'][0],
                                "pixel_shader": gpu_data['pixelShader'][0],
                                "vertex_shader": gpu_data['vertexShader'][0], 
                                "igp": gpu_data['igp'][0],
                                "bus": gpu_data['bus'][0],
                                "memory_type": gpu_data['memType'][0],
                                "gpu_chip": gpu_data['gpuChip'][0],
                                }
            
            gpus_obtained.append(gpu_data_formated)
        return jsonify({'gpus':gpus_obtained})
    
    except Exception as e:
        return f'Error {e}'


def error_404(error):
    return "<h1>Página inexistente...</h1>"


if __name__ == '__main__':
    db.Base.metadata.create_all(db.engine) # Start engine and create models/tables
    app.register_error_handler(404, error_404)
    app.run(debug=True)