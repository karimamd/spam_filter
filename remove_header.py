import email
from nltk import word_tokenize
from nltk.corpus import stopwords
stop = set(stopwords.word("english")
def feature_extraction (email_text):
    b = email.message_from_text(email_text)
    return b.payload()
    
