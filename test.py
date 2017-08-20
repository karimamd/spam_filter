from features import *
file_name = input("File name: ")
with open(file_name) as f:
    mail = f.read()
props = email_parser(mail)
for key in props.keys():
    print (key + ":\n"+ "=" * (len(key) +1))
    print(props[key])


print("Lemmatizing:\n" + "=" * (len("Lemmatizing") +1))
print (lemmatize_string(props["body"]))
