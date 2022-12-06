# pyvidplayer
An extremely easy to use module that plays videos on Pygame. 

BaralTech has a good tutorial ---> https://www.youtube.com/watch?v=Xu8SLkvFq8I&ab_channel=BaralTech

# updated once again!
There was an egregious bug that prevented ```active``` from turning false on some videos, which I barely fixed.
Playing videos in Python is just very janky but hopefully this script can serve you well.

Changes:
- fixed (hopefully) the ```active``` bug
- changed some variables to internal use
- added back the close function
- added typing hints
- added seperate pause and resume functions
- significantly reduced console output (although unfortunately there's still some)

notice: Try to save the issues tab for genuine bugs with the script. If you just have a question, you can email me at anrayliu@gmail.com

# **Example**
```
import pygame
from pyvidplayer import Video

pygame.init()
win = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

#provide video class with the path to your video
vid = Video("vid.mp4")

while True:
    key = None
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            vid.close()
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            key = pygame.key.name(event.key)
    
    #your program frame rate does not affect video playback
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
        vid.set_volume(0.0)     #min volume
        
    #draws the video to the given surface, at the given position
    vid.draw(win, (0, 0), force_draw=False)
    
    pygame.display.update()
```

# Properties
The video class now has a bunch of new properties
- ```path```
- ```name```
- ```frame_count```
- ```frame_rate```
- ```duration```
- ```original_size```
- ```current_size```
- ```active``` - becomes false when the video finishes playing
- ```frame_surf``` - current video frame as a pygame surface 
- ```alt_resize``` - fallback resizing function in case the usual one fails. by default this is
                     ```pygame.transform.smoothscale```, which is a bit cpu intensive, so you can switch it
                     to ```pygame.transform.scale``` if you don't mind the video looking uglier
                     
# Functions
- ```restart()```
- ```set_size(size)``` - resizes the video with ffpyplayer's resize function. This is a lot 
                         lighter on the cpu than the fallback function, but it sometimes doesn't work
- ```set_volume(volume)``` - from 0.0 to 1.0
- ```get_volume()```
- ```toggle_pause()```
- ```get_paused()```
- ```pause()```
- ```resume()```
- ```close()``` - releases video resources
- ```get_pos()```          - returns the current time in the video in seconds
- ```seek(time)``` - moves forwards or backwards by time in seconds in the video.
                   Note that when seeking backwards, the video will temporaily freeze. This seems to 
                   be an issue with ffpyplayer, and I can't fix it (trust me I tried)
- ```draw(surf, pos, force_draw=True)``` - draws the current video frame onto the given surface at the given position. If
                                          ```force_draw``` is enabled, a surface will be drawn every time draw is called. If it's
                                          disabled, a surface will only be drawn when a new frame from the video is made which saves cpu
