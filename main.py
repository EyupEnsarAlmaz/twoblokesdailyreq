from services.stock_service import StockAPI
from services.currency_service import fetch_currency_data
from datetime import datetime



def main():
    # Configuration
    API_KEY = ""
    SYMBOLS = ["TSLA", "GOOG", "META", "AAPL", "AMZN", 
              "NFLX", "IBM", "MSFT", "NVDA", "AMD"]

    # Get stock data and update Excel
    api = StockAPI(API_KEY)
    print(f"\nStock Data for {api.get_formatted_date()}")
    print("=" * 50)
    
    stocks = api.get_stock_quotes(SYMBOLS)
    if stocks:
        for stock in stocks:
            print(stock)
        api.update_excel(stocks)

if __name__ == "__main__":
    main()    
    fetch_currency_data()
   
