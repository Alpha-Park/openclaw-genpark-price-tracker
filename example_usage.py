from client import PriceTrackerEngine

if __name__ == "__main__":
    res = PriceTrackerEngine.evaluate_price_drop("SKU-9920", 149.99, [199.99, 189.99, 179.99])
    print("Price Evaluation:", res)
