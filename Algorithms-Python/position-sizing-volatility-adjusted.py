# Volatility-adjusted position sizing to protect capital
# Caps risk per trade and adjusts for asset volatility

def calculate_position_size(account_value, volatility, max_risk_percent=0.01, max_position_percent=0.12):
    risk_amount = account_value * max_risk_percent  # Risk 1% of account per trade
    raw_size = risk_amount / volatility
    capped_size = min(raw_size, account_value * max_position_percent)  # e.g., max 12% for high-conviction
    return capped_size

# Example usage
account = 100000
vol = 0.015  # 1.5% daily volatility
print(f"Recommended position size: €{calculate_position_size(account, vol):,.2f}")
