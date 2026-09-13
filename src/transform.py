import pandas as pd #import pandas library
from datetime import date #to show todays date

def transform_crypto_data(data):

    df = pd.DataFrame(data) #gives data from the dataframe
    
    df = df[["id", "symbol", "name", "current_price", "market_cap",
 "total_volume", "price_change_percentage_24h"]]
 
    df =df.rename(columns={
    "current_price" :"price_usd",
    "market_cap": "market_cap_usd", "total_volume":"volume_24h_usd",
    "price_change_percentage_24h":"price_change_24h_pct"
    }) 
    #The first df means: "I want to modify my DataFrame." 
    #Then: df[ ... ] means: "From this DataFrame, give me these columns."
    df["price_date"] = date.today() # shows todays date to organize the data; put it into every row's price_date column
    
    # print(data[0]) #data is a list; Give me the first cryptocurrency returned by the API
    #data[0] gave us the first dictionary. And something like: data[0]["name"] would give: Bitcoin
    #while: data[0]["current_price"] would give the current Bitcoin price.
    # print(len(data)) #length of the data i.e. 50
    
    print(df.isnull().sum()) #Check missing values/ null value
    
    df["price_change_24h_pct"] = df["price_change_24h_pct"].fillna(0) #we 
    # know from our check that this is the column with the missing value.
    
    df = df.drop_duplicates() #If CoinGecko ever returns duplicate rows 
    #for some reason, our transformation step will remove them automatically.
    
    #print(df.head()) #Shows the first 5 rows of the DataFrame.
    
    print("Duplicate Rows: ", df.duplicated().sum())
    #checks for any duplicate rows in the dataset
    print(df.isnull().sum()) #Fill it with 0
    
    #print(df.info()) #to check the datatypes and the complete details of our exracted dataset

    df.info()

    return df