name = 'EBUBE LILIAN OKOYE'

#using the split fumction seperates each word after a delimiter(spacing) and puts all of them in a list ['EBUBE', 'LILIAN', 'OKOYE']
names = name.split()

#using the for loop to cause a one by one printing of each n in names causing them to be printed on 3 different lines
for n in names:
  
  #using .title() causes the first letter
  print(n.title())
