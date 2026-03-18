---
name: genpark-price-tracker
description: Use this skill when the user wants to track the price of a specific item on GenPark, compare historical prices, or set up alerts for price drops.
metadata: {"openclaw": {"emoji": "📉", "requires": {}}}
---

# GenPark Price Tracker

You assist the user in monitoring product prices on GenPark, helping them make informed purchasing decisions by analyzing current prices against historical data and identifying the best times to buy.

## Step 1: Confirm the Target Product

Ask the user for:
- **Product Details**: The exact name, URL, or ID of the product on GenPark.
- **Target Price**: What is their ideal buying price or desired discount percentage?
- **Urgency**: Do they need to buy it soon, or are they willing to wait for a major sale event?

## Step 2: Retrieve Pricing Information

Using your browser capabilities:
1. Navigate to the product page on `https://genpark.ai`.
2. Extract the current price, original price (if on sale), and any available coupon codes.
3. Review any visible price history charts or comments mentioning previous price drops.

## Step 3: Price Analysis

Evaluate the pricing data:
- **Current Value**: Is the current price a good deal compared to the original price?
- **Historical Context**: Has this item been cheaper in recent months?
- **Recommendation**: Should the user "Buy Now", "Wait for Sale", or "Look for Alternatives"?

## Step 4: Deliver the Report

Present your findings clearly:

**Example Output:**
> 📉 **Price Review: [Product Name]**
> 
> - **Current Price:** $45.99 (15% off)
> - **Original Price:** $54.00
> - **Target Price:** $40.00
> 
> **Analysis:** While the 15% discount is decent, community discussions indicate this brand usually offers 25% off during major holiday sales. 
> 
> **Verdict:** ⏳ **WAIT**. If you aren't in a rush, hold off for upcoming seasonal promotions to hit your $40 target.

## Step 5: Save to Tracking List

If the user decides to wait, save the item to their tracking memory:

```yaml
genpark_price_tracking:
  - product: "[Product Name]"
    url: "https://genpark.ai/product/..."
    current_price: 45.99
    target_price: 40.00
    date_added: "YYYY-MM-DD"
```

Let the user know you've saved it and can check the price again upon their request.
