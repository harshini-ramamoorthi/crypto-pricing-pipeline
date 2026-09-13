import requests #import requests library to make API requests

def fetch_crypto_data(): #A function is basically a reusable block of code.

    url = "https://api.coingecko.com/api/v3/coins/markets" 
    ##CoinGecko's 
# markets endpoint, which gives market information about cryptocurrencies.


    params = { #telling the API what data we want

        "vs_currency" : "usd", #Currency in which prices should be returned: We want prices in USD
        "order": "market_cap_desc", #How the coins should be sorted: Highest market cap first
        "per_page": 50, #Number of coins :Top 50
        "page": 1, #Which page of results: First page
        "sparkline": False #Whether historical sparkline data is needed: We don't need it
    }
    
    response = requests.get(url, params = params) # actual api request; requests, send a GET request to this url, using these params
#calls CoinGecko
    
    response.raise_for_status() #stops the pipeline immediately if CoinGecko returns an HTTP error

    data = response.json() #The API response comes back as JSON.

    return data

