# fund_master

| Column Name        | Data Type   | Business Definition   |
|:-------------------|:------------|:----------------------|
| amfi_code          | int64       |                       |
| fund_house         | object      |                       |
| scheme_name        | object      |                       |
| category           | object      |                       |
| sub_category       | object      |                       |
| plan               | object      |                       |
| launch_date        | object      |                       |
| benchmark          | object      |                       |
| expense_ratio_pct  | float64     |                       |
| exit_load_pct      | float64     |                       |
| min_sip_amount     | int64       |                       |
| min_lumpsum_amount | int64       |                       |
| fund_manager       | object      |                       |
| risk_category      | object      |                       |
| sebi_category_code | object      |                       |

# nav_history

| Column Name   | Data Type   | Business Definition   |
|:--------------|:------------|:----------------------|
| amfi_code     | int64       |                       |
| date          | object      |                       |
| nav           | float64     |                       |

# aum_by_fund_house

| Column Name    | Data Type   | Business Definition   |
|:---------------|:------------|:----------------------|
| date           | object      |                       |
| fund_house     | object      |                       |
| aum_lakh_crore | float64     |                       |
| aum_crore      | int64       |                       |
| num_schemes    | int64       |                       |

# monthly_sip_inflows

| Column Name               | Data Type   | Business Definition   |
|:--------------------------|:------------|:----------------------|
| month                     | object      |                       |
| sip_inflow_crore          | int64       |                       |
| active_sip_accounts_crore | float64     |                       |
| new_sip_accounts_lakh     | float64     |                       |
| sip_aum_lakh_crore        | float64     |                       |
| yoy_growth_pct            | float64     |                       |

# category_inflows

| Column Name      | Data Type   | Business Definition   |
|:-----------------|:------------|:----------------------|
| month            | object      |                       |
| category         | object      |                       |
| net_inflow_crore | float64     |                       |

# industry_folio_count

| Column Name         | Data Type   | Business Definition   |
|:--------------------|:------------|:----------------------|
| month               | object      |                       |
| total_folios_crore  | float64     |                       |
| equity_folios_crore | float64     |                       |
| debt_folios_crore   | float64     |                       |
| hybrid_folios_crore | float64     |                       |
| others_folios_crore | float64     |                       |

# scheme_performance

| Column Name        | Data Type   | Business Definition   |
|:-------------------|:------------|:----------------------|
| amfi_code          | int64       |                       |
| scheme_name        | object      |                       |
| fund_house         | object      |                       |
| category           | object      |                       |
| plan               | object      |                       |
| return_1yr_pct     | float64     |                       |
| return_3yr_pct     | float64     |                       |
| return_5yr_pct     | float64     |                       |
| benchmark_3yr_pct  | float64     |                       |
| alpha              | float64     |                       |
| beta               | float64     |                       |
| sharpe_ratio       | float64     |                       |
| sortino_ratio      | float64     |                       |
| std_dev_ann_pct    | float64     |                       |
| max_drawdown_pct   | float64     |                       |
| aum_crore          | int64       |                       |
| expense_ratio_pct  | float64     |                       |
| morningstar_rating | int64       |                       |
| risk_grade         | object      |                       |

# portfolio_holdings

| Column Name       | Data Type   | Business Definition   |
|:------------------|:------------|:----------------------|
| amfi_code         | int64       |                       |
| stock_symbol      | object      |                       |
| stock_name        | object      |                       |
| sector            | object      |                       |
| weight_pct        | float64     |                       |
| market_value_cr   | float64     |                       |
| current_price_inr | float64     |                       |
| portfolio_date    | object      |                       |

# benchmark_indices

| Column Name   | Data Type   | Business Definition   |
|:--------------|:------------|:----------------------|
| date          | object      |                       |
| index_name    | object      |                       |
| close_value   | float64     |                       |

