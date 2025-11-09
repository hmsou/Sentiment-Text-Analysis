from textblob import TextBlob
from newspaper import Article
# import nltk
# nltk.download('punkt_tab')

# url = "https://en.wikipedia.org/wiki/Neural_network_(machine_learning)"
# article = Article(url)
# article.download()
# article.parse()
# article.nlp()
# text = article.summary
# print(text)

with open('NegativeReview.txt', 'r') as f:
    text = f.read()

blob = TextBlob(text)
sentiment = blob.sentiment # polarity -1 to 1
print(sentiment)