import pygame
import random
from algorithms.sorting import Bubble_Sort, Selection_Sort, Insertion_Sort, Merge_Sort
from vizualizer.renderer import algorithm_explained
def main():
    pygame.init()
    screen = pygame.display.set_mode((1280,720))
    clock = pygame.time.Clock()
    pygame.display.set_caption("Vizual Algo")
    font = pygame.font.SysFont(None, 36)
    description_font = pygame.font.SysFont(None, 26)
    current_screen = "MENU"
    selected_algorithm = None
    Menu_algorithms = {"Sorting" : ["Bubble Sort", "Selection Sort", "Insertion Sort", "Merge Sort", "Quick Sort", "Radix Sort"], "Data Structures" : [], "Graphs" : [], "Number Theory" : [], "Dynamic Programming" : [], "Strings" : [], "Math" : []}
    Vizualizing_buttons = ("speed_up", "speed_down", "pause")
    buttons_vizualize = []
    screen_width = 840
    gap = 100
    frame_limit = 15
    menu_area = pygame.Rect(0,100,screen_width,600)
    back_button = pygame.Rect(menu_area.left, menu_area.bottom-100, 150,70)
    x_first_button = screen_width + 100
    y_first_button = 100

    for i, butt in enumerate(Vizualizing_buttons):
        pos_x = x_first_button
        pos_y = y_first_button + i * 100
        rect = pygame.Rect(pos_x, pos_y, 200, 50)
        buttons_vizualize.append((rect, butt))
    #bubble_button = pygame.Rect(300,150,200,50)
    #sortings
    sorting_functions = {
        "Bubble Sort" : Bubble_Sort,
        "Selection Sort" : Selection_Sort,
        "Insertion Sort" : Insertion_Sort,
        "Merge Sort" : Merge_Sort
    }
    sorting_explained = {
        "Bubble Sort": "The algorithm iterates trough the array, it tries to find a value that is not in its place, if found the algorithm continues, ok = 1, if not the algorithm will stop, ok remains 0, Complexity: O(n^2)",
        "Selection Sort" : "The simplest sorting algorithm will get trough each value and will search in the values that remain after, the smallest/biggest that could be placed in that position Complexity: O(n^2).",
        "Insertion Sort" : "This algorithm searches trough the values that are in the array one that is smaller than the value/values before it then it moves it to a position where this is false, it is similar to finding if a sequence of brackets is correct. Complexity: O(n^2)",
        "Merge Sort" : "We take the values and divide the array in intervals until we get to the smallest possible then we merge the values as we go back in the function, the smallest intervals are sorted so each of the next intervals of bigger values will be sorted, Complexity: O(n*log n)."
    }
    
    scroll_offset = 0
    running = True
    Start_menu = True
    pressed = False
    Menu_algorithms_chose = Menu_algorithms.keys()
    algorithm_generator = None
    data = random.sample(range(1,101),10)
    current_state = {"array": data, "comparing": None}
    paused = False
    frame_counter = 0
    while running:
        #showing buttons precalculate
        buttons = []
        start_y = 0
        start_x = screen_width/2

        for i, algorithm in enumerate(Menu_algorithms_chose):
            content_height = len(Menu_algorithms_chose) * gap
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
                            algorithm_name = sorting_functions[selected_algorithm]
                            algorithm_generator = algorithm_name(data)
                            current_state = {"array": data.copy(), "comparing": None}
                            current_screen = "VIZUALIZING"
                        else:
                            pressed = True
                            Start_menu = False
                for button in buttons_vizualize:
                    if button[0].collidepoint(event.pos):
                        if current_screen == "VIZUALIZING":
                            if button[1] == "speed_up":
                                if frame_limit > 0:
                                    frame_limit -= 5
                            elif button[1] == "speed_down":
                                if frame_limit < 60:
                                    frame_limit += 5
                            elif button[1] == "pause":
                                if paused:
                                    paused = False
                                else:
                                    paused = True
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
            if not paused and algorithm_generator is not None:
                frame_counter += 1
                if frame_counter >= frame_limit:
                    frame_counter = 0
                    try:
                        current_state = next(algorithm_generator)
                    except StopIteration:
                        pass
            arr = current_state["array"]
            comparing = current_state["comparing"]
            bar_width = screen_width // len(arr)
            max_val = max(arr)
            num_pos = 560
            pygame.draw.line(screen, (255,255,255), (0,num_pos - 50),(0,num_pos+150),5)
            for i, val in enumerate(arr):
                if comparing and i in comparing:
                    color1 = (255,100,100)
                    color2 = (255,100,100)  
                else: 
                    color1 = (70,130,180)
                    color2 = (255,255,255)
                height = int((val/max_val)*400)
                x = i * bar_width
                y = 500 - height
                pygame.draw.rect(screen, color1,(x,y,bar_width-5, height))
                
                #draw buttons
                for rect in buttons_vizualize:
                    pygame.draw.rect(screen, (255,255,255), rect[0])
                    text_buttons = font.render(rect[1],True, (0,0,0))
                    text_rect_butt = text_buttons.get_rect(center = rect[0].center)
                    screen.blit(text_buttons, text_rect_butt)
                #explaination of algorithm
                pos_x = x_first_button
                pos_y = y_first_button + len(Vizualizing_buttons) * 100
                lines = algorithm_explained(sorting_explained[selected_algorithm], description_font, max_width=300)
                title = font.render(selected_algorithm, True, (255,255,255))
                screen.blit(title, (pos_x, pos_y))
                pos_y += 40
                for i, line in enumerate(lines):
                    line_paragraph = description_font.render(line, True, (255,255,255))
                    screen.blit(line_paragraph, (pos_x, pos_y + i * 28))
                #draw vector
                pygame.draw.line(screen, (255,255,255),(0,num_pos+50),(screen_width,num_pos+50),5)
                pygame.draw.line(screen, (255,255,255),(0,num_pos+150),(screen_width,num_pos+150),5)
                pygame.draw.line(screen, (255,255,255),(0,num_pos-50),(screen_width,num_pos-50),5)
                pygame.draw.line(screen, (255,255,255),(x+bar_width,num_pos-50),(x+bar_width,num_pos+150),5)
                text_vect = font.render(str(i), True, color2)
                text_rect_v = text_vect.get_rect(center = (x + bar_width//2,num_pos))
                text_num = font.render(str(val), True, (255,255,255))
                text_rect = text_num.get_rect(center = (x+bar_width//2,num_pos + 100))
                screen.blit(text_vect, text_rect_v)
                screen.blit(text_num, text_rect)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
if __name__ == "__main__":
    main()