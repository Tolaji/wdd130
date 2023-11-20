print('~\n~~~~~~~ Comparing numbers ~~~~~~~\n')

First_number = float(input('What is the first number? '))
second_number = float(input('What is the second number? '))
if First_number > second_number:
    print('The first number is greater')
else:
    print('The first number is not greater')
    if First_number == second_number:
        print('The numbers are equal')
    else:
        print('The numbers are not equal')
        if second_number > First_number:
            print('The second number is greater')
        else:
            print('The second number is not greater')
            print()
fav_animal = input('What is your favourite animal? ')
my_fav_animal = 'dog'
print()
if fav_animal.lower() == my_fav_animal.lower():
    print('Thats my favourite animal too!')
else:
    print('That one is not my favourite')