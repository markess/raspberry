import pygame
import sys
import time

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

 axes = [ 0.0 ] * your_joystick.get_numaxes()
    buttons = [ False ] * your_joystick.get_numbuttons()

    while self.keep_alive:
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
             self.keep_alive = False
        elif event.type == pygame.JOYAXISMOTION:
            e = event.dict
            axes[e['axis']] = e['value']
        elif event.type in [pygame.JOYBUTTONUP, pygame.JOYBUTTONDOWN ]:
            e = event.dict
            buttons[e['button']] ^= True
