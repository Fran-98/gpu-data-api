import pandas as pd

def populate_db_from_csv(csv_path:str, table_name:str, engine):
    data = pd.read_csv(csv_path)
    data.to_sql(name=table_name, if_exists='replace', index=False, con=engine)


