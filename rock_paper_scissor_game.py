import random
item_list = ["Rock","Paper","Scissors"]

while True:
    user_choice = input("Enter your choice  ROCK,PAPER,SCISSORS:").capitalize()
    com_choice = random.choice(item_list)

    print(f"user choice= {user_choice}, computer choice = {com_choice}")
    if user_choice not in item_list:
     print("INVALID")
    elif com_choice == user_choice:
     print("THE GAME IS TIE")

    elif com_choice == 'Rock' and user_choice == 'Scissors':
     print('YOU LOSE THE GAME')

    elif com_choice == 'Paper' and user_choice == 'Scissors':
     print('YOU WON THE GAME')

    elif com_choice == 'Rock' and user_choice == 'Paper':
     print('YOU WON THE GAME')
    elif com_choice == 'Scissors' and user_choice == 'Paper':
      print('YOU LOSE THE GAME')     
 
    elif com_choice == 'Paper' and user_choice == 'Rock':
     print('YOU LOSE THE GAME,COMPT WON')

    elif com_choice == 'Scissors' and user_choice == 'Rock':
     print('YOU WON THE GAME') 