# pyvidplayer
An extremely easy to use module that plays videos on Pygame

# updated!
This actually got more users than I thought, so I felt obligated to
improve it a bit. Hang tight while I type up the new docs

changes:
- a fallback resizing function since the one ffpyplayer uses is very buggy
- get_file_data has been replaced with properties to increase performance
- get_playback_data has been split into individual functions to increase performance
- a few more clearly named variables
- removed the close method since video resources are now released automatically
- the draw method now returns true/false depending on if a frame has been drawn

**Example**
```
import pygame
from pyvidplayer import Video

pygame.init()
win = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

#provide video class with the path to your video
vid = Video("4.mp4")
vid.set_size((1280, 720))

while True:
    key = None
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #release video resources when done
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            key = pygame.key.name(event.key)
    
    #your program frame rate does not affect video playback
    #more info below
    clock.tick(60)
    
    if key == "r":
        vid.restart()           #rewind video to beginning
    elif key == "p":
        vid.toggle_pause()      #pause/plays video
    elif key == "right":
        vid.seek(15)            #skip 15 seconds in video
    elif key == "left":
        vid.seek(-15)           #rewind 15 seconds in video
    elif key == "up":
        vid.set_volume(1.0)     #max volume
    elif key == "down":
        vid.set_volume(0.0)     #min volume - mute
        
    #draws the video to the given surface, at the given position
    #info on force draw below
    vid.draw(win, (0, 0), force_draw=False)
    
    pygame.display.update()
```
