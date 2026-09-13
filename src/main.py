from extract import fetch_crypto_data
from transform import transform_crypto_data
from load import load_crypto_data


data = fetch_crypto_data()

df = transform_crypto_data(data)

load_crypto_data(df)