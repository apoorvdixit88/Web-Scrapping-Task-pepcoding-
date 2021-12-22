import nltk 
import urllib
import bs4 as bs
import re
from nltk.corpus import stopwords
nltk.download('stopwords')
nltk.download('punkt')

source =urllib.request.urlopen('https://en.wikipedia.org/wiki/A#Other_uses')

soup =bs.BeautifulSoup(source,'lxml')
text=""
for para in soup.find_all('p'):
    text+=para.text

text=re.sub(r'\[[0-9]*\]',' ',text)
text=re.sub(r'\s+',' ',text)
text=text.lower();
text=re.sub(r'\d',' ',text)
text=re.sub(r'\s+',' ',text)

sentences=nltk.sent_tokenize(text)
sentences=[nltk.word_tokenize(sentence) for sentence in sentences]
print(sentences)
# listToStr = ' '.join([str(elem) for elem in sentences])
# f=open("histo.txt","w")
# f.write(listToStr.encode("utf-8"))
# f.close()
# # print(sentences)