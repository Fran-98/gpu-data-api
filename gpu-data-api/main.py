import db
import utils.misc
from models import gpuBenchmarks, gpu_spec
from flask import Flask, request, jsonify
from sqlalchemy import MetaData, Table
from sqlalchemy.orm import sessionmaker
import pandas as pd




app = Flask(__name__)

def run():
    app.run()
    pass

@app.route('/')
def buenas():
    return jsonify({"message": "Buenas!!!"})


@app.route('/gpu_info_all', methods=['GET'])
def gpu_info_all():
    
    try:
        Session = sessionmaker(bind=db.engine)
        session = Session()
        query=f'SELECT * FROM gpu_spec'
        gpu_info_query = pd.read_sql_query(query, db.engine)
        gpu_info_list=gpu_info_query.values.tolist()
        gpu_info=[]

        for gpu in gpu_info_list:
            gpu_data_formated = {
                "manufacturer":gpu[0],
                "name":gpu[1],
                "releaseYear":gpu[2],
                "memory_size":gpu[3],
                "memory_bus_width":gpu[4],
                "gpu_clock":gpu[5],
                "memory_clock":gpu[6],
                "unified_shader":gpu[7],
                "tmu":gpu[8],
                "rop":gpu[9],
                "pixel_shader":gpu[10],
                "vertex_shader":gpu[11],
                "igp":gpu[12],
                "bus":gpu[13],
                "memory_type":gpu[14],
                "gpu_chip":gpu[15],
            }
            gpu_info.append(gpu_data_formated)

        session.close()
        return jsonify({'all gpus':gpu_info})
    except Exception as ex:
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



@app.route('/gpu_info/<manufacturer>', methods=['GET'])
def manufacture(manufacturer):
    try:
        Session = sessionmaker(bind=db.engine)
        session = Session()
        query=f"SELECT * FROM gpu_spec WHERE manufacturer = '{manufacturer}' "
        gpu_info = pd.read_sql_query(query, db.engine)
        gpu_info_list=gpu_info.values.tolist()
        gpu_manufacturer =[]
        for gpu in gpu_info_list:
            gpu_data_formated = {
                "name":gpu[1],
                "releaseYear":gpu[2],
                "memory_size":gpu[3],
                "memory_bus_width":gpu[4],
                "gpu_clock":gpu[5],
                "memory_clock":gpu[6],
                "unified_shader":gpu[7],
                "tmu":gpu[8],
                "rop":gpu[9],
                "pixel_shader":gpu[10],
                "vertex_shader":gpu[11],
                "igp":gpu[12],
                "bus":gpu[13],
                "memory_type":gpu[14],
                "gpu_chip":gpu[15],
            }
            gpu_manufacturer.append(gpu_data_formated)
        session.close()
        return jsonify({'gpu according to manufacturer':gpu_manufacturer})
        
    except Exception as ex:
        return 'error'


@app.route('/gpu_in_rank/<rank>', methods=['GET'])
def get_rank(rank):
    try:
        real_rank=int(rank)-1
        Session = sessionmaker(bind=db.engine)
        session = Session()
        query=f"SELECT * FROM gpu_benchmark ORDER BY averageScore DESC LIMIT 1 OFFSET {real_rank}; "
        gpu_info_query = pd.read_sql_query(query, db.engine)
        gpu_info_list=gpu_info_query.values.tolist()
        gpu_in_rank =[]
        for gpu in gpu_info_list:
            gpu_data_formated = {
                "gpuName":gpu_info_list[0][0],
                "averageScore":gpu_info_list[0][1],
                "price":gpu_info_list[0][2],
            }
            gpu_in_rank.append(gpu_data_formated)
        session.close()
        return jsonify({'gpu in rank':gpu_in_rank})

    except Exception as ex:
        return 'error'


