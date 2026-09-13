from google.cloud import bigquery #imports the BigQuery Python library
from datetime import date #to show todays date

def load_crypto_data(df):
    client = bigquery.Client(project="crypto-pricing-pipeline") 
    #bigquery.Client(...) → creates our connection/client for BigQuery.
    #project="crypto-pricing-pipeline" → tells it which GCP project we're working with.
    #client → stores that connection so we'll use it later to load df.

    table_id = "crypto-pricing-pipeline.crypto_data.crypto_prices"
    #to tell Python which BigQuery table we're going to load.
    #This identifies: Project → crypto-pricing-pipeline 
    #Dataset → crypto_data Table → crypto_prices

    partition_table_id = f"{table_id}${date.today().strftime('%Y%m%d')}"
    #create a destination specifically for today's partition: 
    #for today: crypto-pricing-pipeline.crypto_data.crypto_prices$20260910

    # It tells Python:
    # df → the data we cleaned
    # partition_table_id → today's BigQuery partition
    # job_config → how to load the data

    job_config = bigquery.LoadJobConfig(write_disposition="WRITE_TRUNCATE")

    job = client.load_table_from_dataframe(df, partition_table_id, job_config=job_config)
    #It tells Python: df → the data we cleaned; 
    #table_id → where to put it job_config → how to load it

    job.result()

    print("Data loaded successfully into BigQuery!")
