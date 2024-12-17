# this is where we check the key input for a)value error; to be sure its an int,
# b) error if the user gives a -ve number (<0)
# c) error if the user gives a value > 2147483648
while True:
  try:
    key = int(input("key:  "))
  except ValueError:
    print ("Not an integer")
    continue
  if key < 0:
    continue
  if key > 2147483648:
    continue
  else:
    break

# lets make sure the user gives a str as input
while True:
    try:
      plaintext = str(input("plaintext: "))
# then convert the text to all lower case so that you can work with it using the dict and list,
# that i created below, which are in lower case
      plaintext_lowercase = plaintext.lower()
    except ValueError:
      print ("Not a text")
      continue
    if True:
      break
# this is where we check the text input for value error; to be sure its a string
alphabets_dict = {
    "a": 0,
    "b": 1,
    "c": 2,
    "d": 3,
    "e": 4,
    "f": 5,
    "g": 6,
    "h": 7,
    "i": 8,
    "j": 9,
    "k": 10,
    "l": 11,
    "m": 12,
    "n": 13,
    "o": 14,
    "p": 15,
    "q": 16,
    "r": 17,
    "s": 18,
    "t": 19,
    "u": 20,
    "v": 21,
    "w": 22,
    "x": 23,
    "y": 24,
    "z": 25,
  }

alphabets_list= ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# k: check for max number, argv, and no cla at all

encrypted_text =[]
counter=0
i=0
j=0

while i <len(plaintext_lowercase):
  if plaintext_lowercase[i] not in alphabets_dict:
# the only scenario where plaintext_lowercase will not be in alphabets_dict is if its a special character
# or a space which we wont encrypt but will need to still add to the final result
      encrypted_text.append(plaintext_lowercase[i])
      i+=1
  else:
      starting_value = alphabets_dict[plaintext_lowercase[i]]
      if j< len(alphabets_dict):
            if j != starting_value:
                j+=1
            elif j == starting_value:
# eg first character H is at position 7 in the dictionary, but in actual alphabet count,
# the position is 8 which is what matters when we start adding key.
                k = j+1
                j=0
# k is the value of each letter(1-26). k=1 is 'a'
                while counter< key:
                    if k < len(alphabets_dict):
                        k += 1
                        counter+=1
                    elif k == len(alphabets_dict):
# by the time k is 26, it is at alphabet z, then we want it to wrap around and start counting from
# alphabet a again, so the we initialize it to 0 before it starts counting from a again as it goes
#back to the if conditional above then alphabet a is k=1
                        alphabets_dict["a"] = alphabets_dict["a"] + k
                        k=0

                        counter+=1
# this next line is not so relevant, but its to show you the  position to expect the new/encrypted
# char to be. eg if at the end of the day a= 52, if encrypted_value is 56, that means k=4 for that round
# so then the new/encypted char will be the alphabet at position 4
                encrypted_value = alphabets_dict["a"] + k
                z=0
                counter = 0
                while z < len(alphabets_list):
                    if counter < k:
                        z+=1
                        counter+=1
                    else:
                        encrypted_text.append(alphabets_list[z])
                        alphabets_dict["a"] = 0
                        counter=0
                        j = 0
                        i += 1
                        break


#lets check if each char in plaintext is in upper case, otherwise,
# we change the encrypted_text equivalent index to uppercase
in_actual_case = ""
ciphertext = []
i=0
while i<len(plaintext):
    if plaintext[i].isupper():
      popped = encrypted_text.pop(0)
      in_actual_case = in_actual_case + popped
      in_actual_case_uc = in_actual_case.upper()
      ciphertext.append(in_actual_case_uc)
      in_actual_case = ""
      i+=1

    if plaintext[i].islower():
      popped = encrypted_text.pop(0)
      in_actual_case = in_actual_case + popped
      in_actual_case_lc = in_actual_case.lower()
      ciphertext.append(in_actual_case_lc)
      in_actual_case = ""
      i+=1
    else:
       popped = encrypted_text.pop(0)
       ciphertext.append(popped)
       i+=1
       
joined_cipher_text = "".join(ciphertext)
print(f"ciphertext: {joined_cipher_text}")

