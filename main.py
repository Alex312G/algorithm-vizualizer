import pygame
def main():
    pygame.init()
    screen = pygame.display.set_mode((1280,720))
    clock = pygame.time.Clock()
    pygame.display.set_caption("Vizual Algo")
    font = pygame.font.SysFont(None, 36)

    current_screen = "MENU"
    selected_algorithm = None
    #["Bubble Sort", "Selection Sort", "Insertion Sort", "Merge Sort", "Radix Sort"]
    Algorithms = ["Sorting", "Data Structures", "Graphs", "Number Theory", "Dynamic Programming", "Strings", "Math"]
    screen_width = 840
    gap = 100
    menu_area = pygame.Rect(0,100,screen_width,600)
    #bubble_button = pygame.Rect(300,150,200,50)
    scroll_offset = 0
    running = True
    while running:
        buttons = []
        start_y = 0
        start_x = screen_width/2
        for i, algorithm in enumerate(Algorithms):
            content_height = len(Algorithms) * gap
            max_scroll = max(0,content_height - menu_area.height)
            scroll_offset = max(0, min(scroll_offset, max_scroll))
            start_y+=gap
            y = start_y - scroll_offset
            rect = pygame.Rect(start_x,y, 200, 90)
            start_x += 220
            if i % 2 == 1:
                start_x = 420
            buttons.append((rect, algorithm))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEWHEEL:
                scroll_offset -= event.y*30
            elif event.type == pygame.MOUSEBUTTONDOWN:
              if event.button == 1:
                for button in buttons:
                    if button[0].collidepoint(event.pos):
                        selected_algorithm = button[1]
                        current_screen = "VIZUALIZING"
        screen.fill((30, 30, 30))
        if current_screen == "MENU":
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
           #for i, algorithm in enumerate(Algorithms):
             #   pygame.draw.rect(screen, (70, 130, 180), rect)
            #    text_surface = font.render(algorithm, True, (255, 255, 255))
           #     screen.blit(text_surface, text_surface.get_rect(center=rect.center))
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