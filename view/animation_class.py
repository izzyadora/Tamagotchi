import pygame
import os

class Animation:
    def __init__(folder_path, frame_duration):
        self.frames = []
        self.frame_duration = frame_duration
        self.current_frame = 0
        self.timer = 0

    for file in sorted(os.listdir(folder_path)):
                path = os.path.join(folder_path, file)
                image = pygame.image.load(path).convert_alpha()
                self.frames.append(image)

    def update(self, dt):
        self.timer += dt
        if self.timer >= self.frame_duration:
            self.timer = 0
            self.current_frame = (self.current_frame + 1) % len(self.frames)

    def draw(self, surface, position):
        surface.blit(self.frames[self.current_frame], position)