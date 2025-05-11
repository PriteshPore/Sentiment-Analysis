import streamlit as st
from transformers import pipeline


def load_sentiment_model():
    # Load pre-trained sentiment analysis model from Hugging Face
    return pipeline("sentiment-analysis")

def main():
        st.title("Real-Time Sentiment Analysis")
        st.markdown("""
                    This app performs real-time sentiment analysis on the input text.
                    Simply type or paste your text in the box below to anlayse the sentiment!""")
        
        # Load the sentiment analysis model
        sentiment_analyser = load_sentiment_model()

        # Input Text
        user_input = st.text_area("Enter your text here:",height=200)
        if st.button("Analyse Sentiment") and user_input:
              # Perform sentiment analysis
              result = sentiment_analyser(user_input)

              # Display the result
              sentiment = result[0]['label']
              score = result[0]['score']
              st.markdown(f"**Sentiment:** {sentiment}")
              st.markdown(f"**Score:** {score}")
            
if __name__ =="__main__":
      main()
