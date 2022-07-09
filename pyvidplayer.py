import pygame 
import os
from ffpyplayer.player import MediaPlayer
from pymediainfo import MediaInfo
from errno import ENOENT


class Video:
    def __init__(self, path):
        if not os.path.exists(path):
            raise FileNotFoundError(ENOENT, os.strerror(ENOENT), path)
        
        self.video = MediaPlayer(path)
        info = MediaInfo.parse(path).video_tracks[0]
        
        self.path = path 
        self.name = os.path.splitext(os.path.basename(path))[0]
        
        self.frame_rate = float(info.frame_rate)
        self.frame_count = int(info.frame_count)
        self.frame_delay = 1 / self.frame_rate
        self.duration = info.duration / 1000
        self.original_size = (info.width, info.height)
        
        self.active = True
        self.frame_num = 0
        self.frame_surf = None
        self.current_size = self.original_size
        
        self.alt_resize = pygame.transform.smoothscale
        
    def __del__(self):
        self.video.close_player()
        
    def restart(self):
        self.video.seek(0, relative=False)
        self.frame_num = 0
        self.frame_surf = None
        self.active = True
        
    def set_size(self, size):
        self.video.set_size(*size)
        self.current_size = size
    
    def set_volume(self, volume):
        self.video.set_volume(volume)
        
    def get_volume(self):
        return self.video.get_volume()
        
    def get_paused(self):
        return self.video.get_pause()
        
    def get_pos(self):
        return self.video.get_pts()
            
    def toggle_pause(self):
        self.video.toggle_pause()
        
    def update(self):
        updated = False
        while self.video.get_pts() > self.frame_num * self.frame_delay:
            frame, val = self.video.get_frame()
            self.frame_num += 1
            updated = True
        if updated:
            if val == "eof":
                self.active = False
            elif frame != None:
                size = frame[0].get_size()
                self.frame_surf = pygame.image.frombuffer(frame[0].to_bytearray()[0], size, "RGB")
                if size != self.current_size:
                    self.frame_surf = self.alt_resize(self.frame_surf, self.current_size)
        return updated
        
    def seek(self, seek_time):
        vid_time = self.video.get_pts()
        if vid_time + seek_time < self.duration and self.active:
            self.video.seek(seek_time)
            while vid_time + seek_time < self.frame_num * self.frame_delay:
                self.frame_num -= 1
        
    def draw(self, surf, pos, force_draw=True):
        if self.active and (self.update() or force_draw) and self.frame_surf != None:
            surf.blit(self.frame_surf, pos)
            return True
        return False