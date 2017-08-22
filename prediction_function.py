from probability_tables import *
from features import *
def word_spam_probability(word,spamCounter):

    #TODO implement a better and faster search
    for i in spam:
        if i[0]==word:
            if i[1]!= 0:
                probability=int(i[1])*1.0/spamCounter
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
mail="my naming is kareem name,far"


parsed_email=email_parser(mail)
body_dictionary=lemmatize_string(parsed_email["body"])
mail_words=body_dictionary.split(" ")
print(mail_words)

for i in spam:
    if i[0]=="dog":
        print("found")
        print(i)

for each_word in mail_words:
    probability_spam*=word_spam_probability(each_word,spamCounter)
    probability_ham*=word_ham_probability(each_word,ehamCounter,hhamCounter)
if probability_spam>probability_ham:
    print("spam mail")
else:
    print ("non-spam mail")