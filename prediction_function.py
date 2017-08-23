from probability_tables import *
from math import log10
from features import *

#extras
from collections import Counter
import  os.path
import sys
PSPAM = 0.8
PHAM = 1 - PSPAM
ham,spam,hamCounter,spamCounter=remove_big_words_from_list()
counter = hamCounter + spamCounter
def word_spam_probability(word):
    probability = spam[word] /spamCounter
    if probability == 0:
        probability = 1.0 / (counter+1)
    return probability

def word_ham_probability(word):
    probability = ham[word] * 1.0 / hamCounter
    if probability == 0:
        probability = 1.0 / (counter+1)
    return probability

def classify_stemmed_text(txt):
    pham =  log10(1-PHAM) - log10(PHAM)   # likely hood of ham on log scale
    pspam = log10(1-PSPAM) - log10(PSPAM)   # likely hood of spam log scale
    for word in txt.split(" "):
        wsp = word_spam_probability(word) # word spam probability
        pspam += log10(1-wsp) - log10(wsp)
        whp = word_ham_probability(word) # word ham probability
        pham += log10(1-whp) - log10(whp)
    if pham < pspam:
        return "HAM"
    else:
        return "SPAM"

'''
#sort eham,ham and spam to easily find what we are looking for
eham.sort()
hham.sort()
spam.sort()

'''
if __name__ == '__main__':
    directory = input("Directory: ")
    spam_mails=0
    ham_mails=0
    total=0
    for root, _, files in os.walk(directory):
        for file_obj in files:
            sys.stdout.write(".")
            sys.stdout.flush()
            file_name = os.path.join(root, file_obj)
            # open each file in directory and read them
            with open(file_name, errors="replace") as f:
                mail = f.read()
            parsed_email = email_parser(mail)
            if "body" not in parsed_email.keys():
                continue
            body_txt = lemmatize_string(parsed_email["body"])
            total += 1
            if classify_stemmed_text(body_txt) == "SPAM":
                spam_mails+=1
            else:
                ham_mails+=1
    print("\nham : "+ str(ham_mails))
    print("spam: " + str(spam_mails))
    print("total: " + str(total))
