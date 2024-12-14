import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i']
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,]
characters = ['!', '+', '&', '%', '?' ,'*','#']

nr_letters = int(input(f"How many letters would you like in your password?"))
nr_numbers = int(input(f"how many numbers would you like in your password?"))
nr_characters = int(input(f"how many characters would you like in your password?"))

password_list = []

for i in range(nr_letters):
    random_letter = random.choice(letters)
    password_list += random_letter


for i in range(nr_numbers):
    random_number = random.choice(numbers)
    password_list += str(random_number)



for i in range(nr_characters):
    random_character = random.choice(characters)
    password_list += random_character      
random.shuffle(password_list)


password = ""
for i in password_list:
    password += i
    
    
print(f"Your password is: {password}")





