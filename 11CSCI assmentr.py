
play ="y"
while play == "y":
  score = 0
  print ("Your goal is to 60% or over otherwise you fail")
  quiz1= {"What movie has Julian Dennison and Ryan Ryenolds. \n a) Finding Nemo \n b) Green Lantern \n c) Oppenheimer \n d) Deadpool 2 \n ":'d',"What country is Julian Dennison from? \n a) Canada \n b) Russia \n c) Moldova \n d) New Zealand \n ":'d', "Who is Julian Dennison’s mum? \n a) Mabelle Dennison \n b) Dwayne Johnson \n c) Tony Stark \n d) Wonder Woman \n":'a', "When was Julian Dennison born? \n a) 30th of February 2008 \n b) 19 September 2002 \n c) 26 October 2054 \n d) 26 October 26 2002":'d',"What ethnicity is Julian Dennison? \n a) Chinese \n b) Maori \n c) Hawaiian \n d) Chicken BBQ Sausage":'b',}
  for x in  quiz1:
    print(x)
    user_input = input("Please answer the question using a, b, c or d.\n Enter Answer: ")
    if user_input == (quiz1[x]):
      print("Correct!")
      score = score + 20
    else:
      print("Incorrect!")
    print (quiz1[x])
  
  print("You scored", score, "%")
  
  if score >= 60:
    print ("You have passed this test")
  else:
    print ("You have failed this test")
  play = input("Would you like to play again? y/n \n Enter: ")
