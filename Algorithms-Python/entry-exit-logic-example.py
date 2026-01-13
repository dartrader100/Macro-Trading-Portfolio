# Basic entry/exit logic for regime-confirmed trends
# Enters on pullback in bullish regime, exits on regime break

def entry_signal(current_price, range_low, range_high, regime):
    if regime == "Bullish" and current_price <= range_low * 1.05:  # Near lower band
        return "Enter Long — High-conviction pullback"
    return "No Signal"

def exit_signal(regime):
    if regime == "Neutral" or regime == "Bearish":
        return "Exit Position — Regime break"
    return "Hold"

# Example
regime = "Bullish"
price = 100
low = 95
high = 110
print(entry_signal(price, low, high, regime))
print(exit_signal("Neutral"))
