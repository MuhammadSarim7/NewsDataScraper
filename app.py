import streamlit as st
import pandas as pd
from news_scraper import fetch_news
from utils import filter_news_by_date

st.title("News Dashboard")
st.header("Latest News")

news_data = fetch_news()

news_df = pd.DataFrame(news_data)

start_date = st.date_input("Start Date")
end_date = st.date_input("End Date")

filtered_news = filter_news_by_date(news_df, start_date, end_date)

st.dataframe(filtered_news)
