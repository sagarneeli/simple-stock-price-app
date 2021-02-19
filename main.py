"""
## SIMPLE STOCK PRICE

DESCRIPTION - A simple app that displays stock **closing price** and ***volume*** of a given company

Author: [Sagar Neeli](https://www.sagarneeli.com)\n
Source: [Github](https://github.com/sagarneeli/simple-stock-price)
"""
import yfinance as yf
import streamlit as st


def run():
    ticker_symbol = st.text_input('Enter Ticker Symbol : Eg GOOGL', value='', max_chars=None, key=None, type='default')
    st.write('(*Checkout this website for reference: - https://finance.yahoo.com/lookup/)*')
    st.write('Provide date range')
    start_data = st.text_input(
        'Start Date : (format YYYY-MM-DD))',
        value='2010-5-31',
        max_chars=None,
        key=None,
        type='default'
    )
    end_data = st.text_input(
        'End Date : (format YYYY-MM-DD))',
        value='2020-5-31',
        max_chars=None,
        key=None,
        type='default'
    )

    if ticker_symbol:
        ticker_data = yf.Ticker(ticker_symbol)
        # Get the historical prices for this ticker
        ticker_df = ticker_data.history(period='1d', start=start_data, end=end_data)

        st.write("""
        ## Closing Price
        """)
        st.line_chart(ticker_df.Close)
        st.write("""
        ## Volume Price
        """)
        st.line_chart(ticker_df.Volume)


def main():
    st.title('Simple Stock Price App')
    st.markdown('Find out what the stock **closing price** and ***volume*** of a given company!')
    run()


if __name__ == "__main__":
    main()
