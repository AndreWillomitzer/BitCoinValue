# BitCoinValue
This is a tiny script I wrote to grab the value of Bitcoin for each week of every month. It fetches from Alpha Vantage API using the Requests library and writes the data into Rows/Columns using Pandas.

Eventually I intend to make it grab all of the crypto currency values instead of just BitCoin. I work on it when I can :D

## How to use
- To use the script you must sign up for free with Alpha Vantage to obtain an API key.
- Substitute the ${apiKey} placeholder with your key.
- Install Python 3.
- Make sure to install all dependencies such as Pandas and Request library.
- type *python 3 cryptoPrice_Script* from the terminal/CLI.

## If you want a different currency
- Edit the script, and replace "BTC" in the URL with the alternate currency for example Ethereum.
- Optional: You can rename the spreadsheet as well.
