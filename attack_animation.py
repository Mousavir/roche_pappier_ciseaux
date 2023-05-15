from enum import Enum
import arcade
#commit
class AttackType(Enum):
   """
   Simple énumération pour représenter les différents types d'attaques.
   """
   ROCK = 0,
   PAPER = 1,
   SCISSORS = 2

class AttackAnimation(arcade.Sprite):
   ATTACK_SCALE = 0.50
   ANIMATION_SPEED = 5.0

def on_update(self, delta_time: float = 1 / 60):
   # Update the animation.
   self.current_texture += 1
   if self.current_texture < len(self.textures):
       self.set_texture(self.current_texture)
   else:
       self.current_texture = 0
       self.set_texture(self.current_texture)

def __init__(self, attack_type):
   super().__init__()

   self.attack_type = attack_type
   if self.attack_type == AttackType.ROCK:
       self.textures = [
           arcade.load_texture("Assets/srock.png"),
           arcade.load_texture("Assets/srock-attack.png"),
       ]
   elif self.attack_type == AttackType.PAPER:
       self.textures = [
           arcade.load_texture("Assets/spaper.png"),
           arcade.load_texture("Assets/spaper-attack.png"),
       ]
   else:
       self.textures = [
           arcade.load_texture("Assets/scissors.png"),
           arcade.load_texture("Assets/scissors-close.png"),
       ]

   self.scale = self.ATTACK_SCALE
   self.current_texture = 0
   self.set_texture(self.current_texture)



