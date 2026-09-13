SELECT
    name,
    symbol,
    market_cap_usd,
    ROUND(
        market_cap_usd /
        SUM(market_cap_usd) OVER () * 100,
        2 
        
        --That calculates the total market cap of all the crypto records for the latest date.
        --and individual crypto market cap ÷ total market cap × 100
        --so it looks like
        --Bitcoin       55.32%
        -- Ethereum      14.21%
        -- Tether         4.12%
        -- ...

    ) AS market_cap_share_pct
FROM
    `crypto-pricing-pipeline.crypto_data.crypto_prices`
WHERE
    price_date = (
        SELECT MAX(price_date)
        FROM `crypto-pricing-pipeline.crypto_data.crypto_prices`
    )
ORDER BY
    market_cap_share_pct DESC
LIMIT 10;