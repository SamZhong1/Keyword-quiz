k = open("keywords.txt", "r")
keywords = k.readlines()

def quiz():
  print("You will be tested on Python command definitions and will be scored out of 12, you need atleast 50% (6 correct) to pass the quiz")
  #generate a random question with set answers

def quiz_definition():
  user_option = int(input("Choose a number :\n 1. view definitions \n 2. start quiz \n Enter here: ")) 
  print("\n")

  if user_option == 1:
     for i in range (1,len(keywords),2):
       print(keywords[i].strip())
       print(keywords[i+1])
     user_option_2 = input("Would you like to start the quiz? \n YES \n NO \n Enter response in caps: ")
     if user_option_2 == "YES":
       quiz()
     if user_option_2 == "NO":
         print("Ok")
     else:
       print ("invalid option")

  if user_option == 2:
    print("Starting quiz...")
    quiz()

quiz_definition() 
