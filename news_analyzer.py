from textblob import TextBlob


def analyze_news(stock_name):

    # MOCK COMPANY NEWS

    mock_news = {

        "TSLA": [
            "Tesla announces record vehicle deliveries",
            "Tesla stock gains after strong earnings",
            "Investors optimistic about Tesla AI plans"
        ],

        "AAPL": [
            "Apple reports strong iPhone sales",
            "Apple expands AI features globally",
            "Apple market performance remains stable"
        ],

        "MSFT": [
            "Microsoft cloud revenue increases significantly",
            "Microsoft AI partnership boosts confidence",
            "Positive outlook for Microsoft shares"
        ],

        "AMZN": [
            "Amazon faces regulatory pressure",
            "Concerns over Amazon slowing growth",
            "Amazon stock under analyst watch"
        ]
    }

    news_list = mock_news.get(stock_name, [])

    if not news_list:
        return "Neutral"

    total_score = 0

    for news in news_list:

        analysis = TextBlob(news)

        total_score += analysis.sentiment.polarity

    average_score = total_score / len(news_list)

    if average_score > 0:
        return "Positive"

    elif average_score < 0:
        return "Negative"

    else:
        return "Neutral"