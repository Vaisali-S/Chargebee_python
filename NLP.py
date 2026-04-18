'''
#NLP codes
#Tokenization
import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('punkt_tab')
text = "Hello, my dog is cute"
tokens = word_tokenize(text)
print(tokens)

#Stop words removal
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')
text = "This is a sample sentence, showing off the stop words filtration."
stop_words = set(stopwords.words('english'))
word_tokens = word_tokenize(text)
filtered_sentence = [w for w in word_tokens if not w.lower() in stop_words]
print("Original sentence:", text)
print("Filtered sentence:", " ".join(filtered_sentence))

#Stemming
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
words = ["running", "runner", "ran", "run", "easily", "fairly"]
stemmed_words = [stemmer.stem(word) for word in words]
print("Original words:", words)
print("Stemmed words:", stemmed_words)
#for word in words:
#    print(stemmer.stem(word))

#Lemmatization
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
nltk.download('wordnet')
lemmatizer = WordNetLemmatizer()
words = ["running", "runner", "ran", "run", "easily", "fairly"]
lemmatized_words = [lemmatizer.lemmatize(word, pos=wordnet.VERB) for word in words]
print("Original words:", words)
print("Lemmatized words:", lemmatized_words)
#for word in words:
#    print(lemmatizer.lemmatize(word))

#POS (Part-of-Speech) Tagging
import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('averaged_perceptron_tagger_eng')
text = "The quick brown fox jumps over the lazy dog."
tokens = word_tokenize(text)
pos_tags = pos_tag(tokens)
print("Original sentence:", text)
print("POS tags:", pos_tags)

#Syntax and Parsing
expression = "3 + 5 * ( 2 - 8 )"
result = eval(expression)
print("Expression:", expression)
print("Result:", result)

#Lowercasing
text = "Hello, World!"
lowercased_text = text.lower() 
print("Original text:", text)
print("Lowercased text:", lowercased_text)

#Remove special characters
import re
def remove_special_characters(text):
    return re.sub(r'[^A-Za-z0-9\s]', '', text)
text = "Hello, World! @2024 #NLP"
cleaned_text = remove_special_characters(text)
print("Original text:", text)
print("Cleaned text:", cleaned_text)

#Remove punctuation
import string
def remove_punctuation(text):
    return text.translate(str.maketrans('', '', string.punctuation))
text = "Hello, World! @2024 #NLP"
cleaned_text = remove_punctuation(text)
print("Original text:", text)
print("Cleaned text:", cleaned_text)

#Bag of Words
from sklearn.feature_extraction.text import CountVectorizer
docs = [
    "I love programming in Python",
    "Python is a great language",
    "I enjoy machine learning"
]
#Create the Bag of Words model
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(docs)
print("Feature names:", vectorizer.get_feature_names_out())
print("Bag of Words matrix:")
print(X.toarray())
'''
#N-grams
def generate_ngrams(text, n):
    tokens = text.split()
    return [tuple(tokens[i:i+n]) for i in range(len(tokens)-n+1)]
text = "I love programming in Python"
bigrams = generate_ngrams(text, 2)
trigrams = generate_ngrams(text, 3)
print("Original text:", text)
print("Bigrams:", bigrams)
print("Trigrams:", trigrams)