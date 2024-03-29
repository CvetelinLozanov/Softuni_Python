import requests
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

CURRENT_DAY = datetime.today().strftime('%Y-%m-%d')
TEN_DAYS_BEFORE = (datetime.today() - timedelta(days=10)).strftime('%Y-%m-%d')


# Function to fetch crypto data from Alpha Vantage API
def fetch_crypto_data(api_key, symbol, market):
    url = f'https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&symbol={symbol}&market={market}&apikey={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if 'Time Series (Digital Currency Daily)' in data:
            return data['Time Series (Digital Currency Daily)']
        else:
            print("Error: Data not available for the provided symbol.")
            return None
    else:
        print("Error: Failed to fetch data from Alpha Vantage API.")
        return None


# Function to process stock market data into a Pandas DataFrame
def process_crypto_data(json_data):
    df = pd.DataFrame(json_data).T
    df.index = pd.to_datetime(df.index)
    df = df.loc[TEN_DAYS_BEFORE:]  # takes the information only for the last 10 days
    df = df.astype(float)
    df.columns = ['open_bgn', 'open_usd', 'high_bgn', 'high_usd', 'low_bgn', 'low_usd', 'close_bgn', 'close_usd',
                  'volume', 'market_cap']
    return df


# Function to visualize crypto price over time
def visualize_crypto_prices(dataframe, symbol: str):
    plt.figure(figsize=(10, 6), facecolor='white')
    plt.plot(dataframe.index, dataframe['close_bgn'], color='blue', label='BGN')
    plt.plot(dataframe.index, dataframe['close_usd'], color='green', label='USD')
    plt.title(f'{symbol} currency price')
    plt.xlabel('Date')
    plt.ylabel('Closing Price')
    plt.legend(loc="upper left")
    plt.grid(True)
    plt.show()


# # Function to calculate daily returns
# def calculate_daily_returns(dataframe):
#     dataframe['daily_return'] = dataframe['close'].pct_change() * 100
#     return dataframe
#
#
# # Function to visualize daily returns distribution
# def visualize_daily_returns(dataframe):
#     plt.figure(figsize=(10, 6))
#     plt.hist(dataframe['daily_return'].dropna(), bins=30, color='green', alpha=0.7)
#     plt.title('Daily Returns Distribution')
#     plt.xlabel('Daily Returns (%)')
#     plt.ylabel('Frequency')
#     plt.grid(True)
#     plt.show()
#
#
# # Function to calculate rolling statistics
# def calculate_rolling_statistics(dataframe, window_size):
#     rolling_mean = dataframe['close'].rolling(window=window_size).mean()
#     rolling_std = dataframe['close'].rolling(window=window_size).std()
#     return rolling_mean, rolling_std
#
#
# # Function to visualize rolling statistics
# def visualize_rolling_statistics(dataframe, rolling_mean, rolling_std):
#     plt.figure(figsize=(10, 6))
#     plt.plot(dataframe.index, dataframe['close'], label='Closing Price', color='blue')
#     plt.plot(dataframe.index, rolling_mean, label='Rolling Mean', color='red')
#     plt.plot(dataframe.index, rolling_std, label='Rolling Std', color='green')
#     plt.title('Rolling Statistics')
#     plt.xlabel('Date')
#     plt.ylabel('Price')
#     plt.legend()
#     plt.grid(True)
#     plt.show()
#
#
# # Function to fetch company information from Alpha Vantage API
# def fetch_company_info(api_key, symbol):
#     url = f"https://www.alphavantage.co/query?function=OVERVIEW&symbol={symbol}&apikey={api_key}"
#     response = requests.get(url)
#     if response.status_code == 200:
#         data = response.json()
#         return data
#     else:
#         print("Error: Failed to fetch company information from Alpha Vantage API.")
#         return None


# Main function to orchestrate the execution of all tasks
def main():
    api_key = "YOUR_ALPHA_VANTAGE_API_KEY"
    symbol = "XMR"  # Example symbol (BTC)
    market = "BGN"

    # Fetching stock data
    stock_data = fetch_crypto_data(api_key, symbol, market)
    if stock_data:
        # Processing data into DataFrame
        df = process_crypto_data(stock_data)

        # Visualizing crypto price over time
        visualize_crypto_prices(df, symbol)

        # Calculating daily returns
        # df = calculate_daily_returns(df)
        #
        # # Visualizing daily returns distribution
        # visualize_daily_returns(df)
        #
        # # Calculating rolling statistics
        # rolling_mean, rolling_std = calculate_rolling_statistics(df, window_size=20)
        #
        # # Visualizing rolling statistics
        # visualize_rolling_statistics(df, rolling_mean, rolling_std)
        #
        # # Fetching company information
        # company_info = fetch_company_info(api_key, symbol)
        #
        # if company_info:
        #     print("\nCompany Information:")
        #     print('Name:', company_info.get('Name', 'N/A'))
        #     print('Sector:', company_info.get('Sector', 'N/A'))
        #     print('Country:', company_info.get('Country', 'N/A'))


if __name__ == "__main__":
    main()
