import numpy as np

# Historical monthly returns (example data)
returns = np.array([0.01, -0.02, 0.03, 0.04, -0.01, 0.00, 0.02, -0.03, 0.01, 0.02, -0.01, 0.03])

# Calculate mean return
mean_return = np.mean(returns)

# Calculate standard deviation
std_dev = np.std(returns)

# Assuming a market return with a known beta of the stock
market_returns = np.array([0.01, 0.00, 0.02, 0.03, -0.01, 0.01, 0.02, -0.02, 0.01, 0.01, 0.00, 0.02])
covariance = np.cov(returns, market_returns)[0, 1]
market_variance = np.var(market_returns)

beta = covariance / market_variance

# Calculate VaR at 95% confidence level
z_score_95 = 1.65
VaR_95 = mean_return - z_score_95 * std_dev

# mean_return, std_dev, beta, VaR_95

print(mean_return, std_dev, beta, VaR_95)
