import os 
from PIL import Image
import pygame

pygame.init()

__dirname__ = os.path.dirname(os.path.abspath(__file__))
__basename__ = os.path.basename(__dirname__)

model_image_dir = os.path.join(__dirname__, "FTC-Images/cubebox")


model_image = Image.open(os.path.join(model_image_dir, "0514.jpg"))
print(model_image.size)


# assigning values to X and Y variable
X = model_image.size[0]
Y = model_image.size[1]

display_surface = pygame.display.set_mode((X-100, Y-100))

pygame.display.set_caption('Image')

image = pygame.image.load(os.path.join(model_image_dir, "0514.jpg"))

white = (255,255,255)

# infinite loop
while True :
  
    # completely fill the surface object
    # with white colour
    display_surface.fill(white)
  
    # copying the image surface object
    # to the display surface object at
    # (0, 0) coordinate.
    display_surface.blit(image, (0, 0))
  
    # iterate over the list of Event objects
    # that was returned by pygame.event.get() method.
    for event in pygame.event.get() :
  
        # if event object type is QUIT
        # then quitting the pygame
        # and program both.
        if event.type == pygame.QUIT :
  
            # deactivates the pygame library
            pygame.quit()
  
            # quit the program.
            quit()
  
        # Draws the surface object to the screen.  
        pygame.display.update() 