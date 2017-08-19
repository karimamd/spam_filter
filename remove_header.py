import email
import nltk
def feature_extraction (email_text):
    b = email.message_from_text(email_text)
    return b.payload()
    
