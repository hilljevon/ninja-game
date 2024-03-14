import pygame

class PhysicsEntity:
    # game is Game.self class, e_type is 'player', position is a coordinate, and size is the size of player? 
    def __init__(self, game ,e_type, pos, size) -> None:
        self.game = game 
        self.type = e_type
        self.pos = list(pos)
        self.size = size 
        # self.velocity represents the velocity that player is already traveling at
        self.velocity = [0, 0]

    def update(self, movement=(0,0)):
        # frame movement adds a current movement vector to the already existing player vector
        frame_movement = (movement[0] + self.velocity[0], movement[1] + self.velocity[1])
        # we adjust the player's position to whatever the new movement becomes
        self.pos[0] += frame_movement[0]
        self.pos[1] += frame_movement[1]
    def render(self, surf):
        surf.blit(self.game.assets['player'], self.pos)