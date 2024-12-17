# get user input for key: a) key should be 26 letters of alphabet,
# -if its not 26 characters print an error message
# b) key should contain each letter of the alphabet once 
# - if not, print an error message
# b) and a single argument ie ABCDEF not ABC DEF. or print error
# c) the key should be case insensitive

# get user input for key and encrypted_text
alphabets = 'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
a=0
k=0
while True:
    try:
        key = str(input("key: "))
        key_lc = key.lower()
    except ValueError:
        print ("Provide only the letters of the alphabet")
        continue
    
# lets check that all the alphabet letters are represented in key
    check = all(e in alphabets for e in  key_lc)
    if check == False:
        print("provide only each of the letters of the alphabet")
        continue
    check = all(e in  key_lc for e in alphabets)
    if check == False:
        print("provide only each of the letters of the alphabet")
        continue
    if len(key_lc) < len(alphabets):
        print("Represent one of each of the letters of the alphabet")
        continue
    if len(key_lc) > len(alphabets):
        print("Represent one of each of the letters of the alphabet")
        continue
    else:
        break
        
       
    
while True:
    try:
        encrypted_text = str(input("encrypted_text : "))
        encrypted_text_lc = encrypted_text.lower()
    except ValueError:
        print("provide only letters")
        continue
    else:
        break

substitutes= []
e=0
k=0
a=0
while k<len(key) and a<len(alphabets):
    a = k
    if e <len(encrypted_text_lc):
        if encrypted_text_lc[e] in alphabets:
            if encrypted_text_lc[e] == alphabets[a]:
                substitutes.append(key[k])
                a=0
                k=0
                e+=1
            else:
                a+=1
                k+=1
        else:
             substitutes.append(encrypted_text_lc[e])
             e+=1
    else:
        break

joined_substitutes = "".join(substitutes)
in_actual_case = ""
ciphertext = []
e=0
while e <len(encrypted_text):
    if encrypted_text[e].isupper():
        popped_char = substitutes.pop(0)
        in_actual_case = in_actual_case + popped_char
        actual_case_uc = in_actual_case.upper()
        ciphertext.append(actual_case_uc)
        in_actual_case = ""
        e+=1
    elif encrypted_text[e].islower():
        popped_char = substitutes.pop(0)
        in_actual_case = in_actual_case + popped_char
        actual_case_lc = in_actual_case.lower()
        ciphertext.append(actual_case_lc)
        in_actual_case = ""
        e+=1
    else:
        popped_char = substitutes.pop(0)
        ciphertext.append(popped_char)
        e+=1
    
print(f"ciphertext: {"".join(ciphertext)}")