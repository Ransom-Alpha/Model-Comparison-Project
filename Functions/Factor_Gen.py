import pandas as pd
import numpy as np
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def compute_ohlc_average(open_prices, high_prices, low_prices, close_prices):
    return (open_prices + high_prices + low_prices + close_prices) / 4

def compute_log_returns(monthly_close):
    return np.log(monthly_close / monthly_close.shift(1))

def compute_rolling_beta(log_returns, market_col="^GSPC", window_size=60):
    market_returns = log_returns[market_col]
    rolling_betas = pd.DataFrame(index=log_returns.index)
    for stock in log_returns.columns:
        if stock != market_col:
            rolling_betas[stock] = (
                log_returns[stock].rolling(window=window_size).cov(market_returns)
                / market_returns.rolling(window=window_size).var()
            )
    return rolling_betas.dropna()

def compute_smb(returns, market_caps, size_threshold=50):
    size_cutoff = market_caps.quantile(size_threshold / 100, axis=1)
    small_firms = returns[market_caps.le(size_cutoff, axis=0)]
    big_firms = returns[market_caps.gt(size_cutoff, axis=0)]
    return small_firms.mean(axis=1) - big_firms.mean(axis=1)

def compute_hml(returns, book_to_market, value_threshold=50):
    value_cutoff = book_to_market.quantile(value_threshold / 100, axis=1)
    value_stocks = returns[book_to_market.ge(value_cutoff, axis=0)]
    growth_stocks = returns[book_to_market.lt(value_cutoff, axis=0)]
    return value_stocks.mean(axis=1) - growth_stocks.mean(axis=1)

def compute_umd(returns, momentum_window=12, momentum_threshold=30):
    past_returns = returns.shift(1).rolling(momentum_window).sum()
    top_cutoff = past_returns.quantile((100 - momentum_threshold) / 100, axis=1)
    bottom_cutoff = past_returns.quantile(momentum_threshold / 100, axis=1)
    winners = returns[past_returns.ge(top_cutoff, axis=0)]
    losers = returns[past_returns.le(bottom_cutoff, axis=0)]
    return winners.mean(axis=1) - losers.mean(axis=1)

def compute_rmw(returns, roe, profitability_threshold=50):
    profit_cutoff = roe.quantile(profitability_threshold / 100, axis=1)
    robust = returns[roe.ge(profit_cutoff, axis=0)]
    weak = returns[roe.lt(profit_cutoff, axis=0)]
    return robust.mean(axis=1) - weak.mean(axis=1)

def compute_cma(returns, asset_growth, investment_threshold=50):
    investment_cutoff = asset_growth.quantile(investment_threshold / 100, axis=1)
    conservative = returns[asset_growth.le(investment_cutoff, axis=0)]
    aggressive = returns[asset_growth.gt(investment_cutoff, axis=0)]
    return conservative.mean(axis=1) - aggressive.mean(axis=1)

def compute_liq(returns, traded_volume, market_impact, liquidity_threshold=50):
    liquidity_measure = traded_volume * market_impact
    liquidity_cutoff = liquidity_measure.quantile(liquidity_threshold / 100, axis=1)
    illiquid = returns[liquidity_measure.le(liquidity_cutoff, axis=0)]
    liquid = returns[liquidity_measure.gt(liquidity_cutoff, axis=0)]
    return illiquid.mean(axis=1) - liquid.mean(axis=1)

def compute_q_roe(returns, roe, roe_threshold=50):
    roe_cutoff = roe.quantile(roe_threshold / 100, axis=1)
    high_roe = returns[roe.ge(roe_cutoff, axis=0)]
    low_roe = returns[roe.lt(roe_cutoff, axis=0)]
    return high_roe.mean(axis=1) - low_roe.mean(axis=1)

def load_csv(file_path):
    return pd.read_csv(file_path, index_col="Date", parse_dates=True)

def save_csv(data, file_path):
    data.to_csv(file_path)

def main():
    logging.info("Loading data...")
    monthly_close = load_csv("monthly_closing_prices_fixed.csv")
    logging.info("Computing log returns...")
    log_returns = compute_log_returns(monthly_close)
    save_csv(log_returns, "monthly_log_returns.csv")
    logging.info("Computing rolling betas...")
    rolling_betas = compute_rolling_beta(log_returns)
    save_csv(rolling_betas, "rolling_beta_5yr.csv")
    logging.info("Completed all computations.")

if __name__ == "__main__":
    main()
