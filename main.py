from excel_handler import read_stock_file, create_output_report
from stock_fetcher import get_stock_data
from sentiment_analyzer import analyze_sentiment
from news_analyzer import analyze_news
from recommendation_engine import generate_recommendation
from email_sender import send_email_report


file_path = "input/INPUT_STOCKS.xlsx"

stocks = read_stock_file(file_path)

report_data = []

print("\nAI STOCK ANALYSIS REPORT\n")


for stock in stocks:

    stock_result = get_stock_data(stock)

    if stock_result:

        social_sentiment = analyze_sentiment(stock)

        news_sentiment = analyze_news(stock)

        recommendation = generate_recommendation(
            stock_result["movement"],
            social_sentiment,
            news_sentiment
        )

        # STORE DATA FOR EXCEL REPORT

        report_data.append({

            "Stock Name": stock,

            "Social Media Sentiment": social_sentiment,

            "News": news_sentiment,

            "Company Info": stock_result["movement"],

            "Final Recommendation": recommendation
        })

        print(f"""
==================================================

Stock: {stock_result['stock']}

Stock Movement: {stock_result['movement']}

Social Media Sentiment: {social_sentiment}

News Sentiment: {news_sentiment}

FINAL RECOMMENDATION:
{recommendation}

==================================================
""")

# CREATE OUTPUT EXCEL

output_file = create_output_report(report_data)

print(f"\nOutput File Saved At: {output_file}")
 
 # SEND EMAIL

if output_file:

    send_email_report(output_file)