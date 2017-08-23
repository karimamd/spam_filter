import email
from num2words import num2words
import re
from bs4 import BeautifulSoup
from nltk import word_tokenize, pos_tag
from nltk.corpus import stopwords,wordnet
from nltk.stem import WordNetLemmatizer, PorterStemmer
stop = set(stopwords.words("english"))
def email_parser (email_text, overwrite_b=None):
    b = None
    props = {}
    if overwrite_b == None:
        b = email.message_from_string(email_text)
        props["subject"] = b.get("subject")
    else:
        b = overwrite_b
    p = b.get_payload()
        
    if b.is_multipart() == False:
        try:
            content_type = b.get("content-type").lower()
        except:
            content_type = None
        if content_type is None or "text/plain" in content_type:
            props["body"] = p
        elif "text/html" in content_type:
            soup = BeautifulSoup(p, "lxml")
            props["body"] = soup.get_text()
        elif "application/pgp-signature" in content_type or "application/x-pkcs7-signature" in content_type:
            props["sig"] = True
        elif "application" in content_type or "video" in content_type or "image" in content_type:
            props["attach"] = True
        return props
    for obj in p:
        obj_props = email_parser("", obj)
        if "body" in obj_props.keys():
            try:
                props["body"] += obj_props["body"]

            except:
                props["body"] = obj_props["body"]
            obj_props.pop("body")
        
        for key in obj_props.keys():
            props[key] = obj_props[key]
    return props

def morphy_to_wordnet(tag):
    if tag.startswith("N"):
        return wordnet.NOUN
    elif tag.startswith("J"):
        return wordnet.ADJ
    elif tag.startswith("V"):
        return wordnet.VERB
    elif tag.startswith("R"):
        return wordnet.ADV
    return wordnet.NOUN

def lemmatize_string (text):
    text = re.sub(r"([\w\.-]+@[\w\.-]+\b)", " repmail ", text)
    text = re.sub(r"((http|https|ftp)?:\/\/(\w|\.|\/|\?|\=|\&|\%)*)"," rpwbst ", text)
    text = re.sub(r"(\d+/\d+/\d+)", " repdate ", text)
    text = re.sub(r"(\d+:\d+:\d+)|(\d+:\d+)", " reptime ", text)
    text = re.sub(r"\d+.\d+.\d+", " repvrson ", text)
    text = re.sub(r"\$\S*\d", " dollars 1", text)
    text = re.sub(r"\d*.\d+", " repfrctn ", text)
    for num_start in range(len(text)):
        if text[num_start].isdigit():
            num_end = num_start
            while True:
                num_end += 1
                if num_end >= len(text) or not text[num_end].isdigit():
                    break
            try:
                text = text.replace(text[num_start: num_end], " "+num2words(int(text[num_start: num_end])) + " ")
            except:
                text = text.replace(text[num_start: num_end], " ")
    for i in range(10):
        text = text.replace(num2words(i), " ")
    lemmatized_list = []
    lemmatizer = WordNetLemmatizer()
    stemmer = PorterStemmer()
    text = ''.join(c if c.isalpha() else " " for c in text)
    tokens = text.split(" ")
    while "" in tokens:
        tokens.remove("")
    tags = pos_tag(tokens)
    for tag in tags:
        word = lemmatizer.lemmatize(tag[0], morphy_to_wordnet(tag[1])).lower()
        if word not in stop:
            lemmatized_list.append(stemmer.stem(word))
    return " ".join(lemmatized_list)
