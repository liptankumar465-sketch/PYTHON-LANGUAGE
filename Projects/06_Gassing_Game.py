import random
#! Gassing Game
# ?-------------------------------------------------------------------

while True:
    random_gass = random.randint(1, 3)
    match random_gass:
        case 1:
            random_gass = 'rock'
        case 2:
            random_gass = 'paper'
        case 3:
            random_gass = 'siger'

    print('1) press for rock')
    print('2) press for paper')
    print('3) press for sigher')
    user_gass = int(input('Enter Your Gass:'))

    if user_gass == 1:
        user_gass = 'rock'
    elif user_gass == 2:
        user_gass = 'paper'
    elif user_gass == 3:
        user_gass = 'siger'
    else:
        print('---------------------------------------')
        print('Worng no press!')
        print('Press only 1 , 2 , 3')
        print('---------------------------------------')
        continue

    if user_gass == random_gass:
        print('---------------------------------------')
        print('Opponent Gass: ', random_gass)
        print('Your Gass: ', user_gass)
        print('You Win!')
        break
    else:
        print('---------------------------------------')
        print('Next Round!')
        continue
