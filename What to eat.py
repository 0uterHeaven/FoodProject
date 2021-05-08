   
import random

hungry = input('What do you want to eat: Thai, Italian, Chinese, Japanese, Continental, Mexican, Junk, homemade or random? ')

ethnicity = ['Thai', 'Italian', 'Chinese', 'Japanese', 'Continental', 'Mexican', 'Junk', 'Homemade']

if hungry == 'random':
    print(random.choice(ethnicity))

#ethnicity = ['Thai', 'Italian', 'Chinese', 'Japanese', 'Continental', 'Mexican', 'Junk', 'Homemade']
#print(random.choice(ethnicity))