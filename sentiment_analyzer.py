from textblob import TextBlob


def analyze_sentiment(stock_name):

    # MOCK SOCIAL MEDIA DATA

    mock_posts = {

        "TSLA": [
            "Tesla stock is growing rapidly",
            "Investors are happy with Tesla",
            "Tesla future looks strong"
        ],

        "AAPL": [
            "Apple products are amazing",
            "Apple stock looks stable",
            "Strong iPhone sales expected"
        ],

        "MSFT": [
            "Microsoft cloud business is expanding",
            "Positive growth for Microsoft",
            "Microsoft AI investments are impressive"
        ],

        "AMZN": [
            "Amazon facing delivery issues",
            "Some investors worried about Amazon",
            "Amazon growth slowing down"
        ]
    }

    posts = mock_posts.get(stock_name, [])

    if not posts:
        return "Neutral"

    total_score = 0

    for post in posts:

        analysis = TextBlob(post)

        total_score += analysis.sentiment.polarity

    average_score = total_score / len(posts)

    if average_score > 0:
        return "Positive"

    elif average_score < 0:
        return "Negative"

    else:
        return "Neutral"