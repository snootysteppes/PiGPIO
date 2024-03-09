import pygame # sudo pip3 RPi.GPIO
import RPi.GPIO as GPIO # sudo pip3 RPi.GPIO

# Set up GPIO
GPIO.setmode(GPIO.BCM) # no clue what this is icl
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP) # 17 = Pin No, Took me a while to find out lol

# Set up Pygame
pygame.init() # need to actually call Pygame function

# Function to be called when button is pressed
def button_func():
    print("Hello, world!") # modify this

# Main game loop
while True:
    # Check if button is pressed
    if not GPIO.input(17): # modify pin if not 17
        button_func()

    # Pygame event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            GPIO.cleanup()
            quit()

# https://pypi.org/project/RPi.GPIO/ - PyPi Module
# https://sourceforge.net/p/raspberry-gpio-python/wiki/Home/ - Documentation
# Tested and Working with up to 3.10
