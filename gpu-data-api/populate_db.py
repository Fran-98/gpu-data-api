import pandas as pd
import db

def populate_db_from_csv(csv_path:str, table_name:str, engine):
    data = pd.read_csv(csv_path)
    data.to_sql(name=table_name, if_exists='replace', index=False, con=engine)


populate_db_from_csv('gpu-data-api/utils/data scrapper/gpu_benchmark_data.csv', 'gpu_benchmark', db.engine)
populate_db_from_csv('gpu-data-api/utils/data scrapper/gpu_specs_data.csv', 'gpu_spec', db.engine)