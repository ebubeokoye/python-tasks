def get_int (prompt):
    while True:
        try:
            return int (input(prompt))
        except ValueError:
            print ("Not an integer")
# we will convert the inputs directly to int to be able to sum(+),
# because in python, whatever you type at the command line is a string
def main():
    x = get_int ("x: ")
    y = get_int ("y: ")
    print (x+y)

main()