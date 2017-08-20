import email
from num2words import num2words
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
        content_type = b.get("content-type")
        if content_type is None or "text/plain" in content_type:
            props["body"] = p
        elif "text/html" in content_type:
            soup = BeautifulSoup(p)
            props["body"] = soup.get_text()
        elif "application/pgp-signature" in content_type:
            props["pgp"] = True
        else:
            print("Encountered strange content-type: " + content_type)
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
    import pdb
    text = text.replace("$", " dollars ")
    for num_start in range(len(text)):
        if text[num_start].isdigit():
            num_end = num_start
            while True:
                num_end += 1
                if not text[num_end].isdigit() or num_end > len(text):
                    break
            text = text.replace(text[num_start: num_end], " "+num2words(int(text[num_start: num_end])) + " ")
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
