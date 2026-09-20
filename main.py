import pygame
import random
from algorithms.sorting import Bubble_Sort
def main():
    pygame.init()
    screen = pygame.display.set_mode((1280,720))
    clock = pygame.time.Clock()
    pygame.display.set_caption("Vizual Algo")
    font = pygame.font.SysFont(None, 36)
    current_screen = "MENU"
    selected_algorithm = None
    Menu_algorithms = {"Sorting" : ["Bubble Sort", "Selection Sort", "Insertion Sort", "Merge Sort", "Quick Sort", "Radix Sort"], "Data Structures" : [], "Graphs" : [], "Number Theory" : [], "Dynamic Programming" : [], "Strings" : [], "Math" : []}
    screen_width = 840
    gap = 100
    menu_area = pygame.Rect(0,100,screen_width,600)
    back_button = pygame.Rect(menu_area.left, menu_area.bottom-100, 150,70)
    #bubble_button = pygame.Rect(300,150,200,50)
    sorting_functions = {
        "Bubble Sort" : Bubble_Sort
    }
    scroll_offset = 0
    running = True
    Start_menu = True
    pressed = False
    Menu_algorithms_chose = Menu_algorithms.keys()
    algorithm_generator = None
    current_state = {"array": data, "comparing": None}
    paused = False
    while running:
        #showing buttons precalculate
        buttons = []
        start_y = 0
        start_x = screen_width/2

        for i, algorithm in enumerate(Menu_algorithms_chose):
            content_height = len(Menu_algorithms) * gap
            max_scroll = max(0,content_height - menu_area.height)
            scroll_offset = max(0, min(scroll_offset, max_scroll))
            start_y+=gap
            y = start_y - scroll_offset
            rect = pygame.Rect(start_x,y, 200, 90)
            start_x += 220
            if i % 2 == 1:
                start_x = 420
            buttons.append((rect, algorithm))

        #events, keypresses, scroll etc.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEWHEEL:
                scroll_offset -= event.y*30
            elif event.type == pygame.MOUSEBUTTONDOWN:
              if event.button == 1:
                if back_button.collidepoint(event.pos):
                    pressed = True
                    Start_menu = True
                for button in buttons:
                    if button[0].collidepoint(event.pos):
                        selected_algorithm = button[1]
                        if Start_menu == False:
                            data = random.sample(range(1,101),5)
                            algorithm_name = sorting_functions[selected_algorithm]
                            algorithm_generator = algorithm_name(data)
                            current_state = {"array": data.copy(), "comparing": None}
                            current_screen = "VIZUALIZING"
                        else:
                            pressed = True
                            Start_menu = False
                        
                        #current_screen = "SELECTION MENU"
        screen.fill((30, 30, 30))
        #Menu screen with all the buttons shown
        if current_screen == "MENU":
           if Start_menu == False:
               pygame.draw.rect(screen, (70,130,180), back_button)
               text_back_button = font.render("Back", True, (255,255,255))
               screen.blit(text_back_button, text_surface.get_rect(center = back_button.center))
               if pressed == True:
                    Menu_algorithms_chose = Menu_algorithms[selected_algorithm]
                    pressed = False
           elif Start_menu == True and pressed == True:
               Menu_algorithms_chose = Menu_algorithms.keys()
               pressed = False
           scrollbar_track = pygame.Rect(menu_area.right, menu_area.top, 10, menu_area.height)
           pygame.draw.rect(screen, (60,60,60), scrollbar_track)
           if max_scroll > 0:
               handle_height = max(30, menu_area.height * (menu_area.height / (max_scroll + menu_area.height)))
               scroll_progress = scroll_offset/max_scroll
               handle_y = menu_area.top + scroll_progress * (menu_area.height - handle_height)
               if 0<=scroll_progress<=1:
                scrollbar_handle = pygame.Rect(menu_area.right,handle_y,10, handle_height)
                pygame.draw.rect(screen, (150,150,150), scrollbar_handle)
           screen.set_clip(menu_area)
           for button in buttons:
               pygame.draw.rect(screen, (70,130,180), button[0])
               text_surface = font.render(button[1], True, (255,255,255))
               screen.blit(text_surface, text_surface.get_rect(center = button[0].center))
           screen.set_clip(None)
        elif current_screen == "VIZUALIZING":
            text = font.render("we will continue", True,(255,255,255))
            screen.blit(text, (50,50))
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
if __name__ == "__main__":
    main()