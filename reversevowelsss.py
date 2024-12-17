def getReverseVowels(word):
    vowels = "aAeEiIoOuU"
    vowelChars = list(vowels)
    charsInWord = list(word)
    
    # We will go over the word "icecream" in a loop.
    # During the loop, we will identify the vowels.
    # When we identify a vowel, we will take note of 2 things:
        # the position (index) of the vowel
            # e.g vowelIndexes = [0, 2, 5, 6];
        # the actual vowel.
            # e.g identifiedVowels = [I, e, e, A]
    # We will reverse the vowels we identified.
        # reversedVowels = [A, e, e, I]
    # Next, we replace each vowel's position with the vowel in the same position after the reversal.
    i = 0
    vowelIndexes = []
    identifiedVowels = []
    while i < len(charsInWord):
        actualVowel = charsInWord[i]
        if actualVowel in vowelChars:
            vowelIndexes.append(i)
            identifiedVowels.append(actualVowel)
        i += 1

    # Reverse the identified vowels.
    identifiedVowels.reverse()

    i = 0
    # IceCreAm the word
    # vowelIndexes = [0, 2, 5, 6] positions of vowels in the word
    # [A, e, e, I] reversed identified vowels

    while i < len(identifiedVowels):
        vowelIndexInWord = vowelIndexes[i]
        charsInWord[vowelIndexInWord] = identifiedVowels[i]
        i += 1

    return "".join(charsInWord)

print(getReverseVowels("IceCreAm"))
