CREATE TABLE IF NOT EXISTS dim_fund (
    fund_key INTEGER PRIMARY KEY AUTOINCREMENT,
    amfi_code INTEGER UNIQUE,
    scheme_name TEXT
)
CREATE TABLE IF NOT EXISTS dim_date (
    date_key INTEGER PRIMARY KEY,
    full_date DATE
)
CREATE TABLE IF NOT EXISTS fact_nav (
    nav_key INTEGER PRIMARY KEY,
    fund_key INTEGER,
    date_key INTEGER,
    nav_value REAL,
    FOREIGN KEY (fund_key) REFERENCES dim_fund(fund_key),
    FOREIGN KEY (date_key) REFERENCES dim_date(date_key))

CREATE TABLE IF NOT EXISTS fact_transactions (
    transaction_key INTEGER PRIMARY KEY AUTOINCREMENT,
    fund_key INTEGER NOT NULL,
    date_key INTEGER NOT NULL,

    investor_id TEXT,
    transaction_type TEXT,
    amount REAL NOT NULL,
    units REAL,
    kyc_status TEXT,

    FOREIGN KEY (fund_key)
        REFERENCES dim_fund(fund_key),

    FOREIGN KEY (date_key)
        REFERENCES dim_date(date_key)
)

CREATE TABLE IF NOT EXISTS fact_performance (
    performance_key INTEGER PRIMARY KEY AUTOINCREMENT,
    fund_key INTEGER NOT NULL,
    date_key INTEGER NOT NULL,

    return_1y REAL,
    return_3y REAL,
    return_5y REAL,
    benchmark_return REAL,

    FOREIGN KEY (fund_key)
        REFERENCES dim_fund(fund_key),

    FOREIGN KEY (date_key)
        REFERENCES dim_date(date_key)
)

CREATE TABLE IF NOT EXISTS fact_aum (
    aum_key INTEGER PRIMARY KEY AUTOINCREMENT,
    fund_key INTEGER NOT NULL,
    date_key INTEGER NOT NULL,

    aum_value REAL NOT NULL,

    FOREIGN KEY (fund_key)
        REFERENCES dim_fund(fund_key),

    FOREIGN KEY (date_key)
        REFERENCES dim_date(date_key)
)
INSERT INTO dim_fund (fund_key,amfi_code,scheme_name)
VALUES (01,2601,'Fund A');

INSERT INTO dim_fund (fund_key,amfi_code,scheme_name)
VALUES (02,2602,'Fund B');