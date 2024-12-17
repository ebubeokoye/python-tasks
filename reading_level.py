# using coleman_Liau index formula to determine the grade level of the text above:
# index = 0.0588 * L - 0.296 * S - 15.8
import unicodedata

text = input ("Text: ")
alphabets = ['a','A','b','B','c','C','d','D','e','E','f','F','g','G','h','H','i','I','j','J','k','K','l','L','m','M','n','N',
             'o','O','p','P','q','Q','r','R','s','S','t','T','u','U','v','V','w','W','x','X','y','Y','z','Z']
quotations_to_end_sentences = ['.', '!', '?']
space = " "
# lets count the letters- no punctuation marks or spaces includes
text_list = list(text)
count_of_letters =[]
counter = 0
i=0
while i < len(text_list):
    if text_list[i] in alphabets:
        counter+=1
        i+=1
    else:
        i+=1
count_of_letters=counter
# lets see how many words by counting the spaces- a word end where there is space 
# i equated counter to 1 instead of 0 bcuz after the last 'space' comes a word which
#wont be counted if we are only checking for spaces, so i added its count to counter 
i=0
counter = 1
number_of_words = []
while i < len(text_list):
    if text_list[i] == space:
        counter+=1
        i+=1
    elif text_list[i] != space:
        i+=1
number_of_words=counter
# lets count the sentences- sentences end with . or ! or ?
i=0
counter = 0
number_of_sentences = []
while i < len(text_list):
    if text_list[i] in quotations_to_end_sentences:
        counter+=1
        i+=1
    else:
        i+=1
number_of_sentences=counter

# the Coleman-Liau index:
L = (count_of_letters * 100)/number_of_words
S = (number_of_sentences * 100)/number_of_words
index = 0.0588 * L - 0.296 * S - 15.8
rounded_index = round(index)
if rounded_index >= 16:
    print("Grade 16+")
elif rounded_index < 1:
    print("Before Grade 1")
else:
    print(f"Grade {rounded_index}")