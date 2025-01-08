import random

lucky_number = random.randint(1,100)

frotune_number = random.randint(1,3)

fortune_text = ''

if frotune_number == 1:
    
    fortune_text = 'You will have a great day!'

if frotune_number == 2:
    fortune_text = 'Today will be tough..but worth it.'

if frotune_number == 3:
    fortune_text = 'You will get merried this year!'

print(f'{fortune_text} Your Lucky number is: {frotune_number}t
      '