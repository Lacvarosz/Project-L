from typing import Self
from pygame import Surface

class Animation:
    def __init__(self, images :list[Surface], img_dur :int = 5, loop :bool = True) -> None:
        self.images = images
        self.loop = loop
        self.img_duration = img_dur
        self.done = False
        self.frame = 0
        
    def copy(self) -> Self:
        return Animation(self.images, self.img_duration, self.loop)
    
    def img(self) -> Surface:
        return self.images[int(self.frame / self.img_duration)]
    
    def update(self) -> None:
        if self.loop:
            self.frame = (self.frame + 1) % (self.img_duration * len(self.images))
        else:
            self.frame = min(self.frame + 1, self.img_duration * len(self.images) - 1)
            if self.frame >= self.img_duration * len(self.images) - 1:
                self.done = True