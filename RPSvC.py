def play():
    
    import random

    name1 = input('Player 1 Please enter your name ')
    print(f'{name1} you will be playing rock paper scissors vs the CPU')
    
    name1score = 0
    cpuscore = 0
    wins_nes = 5
    cpu_list = ['r', 'p', 's']

    
    
    
     
    while name1score != wins_nes and cpuscore != wins_nes:
        
        print(f'{name1}s score is {name1score}. \nCPUs score is {cpuscore}')

        
            #pick your answer
        user1 = input(name1 + ', make your move (r, p, or s) ')
        user2 = random.choice(cpu_list)

        
        
        while user1 == user2:
            print('it is a draw. Please try again')
            user1 = input(name1 + ', make your move (r, p, or s) ')
            user2 = random.choice(cpu_list)

    
    
        if user1 != user2:
                        #rock>scissors
            if user1 == 'r' and user2 == 's':
                name1score += 1
            if user2 == 'r' and user1 == 's':
                cpuscore += 1


                   
                      #rock<paper
            if user1 == 'r' and user2 == 'p':
                cpuscore += 1

            if user2 == 'r' and user1 == 'p':
                name1score += 1

                        #paper<scissors
            if user2 == 's' and user1 == 'p':
                cpuscore += 1
            if user1 == 's' and user2 == 'p':
                name1score += 1

      
            
        
    if name1score == wins_nes:
        print(f'Congratulations {name1}, you beat that loser!')

    if cpuscore == wins_nes:
        print(f'Congratulations {name1}, you LOST to the CPU! HAHA!')

if __name__ == '__main__':
    play()
        