def get_str(prompt):
  while True:
    try:
      return str(input(prompt))
    except ValueError:
      print ("Not a text")
      return 1
# lets get the text input to be encrypted
def main():
  y = get_str("plaintext:  ")
  plaintext_lower = y.lower()

main()



from sys import argv
  if len(argv) != 2:
    print("provide an integer without space")
  else:
    return x