from probability_tables import *
from math import log10
from features import *

#extras
from collections import Counter
import  os.path
import sys

def word_spam_probability(word,spamCounter):

    #TODO implement a better and faster search
    for i in spam:
        if i[0]==word:
            if i[1]!= 0:
                probability=int(i[1])*1.0/spamCounter
                #print(i[0]+" spam "+str(abs(log10(probability))))
            else:
                probability=1.0/(spamCounter+1)
        else:
            probability = 1.0 / (spamCounter+1)

    return probability

def word_ham_probability(word,ehamCounter,hhamCounter):
    # TODO implement a better and faster search
    #TODO check for improvements on using eham or hham or both
    hamCounter=ehamCounter+hhamCounter
    ham=eham+hham
    for i in ham:
        if i[0] == word:
            if i[1] != 0:
                probability = int(i[1]) * 1.0 / hamCounter
            else:
                probability = 1.0 / (hamCounter+1)
        else:
            probability = 1.0 / (hamCounter+1)

    return probability


eham,hham,spam,ehamCounter,hhamCounter,spamCounter=remove_big_words_from_list()
'''
#sort eham,ham and spam to easily find what we are looking for
eham.sort()
hham.sort()
spam.sort()

'''

probability_spam=1
probability_ham=1
#mail_words is list of stemmed words in fount in the input mail
#TODO choose proper input method for email , a file for example
mail="mail hundr free"


parsed_email=email_parser(mail)
body_dictionary=lemmatize_string(parsed_email["body"])
mail_words=body_dictionary.split(" ")
print(mail_words)


for each_word in mail_words:
    probability_spam*=word_spam_probability(each_word,spamCounter)
    probability_ham*=word_ham_probability(each_word,ehamCounter,hhamCounter)
#we use less than for spam because we take log so the one with the lowest power will be the smallest
if abs(log10(probability_spam)) < abs(log10(probability_ham)):
    print("spam mail")
else:
    print ("non-spam mail")


#test
#user input directory name containing files of testing (mails)
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
        body_dictionary = lemmatize_string(parsed_email["body"])
        mail_words = body_dictionary.split(" ")
        probability_spam = 1
        probability_ham = 1
        for each_word in mail_words:
            probability_spam *= word_spam_probability(each_word, spamCounter)
            probability_ham *= word_ham_probability(each_word, ehamCounter, hhamCounter)
        # we use less than for spam because we take log so the one with the lowest power will be the smallest
        if probability_spam < probability_ham:
            spam_mails+=1
        else:
            ham_mails+=1

print("ham : "+ str(1.0*ham_mails/total))
print("spam: " + str(1.0*spam_mails/total))
