import requests  #import requests library to make API requests
import pandas as pd #import pandas library
from datetime import date #to show todays date
from google.cloud import bigquery #imports the BigQuery Python library

client = bigquery.Client(project="crypto-pricing-pipeline") 
#bigquery.Client(...) → creates our connection/client for BigQuery.
#project="crypto-pricing-pipeline" → tells it which GCP project we're working with.
#client → stores that connection so we'll use it later to load df.

table_id = "crypto-pricing-pipeline.crypto_data.crypto_prices"
#to tell Python which BigQuery table we're going to load.
#This identifies: Project → crypto-pricing-pipeline 
#Dataset → crypto_data Table → crypto_prices

url = "https://api.coingecko.com/api/v3/coins/markets"  #CoinGecko's 
# markets endpoint, which gives market information about cryptocurrencies.

params = {  #telling the API what data we want

    "vs_currency" : "usd" , #Currency in which prices should be returned: We want prices in USD
    "order" : "market_cap_desc", #How the coins should be sorted: Highest market cap first
    "per_page" : 50, #Number of coins :Top 50
    "page" : 1, #Which page of results: First page
    "sparkline" : False #Whether historical sparkline data is needed: We don't need it

} 

response = requests.get(url, params = params) # actual api request; requests, send a GET request to this url, using these params

data = response.json() #The API response comes back as JSON.

df = pd.DataFrame(data) #gives data from the dataframe

df = df[["id", "symbol", "name", "current_price", "market_cap",
 "total_volume", "price_change_percentage_24h"]]

df =df.rename(columns={"current_price" :"price_usd", 
"market_cap": "market_cap_usd", "total_volume":"volume_24h_usd", 
"price_change_percentage_24h":"price_change_24h_pct"}) #The first df means: "I want to modify my DataFrame." 
#Then: df[ ... ] means: "From this DataFrame, give me these columns."

df["price_date"] = date.today() # shows todays date to organize the data; put it into every row's price_date column

# print(data[0]) #data is a list; Give me the first cryptocurrency returned by the API.
#data[0] gave us the first dictionary. And something like: data[0]["name"] would give: Bitcoin
#while: data[0]["current_price"] would give the current Bitcoin price.

# print(len(data)) #length of the data i.e. 50

print(df.isnull().sum()) #Check missing values/ null value

df["price_change_24h_pct"] = df["price_change_24h_pct"].fillna(0) #we 
# know from our check that this is the column with the missing value.

df = df.drop_duplicates() #If CoinGecko ever returns duplicate rows 
#for some reason, our transformation step will remove them automatically.

#print(df.head()) #Shows the first 5 rows of the DataFrame.

print("Duplicate Rows: ", df.duplicated().sum()) #checks for any duplicate rows in the dataset

print(df.isnull().sum()) #Fill it with 0

#print(df.info()) #to check the datatypes and the complete details of our exracted dataset

df.info()

job_config = bigquery.LoadJobConfig(write_disposition="WRITE_APPEND")
#WRITE_APPEND means: Add today's 50 crypto records to the existing 
#table without deleting previous data.

job = client.load_table_from_dataframe(df, table_id, job_config=job_config)
#It tells Python: df → the data we cleaned; 
#table_id → where to put it job_config → how to load it

job.result()

print("Data loaded successfully into BigQuery!")
