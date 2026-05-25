import pandas as pd

from datetime import datetime


def read_stock_file(file_path):

    try:
        df = pd.read_excel(file_path)

        stocks = df["Stock Name"].dropna().tolist()

        return stocks

    except Exception as e:
        print(f"Error reading Excel file: {e}")

        return []


def create_output_report(report_data):

    try:

        output_df = pd.DataFrame(report_data)

        timestamp = datetime.now().strftime("%d%m%Y%H%M%S")

        filename = f"OUTPUT_REPORT_{timestamp}.xlsx"

        output_path = f"output/{filename}"

        output_df.to_excel(output_path, index=False)

        print(f"\nReport Generated Successfully: {filename}")

        return output_path

    except Exception as e:

        print(f"Error creating output report: {e}")

        return None
    