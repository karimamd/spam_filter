from spam import *
from ham import *
#words > 9 charachters are probably non english meaningful  words
#and counts number of all words(excluding filtered ones) in spam/eham/hham mails (summation of occurrences of all words)
#TODO this should be done while stemming!
def remove_big_words_from_list():
    hamCounter,spamCounter=0,0
    del_set = set(list("abcdefghijklmnopqrstuvwxyz"))
    for key in ham.keys():
        if key.isupper():
            continue
        if len(key) > 9:
            del_set.add(key)
        else:
            hamCounter += ham[key]
    for word in del_set:
        del ham[word]
    
    del_set = set(list("abcdefghijklmnopqrstuvwxyz"))
    for key in spam.keys():
        if key.isupper():
            continue
        if len(key) > 9:
            del_set.add(key)
        else:
            spamCounter += spam[key]
    
    for word in del_set:
        del ham[word]
    return ham,spam,hamCounter,spamCounter
