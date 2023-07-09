Sure! Here's an example code using the Natural Language Toolkit (NLTK) library in Python to perform sentiment analysis:

```python
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Download the required NLTK resources (only needed for the first time)
nltk.download('vader_lexicon')

def sentiment_analysis(text):
    # Create a new SentimentIntensityAnalyzer
    sid = SentimentIntensityAnalyzer()
    
    # Analyze the sentiment of the text
    sentiment_scores = sid.polarity_scores(text)
    
    # Determine the sentiment label based on the compound score
    if sentiment_scores['compound'] >= 0.05:
        sentiment = 'Positive'
    elif sentiment_scores['compound'] <= -0.05:
        sentiment = 'Negative'
    else:
        sentiment = 'Neutral'
    
    return sentiment

# Example usage
text = "I love this product! It's amazing!"
sentiment = sentiment_analysis(text)
print("Sentiment:", sentiment)
```

In this code, we first import the necessary libraries, NLTK and the `SentimentIntensityAnalyzer` class from the `nltk.sentiment` module. We then create a function `sentiment_analysis()` that takes in a text as input.

Inside the function, we create a new instance of the `SentimentIntensityAnalyzer` class. We then use this object to analyze the sentiment of the given text using the `polarity_scores()` function, which returns a dictionary of sentiment scores.

Based on the compound score (which represents the overall sentiment), we determine the sentiment label as positive, negative, or neutral. Finally, the function returns the sentiment label.

In the example usage, we provide a sample text and pass it to the `sentiment_analysis()` function. The sentiment label is then printed to the console.