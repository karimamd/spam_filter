from spam import *
from ham import *
#words > 9 charachters are probably non english meaningful  words
#and counts number of all words(excluding filtered ones) in spam/eham/hham mails (summation of occurrences of all words)
#TODO this should be done while stemming!
def remove_big_words_from_list():
    hamCounter,spamCounter=0,0
    for key in ham.keys():
        hamCounter += ham[key]
    for key in spam.keys():
        spamCounter += spam[key]
    
    return ham,spam,hamCounter,spamCounter
