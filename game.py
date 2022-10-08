from random import randint
#what will we learn?
# 1. variable - store input, access later.
# 2. user input - enter data.
# 3. operator - sub, add, smaller , bigger.
# 4. list
# 5. dictionaries - store information in python .
# 6. function - create , what function, reusable code.
# 7. control schem - if else.
# 8. f-string/formative string - dynamically check information from outside
 
#variables
"""
player_name = 'Jerry'
player_attack = 10 
player_heal = 16
player_health = 100
"""
#list
"""
player = ['Jerry', 10, 16, 100]
player[1] = 12 #change value using index in list
print(player[1]) # print using indexx [n]
"""

#Dictionary key value pair

game_running = True
#functions
def calc_monster_attack():
    return randint(monster['attack_min'], monster['attack_max'])

#control scheme while loop
while game_running == True:
    new_round = True
    player ={'name': 'Jerry', 'attack':12, 'heal':25, 'health':100} 
    monster ={'name': 'soul eater', 'attack_min': 16, 'attack_max': 25, 'health': 100}
    print("enter player name")
    player['name'] =  input()
    while new_round == True:
        player_won = False
        monster_won = False
        print('Select action')
        print('1. Attack')
        print('2. Heal')
        print('3. Exit')
        
        #input
        player_choice = input()

        #control scheme + comparision operator
        if player_choice == '1':
            monster['health'] = monster['health'] - player['attack']
            if monster['health'] <=0:
                player_won = True
                
            else:
                
                player['health'] = player['health'] - calc_monster_attack()
                if player['health'] <=0:
                    monster_won = True
                     

            
        elif player_choice == '2':
            if player['health'] >= 80:
                
                print('Cannot use heal now')
                player['health'] = player['health'] - calc_monster_attack()
                
            else:
                monster_attack = randint(monster['attack_min'], monster['attack_max'])
                player['health'] = player['health'] + player['heal']
                player['health'] = player['health'] - monster_attack
                if player['health'] <= 0:
                    monster_won = True
            
        elif player_choice == '3':
            new_round = False
            game_running = False    
        else:
            print('Invalid input')
        
        
        if player_won == False and monster_won == False:
            print(monster['name'] + '  has  ' + str(monster['health']) + '  health') 
            print(player['name'] + '  has  ' + str(player['health']) + '  health')
        elif monster_won:
            print('- - -' * 7)
            print(monster['name']  +  '  won')
            print('- - -' * 7)
            new_round = False            
        elif player_won:
            print('- - -' * 7)
            print(player['name']  +  '  won')
            print('- - -' * 7)
            new_round = False


             
            
       
    
        
     
  