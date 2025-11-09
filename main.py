from textblob import TextBlob
from newspaper import Article
import nltk
nltk.download('punkt_tab')

url = "https://en.wikipedia.org/wiki/Neural_network_(machine_learning)"
article = Article(url)
# url2 = "https://g1.globo.com/jornal-nacional/noticia/2025/11/08/moradores-relatam-desespero-apos-tornado-destruir-cidade-no-interior-do-parana.ghtml"
# article2 = Article(url2)

article.download()
article.parse()
article.nlp()

text = article.text
print(text)