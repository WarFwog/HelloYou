# Add your Python code here. E.g.
from microbit import *
import music

while True:

        if button_a.is_pressed():
            notes = ['A3:3', 'C4', 'E', 'A', 'B', 'E', 'C', 'B', 'C5', 'E4', 'C', 'C5', 'F#4', 'D',
                     'A3', 'F#4','E', 'C','A3', 'C4:6', 'E:3', 'C', 'A3', 'G', 'A', 'A:12', 'A2:3', 'F3', 'E',
                     'A2', 'A3', 'C4', 'E', 'B', 'E', 'C', 'B', 'C5', 'E4', 'C', 'C5', 'F#4', 'D',
                     'A3', 'F#4','E', 'C','A3', 'C4:6', 'E:3', 'C', 'A3', 'G', 'A', 'A:12',
                     'A2:3', 'B', 'C3', 'E', 'G', 'E4', 'F#', 'D', 'A3', 'F#4', 'E', 'C', 'A3', 'E4', 'B3:1', 'C4:2', 'A3:3', 'A2', 'B', 'C4', 'G3', 'E', 'C4', 'G', 'B3', 'G', 'G4:2', 'G:1', 'F#:2', 'F#:3', 'F#:12',
                     'A2:3', 'B', 'C3', 'E', 'G', 'C4', 'F#', 'D', 'A3', 'F#4', 'E', 'C', 'A3', 'E4', 'B3:1', 'C4:2', 'A3:3', 'A2', 'B', 'C3', 'E', 'G', 'C4', 'D3', 'A', 'C4', 'F#', 'E', 'E', 'E:12', ]
            music.play(notes)
        
        if button_b.is_pressed():
            display.scroll('De song titel is: Stairway to heaven van Led Zeppelin')