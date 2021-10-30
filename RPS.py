def play():
    
    name1 = input('Player 1 Please enter your name ')
    name2 = input('Player 2 Please enter your name ')
    
    name1score = 0
    name2score = 0
    wins_nes = 5
    
    
     
    while name1score != wins_nes and name2score != wins_nes:
        
        print(f'{name1}s score is {name1score}. \n{name2}s score is {name2score}')

        
            #pick your answer
        user1 = input(name1 + ', make your move (r, p, or s) ')
        user2 = input(name2 + ', make your move (r, p, or s) ')

        
        
        if user1 == user2:
            print('it is a draw. Please try again')
            user1 = input(name1 + ', make your move (r, p, or s) ')
            user2 = input(name2 + ', make your move (r, p, or s) ')
    
    
        if user1 != user2:
                        #rock>scissors
            if user1 == 'r' and user2 == 's':
                name1score += 1
            if user2 == 'r' and user1 == 's':
                name2score += 1


                   
                      #rock<paper
            if user1 == 'r' and user2 == 'p':
                name2score += 1

            if user2 == 'r' and user1 == 'p':
                name1score += 1

                        #paper<scissors
            if user2 == 's' and user1 == 'p':
                name2score += 1
            if user1 == 's' and user2 == 'p':
                name1score += 1

      
            
        
    if name1score == wins_nes or name2score == wins_nes:
        print(f'Congratulations {name1}, you beat that loser!')

    else:
        print(f'Congratulations {name2}, you beat that loser!')

if __name__ == '__main__':
    play()
        