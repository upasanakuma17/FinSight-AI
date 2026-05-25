def generate_recommendation(
        stock_movement,
        social_sentiment,
        news_sentiment
):

    positive_count = 0
    negative_count = 0

    # STOCK MOVEMENT

    if stock_movement == "Positive":
        positive_count += 1

    elif stock_movement == "Negative":
        negative_count += 1

    # SOCIAL SENTIMENT

    if social_sentiment == "Positive":
        positive_count += 1

    elif social_sentiment == "Negative":
        negative_count += 1

    # NEWS SENTIMENT

    if news_sentiment == "Positive":
        positive_count += 1

    elif news_sentiment == "Negative":
        negative_count += 1

    # FINAL DECISION

    if positive_count >= 2:
        return "Bullish Trend"

    elif negative_count >= 2:
        return "Bearish Trend"

    else:
        return "Hold / Neutral"