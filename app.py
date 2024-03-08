import streamlit as st
from fetch_tweet import extract_tweet_text
from find_sentimate import find_sentimate


st.title('Tweet Sentiment Analysis')

st.write("This is a tweet sentiment analysis tool that will help you understand the sentiment of the tweet. Simply enter the tweet URL and click on the button below to get the sentiment of the tweet.")

tweet_url = st.text_input('Enter the tweet url')

analyze = st.button('Analyze',type='primary')

tweet_text = extract_tweet_text(tweet_url)


if analyze:

    st.write("Tweet : \n")
    text_content = tweet_text

    styled_text = f"<div style='border: 1px solid white; padding: 5px;border-radius:5px;'>{text_content}</div>"

    st.markdown(styled_text, unsafe_allow_html=True)

    preds = find_sentimate(tweet_text)
    if preds == 0:
        st.write("The sentiment of the tweet is negative")
    else:
        st.write("The sentiment of the tweet is positive")


