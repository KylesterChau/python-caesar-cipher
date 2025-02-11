import string

alphabet_list = list(string.ascii_lowercase)

def encrypt(word, st):
    tem = ""
    for x in range(len(word)):
        if word[x] != " ":
            num = (alphabet_list.index(word[x]) + st) % 26
            tem += alphabet_list[num]
        else:
            tem += " "
    return tem

def decrypt(word,st):
    tem = ""
    for x in range(len(word)):
        if word[x] != " ":
            num = (alphabet_list.index(word[x]) - st) % 26
            tem += alphabet_list[num]
        else:
            tem += " "
    return tem      
try:
    Word=input("Enter word to cipher: ")
    shift= int(input("What is the shift? "))
    option = input("Encrypt (E) or Decrypt (D)? ").upper()
    if option == "E":
        print(encrypt(Word,shift))
    elif option == "D":
        print(decrypt(Word,shift))
    else:
        print("Invalid option")
except:
    print("Enter a valid option next time")