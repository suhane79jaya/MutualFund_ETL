#Top 5 Funds by aum
SELECT
    fund_house,aum_crore    
FROM dim_fund
ORDER BY aum_crore DESC
LIMIT 5;

#Average NAV Per Month
SELECT
    strftime('%Y-%m', date) AS month,
    ROUND(AVG(nav), 2) AS avg_nav
FROM fact_nav_history
GROUP BY month
ORDER BY month;

SELECT
    strftime('%Y', transaction_date) AS year,
    SUM(amount) AS sip_amount
FROM fact_transactions
WHERE transaction_type = 'SIP'
GROUP BY year
ORDER BY year;

-- Transactions by State
SELECT
    state,
    COUNT(*) AS total_transactions,
    SUM(amount) AS total_amount
FROM fact_transactions
GROUP BY state
ORDER BY total_amount DESC;

-- Funds with Expense Ratio Less Than 1%
SELECT
    scheme_name,
    expense_ratio_pct
FROM fact_scheme_performance
WHERE expense_ratio_pct < 1
ORDER BY expense_ratio_pct;
--Top 10 Investors by Investment Amount
SELECT
    investor_id,
    SUM(amount_inr) AS total_invested
FROM fact_transactions
GROUP BY investor_id
ORDER BY total_invested DESC
LIMIT 10;
--Monthly Transaction Volume
SELECT
    strftime('%Y-%m', transaction_date) AS month,
    COUNT(*) AS transaction_count
FROM fact_transactions
GROUP BY month
ORDER BY month;

--Fund Category-wise Average Return
SELECT
    category,
    ROUND(AVG(return_1yr_pct), 2) AS avg_return
FROM fact_scheme_performance
GROUP BY category
ORDER BY avg_return DESC;

--Highest NAV Recorded for Each Fund
SELECT
    amfi_code,
    MAX(nav) AS highest_nav
FROM fact_nav_history
GROUP BY amfi_code
ORDER BY highest_nav DESC;

--Transaction Type Distribution
SELECT
    transaction_type,
    COUNT(*) AS count_transactions,
    ROUND(100.0 * COUNT(*) /
        (SELECT COUNT(*) FROM fact_transactions), 2)
        AS percentage
FROM fact_transactions
GROUP BY transaction_type;