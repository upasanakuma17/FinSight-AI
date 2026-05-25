import yfinance as yf


def get_stock_data(stock_name):

    try:
        stock = yf.Ticker(stock_name)

        data = stock.history(period="2d")

        if data.empty:
            return None

        latest_close = data["Close"].iloc[-1]
        previous_close = data["Close"].iloc[-2]

        change = latest_close - previous_close

        percent_change = (change / previous_close) * 100

        movement = "Neutral"

        if percent_change > 1:
            movement = "Positive"

        elif percent_change < -1:
            movement = "Negative"

        return {
            "stock": stock_name,
            "current_price": round(latest_close, 2),
            "previous_close": round(previous_close, 2),
            "change_percent": round(percent_change, 2),
            "movement": movement
        }

    except Exception as e:
        print(f"Error fetching stock data for {stock_name}: {e}")

        return None