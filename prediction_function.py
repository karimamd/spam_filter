def word_spam_probability(word):
    #not yet implemented

    return 0.1 *len(word)

def word_ham_probability(word):
    return 0.1*len(word)


probability_spam=1
probability_ham=1
#mail_words is list of stemmed words in fount in the input mail
mail="my name is kareem"
mail_words={"kareem"}
for each_word in mail_words:
    probability_spam*=word_spam_probability(each_word)
    probability_ham*=word_ham_probability(each_word)
if probability_spam>probability_ham:
    print("spam mail")
else:
    print ("non-spam mail")