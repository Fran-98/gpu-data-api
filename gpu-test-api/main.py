import db
from models import GPU
from populate_db import populate_db_from_csv

def run():
    populate_db_from_csv('utils/data scrapper/gpu_benchmark_data.csv', db.engine)
    pass

if __name__ == '__main__':
    db.Base.metadata.create_all(db.engine)
    run()