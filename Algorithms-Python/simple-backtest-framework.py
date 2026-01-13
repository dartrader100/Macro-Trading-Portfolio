# Simple backtest to simulate regime-adjusted returns
# Mock data — anonymized example

import numpy as np
import matplotlib.pyplot as plt

# Mock daily returns in different regimes
high_inflation_returns = np.random.normal(0.0015, 0.02, 252)  # Commodities favor
low_inflation_returns = np.random.normal(0.001, 0.015, 252)   # Equities favor

# Combine for year
returns = np.concatenate([high_inflation_returns, low_inflation_returns])
equity_curve = np.cumprod(1 + returns)

plt.plot(equity_curve)
plt.title("Example Equity Curve — Regime-Adjusted Strategy")
plt.xlabel("Days")
plt.ylabel("Portfolio Value")
plt.show()
