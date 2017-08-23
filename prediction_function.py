from probability_tables import *
from math import log10
from features import *

#extras
from collections import Counter
import  os.path
import sys
eham,hham,spam,ehamCounter,hhamCounter,spamCounter=remove_big_words_from_list()
ham = eham
hamCounter = ehamCounter
counter = ehamCounter + spamCounter
def word_spam_probability(word):

    #TODO implement a better and faster search
    probability = 1.0 / (counter+1)
    for i in spam:
        if i[0]==word:
            if i[1]!= 0:
                probability=int(i[1])*1.0/spamCounter
                break;
    return probability

def word_ham_probability(word):
    # TODO implement a better and faster search
    #TODO check for improvements on using eham or hham or both
    probability = 1.0 / (counter+1)
    for i in ham:
        if i[0] == word and i[1] != 0:
                probability = int(i[1]) * 1.0 / hamCounter
                break;

    return probability


def classify_stemmed_text(txt):
    pham = 0    # on log scale
    pspam = 0   # on log scale
    for word in txt.split(" "):
        pspam -= log10(word_spam_probability(word))
        pham -= log10(word_ham_probability(word))
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
            total+=1
            file_name = os.path.join(root, file_obj)
            # open each file in directory and read them
            with open(file_name, errors="replace") as f:
                mail = f.read()
            parsed_email = email_parser(mail)
            body_txt = lemmatize_string(parsed_email["body"])
            if classify_stemmed_text(body_txt) == "SPAM":
                spam_mails+=1
            else:
                ham_mails+=1
    print("ham : "+ str(1.0*ham_mails/total))
    print("spam: " + str(1.0*spam_mails/total))
