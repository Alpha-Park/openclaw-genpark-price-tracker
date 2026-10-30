"""E-Commerce Price Tracker & Delta Monitor.
100% Python Standard Library.
"""

class PriceTrackerEngine:
    """Tracks historical price points, identifies all-time-lows, and generates discount alert metrics."""

    @staticmethod
    def evaluate_price_drop(sku: str, current_price: float, historical_prices: list, target_discount_pct: float = 15.0) -> dict:
        if not historical_prices:
            return {"sku": sku, "status": "INSUFFICIENT_HISTORY", "current_price": current_price}

        avg_price = sum(historical_prices) / len(historical_prices)
        min_price = min(historical_prices)
        max_price = max(historical_prices)
        discount_from_avg = ((avg_price - current_price) / avg_price) * 100.0

        is_all_time_low = current_price <= min_price
        alert_triggered = discount_from_avg >= target_discount_pct or is_all_time_low

        return {
            "sku": sku,
            "current_price": round(current_price, 2),
            "historical_min": round(min_price, 2),
            "historical_avg": round(avg_price, 2),
            "discount_from_avg_pct": round(discount_from_avg, 2),
            "is_all_time_low": is_all_time_low,
            "alert_triggered": alert_triggered,
            "recommendation": "BUY_NOW_BARGAIN" if alert_triggered else "WAIT_FOR_PROMO"
        }