@app.route('/gpu_info_post', methods=['POST'])
def gpu_post():
    
    try:
        Session = sessionmaker(bind=db.engine)
        session = Session()
        
        data = request.json
        manufacturer = data.get("manufacturer")
        gpuName = data.get("gpuName")  
        releaseYear = data.get("releaseYear")
        memSize = data.get("memorySize")  
        memBusWidth = data.get("memoryBusWidth")  
        gpuClock = data.get("gpuClock")
        memClock = data.get("memoryClock")  
        unifiedShader = data.get("unifiedShader")
        tmu = data.get("tmu")
        rop = data.get("rop")
        pixelShader = data.get("pixelShader")
        vertexShader = data.get("vertexShader")
        igp = data.get("igp")
        bus = data.get("bus")
        memType = data.get("memoryType") 
        gpuChip = data.get("gpuChip")
        averageScore = data.get("averageScore")
        price = data.get("price")

        gpu_added = gpu_spec(manufacturer=manufacturer, gpuName=gpuName, releaseYear=releaseYear, memSize=memSize, memBusWidth=memBusWidth, gpuClock=gpuClock, memClock=memClock, unifiedShader=unifiedShader, tmu=tmu, rop=rop, pixelShader=pixelShader, vertexShader=vertexShader, igp=igp, bus=bus, memType=memType, gpuChip=gpuChip,)
        session.add(gpu_added)
        session.commit()


        gpu_bench_added=gpuBenchmarks(gpuName=gpuName, averageScore=averageScore, price=price)
        session.add(gpu_bench_added)
        session.commit()

        session.close()
        return jsonify({'Messege':'GPU added'})
    except Exception as ex:
        print(str(ex))
        return f'error {ex}'


@app.route('/gpu_delete/<gpu_name>', methods=['DELETE'])
def gpu_delete(gpu_name):
    try:
        print(f"Received DELETE request for GPU name: {gpu_name}")
        Session = sessionmaker(bind=db.engine)
        session = Session()
        
        gpu_to_delete_spec = session.query(gpu_spec).filter_by(gpuName=gpu_name).first()
        session.delete(gpu_to_delete_spec)
        session.commit()

        gpu_to_delete_Benchmark = session.query(gpuBenchmarks).filter_by(gpuName=gpu_name).first()
        session.delete(gpu_to_delete_Benchmark)
        session.commit()


        session.close()

        return jsonify({'Messege':'GPU delete'})

    except Exception as ex:
        return f'error {ex}'


@app.route('/gpu_update/<gpu_name>', methods=['PUT'])
def gpu_update(gpu_name):
    try:
        Session = sessionmaker(bind=db.engine)
        session = Session()
        

        gpu_to_update_spec = session.query(gpu_spec).filter_by(gpuName=gpu_name).first()

        gpu_to_update_spec.manufacturer = request.json['manufacturer']
        gpu_to_update_spec.gpuName = request.json['gpuName']
        gpu_to_update_spec.releaseYear = request.json['releaseYear']
        gpu_to_update_spec.memSize = request.json['memSize']
        gpu_to_update_spec.memBusWidth = request.json['memBusWidth']
        gpu_to_update_spec.gpuClock = request.json['gpuClock']
        gpu_to_update_spec.memClock = request.json['memClock']
        gpu_to_update_spec.unifiedShader = request.json['unifiedShader']
        gpu_to_update_spec.tmu = request.json['tmu']
        gpu_to_update_spec.rop = request.json['rop']
        gpu_to_update_spec.pixelShader = request.json['pixelShader']
        gpu_to_update_spec.vertexShader = request.json['vertexShader']
        gpu_to_update_spec.igp = request.json['igp']
        gpu_to_update_spec.bus = request.json['bus']
        gpu_to_update_spec.memType = request.json['memType']
        gpu_to_update_spec.gpuChip = request.json['gpuChip']
        session.commit()

        gpu_to_update_Benchmark = session.query(gpuBenchmarks).filter_by(gpuName=gpu_name).first()

        gpu_to_update_Benchmark.gpuName = request.json['gpuName']
        gpu_to_update_Benchmark.averageScore = request.json['averageScore']
        gpu_to_update_Benchmark.price = request.json['price']

        session.commit()
        session.close()

        return jsonify({'Message': 'GPU updated'})
        

    except Exception as ex:
        return f'error {ex}'



def error_404(error):
    return "<h1>Página inexistente...</h1>"


if __name__ == '__main__':
    db.Base.metadata.create_all(db.engine) # Start engine and create models/tables
    app.register_error_handler(404, error_404)
    app.run(debug=True)