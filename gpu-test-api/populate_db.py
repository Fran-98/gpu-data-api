import pandas as pd

def populate_db_from_csv(csv_path:str, engine):
    data = pd.read_csv(csv_path)
    data.to_sql(name='gpu_benchmark_db', if_exists='replace', index=False, con=engine)


