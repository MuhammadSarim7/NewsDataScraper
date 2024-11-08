import pandas as pd


def filter_news_by_date(news_df, start_date, end_date):
    start_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date)
    filtered_news = news_df[
        (news_df['date'].notna()) & (news_df['date']
                                     >= start_date) & (news_df['date'] <= end_date)
    ]
    return filtered_news
