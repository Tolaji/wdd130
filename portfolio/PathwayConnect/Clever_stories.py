# Additional creative element:
# Gave the user ability to title the story thereby personalizing same
# Capitalized the title using code
# Added 2 more adjectives to the story
# Added a sentence with "a" based on the starting letter of the adjective at the end of the story.

#Hint
print('\n~~~ MAD LIB STORY ~~~\n')

# Prompt user to personally title the story
story_title = input('Title this Story: ')
print()

#Example prompt insight
print('Please consider the following prompts before proceeding')
print()
print('Adjective')
print('Animal')
print('Exclamation')
print('Verb')
print()

# Prompt the user for inputs
adjective = input('Enter an adjective: ')
animal = input('Enter an animal: ')
verb1 = input('Enter a verb: ')
exclamation = input('Enter an exclamation: ')
verb2 = input('Enter another verb: ')
adjective2 = input('Enter another adjective: ')
adjective3 = input('Enter final adjective: ')
print()

#Show story title in upper case
print(f'{story_title.upper()}')

# Construct the mad lib story
print('The other day, I was really in trouble. It all started when I saw a very')
print('' + adjective + ' ' + animal + ' ' + verb1 + ' down the hallway. "' + exclamation.capitalize() + '!" I yelled.')
print('But all I could think to do was to ' + verb2 + ' over and over. Miraculously,')
print('that caused it to stop, but not before it tried to ' + verb2 + '')
print('right in front of my family.')
print('A day like this would usually get me ' + adjective2 + ' but i ended up feeling very ' + adjective3 + '.')
print()
