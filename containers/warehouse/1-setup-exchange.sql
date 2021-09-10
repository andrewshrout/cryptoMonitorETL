DROP TABLE IF EXISTS bitcoin.exchange;
DROP SCHEMA IF EXISTS bitcoin;
DROP TABLE IF EXISTS crypto.asset;
DROP SCHEMA IF EXISTS crypto;

CREATE SCHEMA bitcoin;
CREATE TABLE bitcoin.exchange (
    id VARCHAR(50),
    name VARCHAR(50),
    rank INT,
    percentTotalVolume NUMERIC(8, 5),
    volumeUsd NUMERIC,
    tradingPairs INT,
    socket BOOLEAN,
    exchangeUrl VARCHAR(50),
    updated_unix_millis BIGINT,
    updated_utc TIMESTAMP
);

CREATE SCHEMA crypto;
CREATE TABLE crypto.asset (
    id VARCHAR(50),
    name VARCHAR(50),
    rank INT,
    symbol VARCHAR(5),
    supply NUMERIC,
    marketCapUsd NUMERIC,
    volumeUsd24Hr NUMERIC,
    priceUsd NUMERIC,
    changePercent24Hr NUMERIC,
    vwap24Hr NUMERIC,
    updated_utc TIMESTAMP
);