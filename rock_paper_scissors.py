import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user = input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.')

array_computer_choice = [rock, paper, scissors]
user_choice = int(user)

random_index = random.randint(0, len(array_computer_choice) - 1)
random_element = array_computer_choice[random_index]

if user_choice == 0 and random_element == rock:
    print(f"{user_choice} \n {rock} \n Computer chose: \n {rock} \n You draw")
elif user_choice == 0 and random_element == paper:
    print(f"{user_choice} \n {rock} \n Computer chose: \n {paper} \n You lose")
elif user_choice == 0 and random_element == scissors:
    print(f"{user_choice} \n {rock} \n Computer chose: \n {scissors} \n You win")
elif user_choice == 1 and random_element == rock:
    print(f"{user_choice} \n {paper} \n Computer chose: \n {rock} \n You win")
elif user_choice == 1 and random_element == paper:
    print(f"{user_choice} \n {paper} \n Computer chose: \n {paper} \n You draw")
elif user_choice == 1 and random_element == scissors:
    print(f"{user_choice} \n {paper} \n Computer chose: \n {scissors} \n You lose")
elif user_choice == 2 and random_element == rock:
    print(f"{user_choice} \n {scissors} \n Computer chose: \n {rock} \n You lose")
elif user_choice == 2 and random_element == paper:
    print(f"{user_choice} \n {scissors} \n Computer chose: \n {paper} \n You win")
elif user_choice == 2 and random_element == scissors:
    print(f"{user_choice} \n {scissors} \n Computer chose: \n {scissors} \n You draw")
