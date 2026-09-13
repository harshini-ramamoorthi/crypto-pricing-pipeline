from src.extract import fetch_crypto_data #From the src.extract file, 
#the fetch_crypto_data function.

from src.transform import transform_crypto_data #From the src.extract
#file, fetch the transform_crypto_data function

from src.load import load_crypto_data #From the src.extract
#file, fetch the load_crypto_data function


data = fetch_crypto_data() # to fetch datta from extact.py

df = transform_crypto_data(data) #to fetch data from transform.py

load_crypto_data(df)

# delete_query = f"""DELETE FROM `{table_id}` WHERE price_date = '{date.today()}'"""

# delete_job = client.query(delete_query)

# delete_job.result()

#job_config = bigquery.LoadJobConfig(write_disposition="WRITE_APPEND")
#WRITE_APPEND means: Add today's 50 crypto records to the existing 
#table without deleting previous data.
