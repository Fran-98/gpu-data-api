import db
from models import GPU
from populate_db import populate_db_from_csv

def run():

    # Maybe a workflow could be: See if tables are populated -> populate them if they are not
    populate_db_from_csv('utils/data scrapper/gpu_benchmark_data.csv', 'gpu_benchmark', db.engine)
    populate_db_from_csv('utils/data scrapper/gpu_specs_data.csv', 'gpu_spec', db.engine)
    

if __name__ == '__main__':
    db.Base.metadata.create_all(db.engine) # Start engine and create models/tables
    run()