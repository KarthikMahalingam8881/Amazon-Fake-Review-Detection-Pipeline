import re
from textblob import TextBlob
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Assumes nltk data is pre-downloaded into your Docker image
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def clean_text_column(df, text_column='text', new_column='clean_text'):
    """
    Clean and lemmatize text column in DataFrame.
    """
    def clean(text):
        text = re.sub(r'[^a-zA-Z0-9\s]', '', str(text).lower())
        tokens = [lemmatizer.lemmatize(w) for w in text.split() if w not in stop_words]
        return " ".join(tokens)

    df[new_column] = df[text_column].apply(clean)
    return df

def apply_sentiment(df, text_column='text', new_column='sentiment'):
    """
    Apply sentiment analysis using TextBlob.
    """
    df[new_column] = df[text_column].astype(str).apply(lambda x: TextBlob(x).sentiment.polarity)
    return df

