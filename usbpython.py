import pygame
import sys
import time

done = False

pygame.joystick.init()

print pygame.joystick.get_count()

_joystick = pygame.joystick.Joystick(0)
_joystick.init()
print _joystick.get_init()
print _joystick.get_id()
print _joystick.get_name()
print _joystick.get_numaxes()
print _joystick.get_numballs()
print _joystick.get_numbuttons()
print _joystick.get_numhats()
print _joystick.get_axis(0)

joystick_count = pygame.joystick.get_count()
for i in range(joystick_count):
    joystick = pygame.joystick.Joystick(i)
    joystick.init()
while done==False:
    for i in range(joystick_count):
        axis = joystick.get_axis( i )
        print ("Axis {} value: {:>6.3f}".format(i, axis) )

    buttons = joystick.get_numbuttons()
    print("Number of buttons: {}".format(buttons) )
    for i in range( buttons ):
        button = joystick.get_button( i )
        print("Button {:>2} value: {}".format(i,button) )
        
