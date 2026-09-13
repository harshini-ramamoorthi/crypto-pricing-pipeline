select name, symbol, price_usd, price_change_24h_pct, market_cap_usd, volume_24h_usd

from `crypto-pricing-pipeline.crypto_data.crypto_prices` 
where price_date = (select MAX(price_date) --Get today's crypto records
from `crypto-pricing-pipeline.crypto_data.crypto_prices`)

order by price_change_24h_pct asc limit 10; --Sort by 24-hour price change and Keep only the top 10

-- ASC means smallest → largest, so the most 
-- negative price changes appear first.

-- For example:

-- -8.5%
-- -6.2%
-- -4.1%
-- ...
-- +2.3%