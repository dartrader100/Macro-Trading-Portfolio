# Simple inflation regime detection using public indicators (e.g., CPI proxy)
# Classifies "high" vs "low" inflation to guide asset rotation

def detect_regime(cpi_yoy, threshold_high=3.0, threshold_low=1.0):
    if cpi_yoy > threshold_high:
        return "High Inflation Regime — Favor Commodities & Metals"
    elif cpi_yoy < threshold_low:
        return "Low Inflation Regime — Favor Equities & Growth Assets"
    else:
        return "Neutral Regime — Balanced Allocation"

# Example usage with mock data
cpi_data = [4.2, 2.8, 1.5, 3.5]  # Year-over-year CPI %
for value in cpi_data:
    print(f"CPI {value}% → {detect_regime(value)}")
