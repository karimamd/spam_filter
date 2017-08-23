from spam import *
from hham import *
from eham import *
#words > 9 charachters are probably non english meaningful  words
#and counts number of all words(excluding filtered ones) in spam/eham/hham mails (summation of occurrences of all words)
def remove_big_words_from_list():
    ehamCounter,hhamCounter,spamCounter=0,0,0
    for i in eham:
        if len(i[0]) > 9 or len(i[0]) == 1:
            eham.remove(i)
        else:
            ehamCounter+=int(i[1])

    for i in spam:
        if len(i[0]) > 9 or len(i[0]) == 1:
            spam.remove(i)
        else:
            spamCounter+=int(i[1])

    for i in hham:
        if len(i[0]) > 9 or len(i[0]) == 1:
            hham.remove(i)
        else:
            hhamCounter+=int(i[1])
    return eham,hham,spam,ehamCounter,hhamCounter,spamCounter
