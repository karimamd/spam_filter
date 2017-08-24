from features import *
from prediction_function import *
file_name = input("File name: ")
with open(file_name) as f:
    txt = f.read()
i = 1
for line in txt.split("\n"):
    print ("EMAIL " + str(i) + ": ")
    i += 1
    #print(line)
    txtl = lemmatize_string(line)
    print (classify_stemmed_text(txtl))

