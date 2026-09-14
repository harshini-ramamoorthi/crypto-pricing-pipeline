from src.transform import transform_crypto_data


def test_required_columns():
    data = [
        {
            "id": "bitcoin",
            "symbol": "btc",
            "name": "Bitcoin",
            "current_price": 50000,
            "market_cap": 1000000000,
            "total_volume": 50000000,
            "price_change_percentage_24h": 2.5
        }
    ]

    df = transform_crypto_data(data)

    expected_columns = [
        "id",
        "symbol",
        "name",
        "price_usd",
        "market_cap_usd",
        "volume_24h_usd",
        "price_change_24h_pct",
        "price_date"
    ]

    assert list(df.columns) == expected_columns


def test_null_price_change_is_filled():
    data = [
        {
            "id": "bitcoin",
            "symbol": "btc",
            "name": "Bitcoin",
            "current_price": 50000,
            "market_cap": 1000000000,
            "total_volume": 50000000,
            "price_change_percentage_24h": None
        }
    ]

    df = transform_crypto_data(data)

    assert df["price_change_24h_pct"].iloc[0] == 0


def test_duplicate_rows_are_removed():
    data = [
        {
            "id": "bitcoin",
            "symbol": "btc",
            "name": "Bitcoin",
            "current_price": 50000,
            "market_cap": 1000000000,
            "total_volume": 50000000,
            "price_change_percentage_24h": 2.5
        },
        {
            "id": "bitcoin",
            "symbol": "btc",
            "name": "Bitcoin",
            "current_price": 50000,
            "market_cap": 1000000000,
            "total_volume": 50000000,
            "price_change_percentage_24h": 2.5
        }
    ]

    df = transform_crypto_data(data)

    assert len(df) == 1


def test_output_has_expected_number_of_rows():
    data = [
        {
            "id": "bitcoin",
            "symbol": "btc",
            "name": "Bitcoin",
            "current_price": 50000,
            "market_cap": 1000000000,
            "total_volume": 50000000,
            "price_change_percentage_24h": 2.5
        },
        {
            "id": "ethereum",
            "symbol": "eth",
            "name": "Ethereum",
            "current_price": 3000,
            "market_cap": 500000000,
            "total_volume": 30000000,
            "price_change_percentage_24h": 1.5
        }
    ]

    df = transform_crypto_data(data)

    assert len(df) == 2