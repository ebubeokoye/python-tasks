
s = "abciiidef"
vowels = ["a","e","i","o","u"]
thisdict = {
    "a" : 0,
    "e" : 0,
    "i" : 0,
    "o" : 0,
    "u" : 0
}
i = 0
while i < len(vowels):
    j=0
    while j < len(s):
        if s[j] == vowels[i]:
           thisdict [s[j]]+=1
        j+=1 
    i+=1
x = thisdict.values()
maximum = max (thisdict.values())
print(maximum)