import pygame

print("Setap inicio")
pygame.init()
window = pygame.display.set_mode(size=(600, 480))
print("Setap fim")
print("Inicio loop")
while True:
    # Check for all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  # close window
            quit()  # end pygame
