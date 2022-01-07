# pyvidplayer
An extremely easy to use module that plays videos on Pygame

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
            vid.close()
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

**Features**:
  - Standard video playing features such as seeking and pausing
  - Internal clock plays video at the right pace regardless of your program's fps
    (try changing the ```clock.tick()``` values in the above example and see for yourself)
  - Uses Pygame surfaces for more user control
  - Minimal cpu usage 
    (on my machine, max optimization used less than 10%, min used 20%,
    and a practical approach used around 12%)
  - Add a video to your game in just 3 lines of code
    
**Other Stuff**
- ```get_file_data()``` returns a bunch of information regarding the video file, such as frame count, duration, size, etc
- ```get_playback_data()``` returns information regarding the video class itself, such as it's volume, pause state, etc
- For ```draw()```, the ```force_draw``` parameter is defaulted to ```True```. That means that everytime the method is called, the current
video frame will be drawn. When ```force_draw``` is turned off, ```draw()``` will only draw something when there is a new frame in the video. 
Otherwise, it draws nothing. This is nice to save cpu, as you don't need to keep drawing the same frame over and over again. However, there will be a lot of
flickering if stuff is drawn above or below the frame, which is why ```force_draw``` is defaulted to ```True```
- Seeking backwards is a lot slower than seeking forwards
- ```video.active``` will become ```False``` when the video finishes playing
