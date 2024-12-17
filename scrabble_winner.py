# create a code to determine the winner of a scrabble
# my program should prompt for input twice: once for Player1 and then for Player2
#then print: "Player1 wins!" or "Player2 wins!" or "Tie!"
this_dict = {
  "a" : 1 , "A" : 1,
  "b" : 3 , "B" : 3,
  "c" : 3 , "C" : 3,
  "d" : 2 , "D" : 2,
  "e" : 1 , "E" : 1,
  "f" : 4 , "F" : 4,
  "g" : 2 , "G" : 2,
  "h" : 4 , "H" : 4,
  "i" : 1 , "I" : 1,
  "j" : 8 , "J" : 8,
  "k" : 5 ,"K" : 5,
  "l" : 1 , "L" : 1,
  "m" : 3 , "M" : 3,
  "n" : 1 , "N" : 1,
  "o" : 1 , "O" : 1,
  "p" : 3 , "P" : 3,
  "q" : 10 , "Q" : 10,
  "r" : 1 , "R" : 1,
  "s" : 1 , "S" : 1,
  "t" : 1 , "T" : 1,
  "u" : 1 , "U" : 1,
  "v" : 4 , "V" : 4,
  "w" : 4 , "W" : 4,
  "x" : 8 , "X" : 8,
  "y" : 4 , "Y" : 4,
  "z" : 10 , "Z" : 10
}

int_of_each_char = []
Player1 = input ("Player1: ")
Player2 = input ("Player2: ")
i=0
while i<len(Player1):
  if Player1[i] in this_dict:
     value_of_char = this_dict[Player1[i]]
     int_of_each_char.append (value_of_char)
     i+=1
  else:
     i+=1
points_scored_player1 = sum(int_of_each_char)
int_of_each_char.clear()

i=0
while i<len(Player2):
  if Player2[i] in this_dict:
     value_of_char = this_dict[Player2[i]]
     int_of_each_char.append (value_of_char)
     i+=1
  else:
     i+=1
points_scored_player2 = sum(int_of_each_char)
int_of_each_char.clear()


if points_scored_player1 > points_scored_player2:
  print ("Player1 wins!")
elif points_scored_player1 < points_scored_player2:
    print ("Player2 wins!")
else:
  print ("Tie")