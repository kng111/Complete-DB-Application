# import pygame
# import pygame_menu
# pygame.init()
# surface = pygame.display.set_mode((600, 400))
# def set_difficulty(value, difficulty):
#     # Do the job here !
#     pass

# def start_the_game():
#     # Do the job here !
#     pass

# menu = pygame_menu.Menu('Welcome', 400, 300,
#                        theme=pygame_menu.themes.THEME_BLUE)

# menu.add.text_input('Name :', default='John Doe')
# menu.add.selector('Difficulty :', [('Hard', 1), ('Easy', 2)], onchange=set_difficulty)
# menu.add.button('Play', start_the_game)
# menu.add.button('Quit', pygame_menu.events.EXIT)
# menu.mainloop(surface)



# 

import pygame
import pygame_menu
import random

pygame.init()
#Size - name of the window
surface = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Example")

def game():
    #Variables
    score = 0
    user_age = age_input.get_value()
    user_name = user_input.get_value()
    while True:
        x = random.randint(0, 10)
        y = random.randint(0, 10)
        z = x + y
        print(str(x) + "+" + str(y))
        result = int(input())
        if result == z:
            print("Correct")
            score = score + 5
            
        else:
            if result != z:
                stop = input("Wrong! Wanna stop? ")
                if stop == ("yes"):
                    print("You have " + str(score) + " points")
                    break
                else:
                    continue

menu = pygame_menu.Menu('Menu', 600, 400,
                       theme=pygame_menu.themes.THEME_BLUE)

user_input = menu.add.text_input('User: ')
age_input = menu.add.text_input('Age: ')
menu.add.button('Start', game)
menu.add.button('Exit', pygame_menu.events.EXIT)

print (user_input)
print (age_input)

menu.mainloop(surface)




