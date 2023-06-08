##Rozhina Mousavi
#TP5

import random

import arcade

import game_state

#import arcade.gui

from attack_animation import AttackType, AttackAnimation

from game_state import GameState

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Roche, papier, ciseaux"
DEFAULT_LINE_HEIGHT = 45  # The default line height for text.
PLAYER_IMAGE_X = (SCREEN_WIDTH / 2) * 1.5
PLAYER_IMAGE_Y = SCREEN_HEIGHT / 2.5

COMPUTER_IMAGE_X = (SCREEN_WIDTH / 2) * 1.5
COMPUTER_IMAGE_Y = SCREEN_HEIGHT / 2.5
ATTACK_FRAME_WIDTH = 154 / 2
ATTACK_FRAME_HEIGHT = 154 / 2

class MyGame(arcade.Window):
   """
   La classe principale de l'application

   NOTE: Vous pouvez effacer les méthodes que vous n'avez pas besoin.
   Si vous en avez besoin, remplacer le mot clé "pass" par votre propre code.
   """




   def __init__(self, width, height, title):
       super().__init__(width, height, title)

       arcade.set_background_color(arcade.color.BLIZZARD_BLUE)

       self.player = None
       self.computer = None
       self.players = None
       self.rock = None
       self.paper = None
       self.scissors = None
       self.player_score = 0
       self.computer_score = 0
       self.player_attack_type = {} #dictionnaire on mouse presse , if colides with point modify player attack type to rock for example
       self.computer_attack_type = None
       self.player_attack_chosen = False
       self.player_won_round = False
       self.draw_round = None
       self.game_state = game_state.GameState.NOT_STARTED


#fonction en maine pour les objects statiques
   #1)dessiner les photos sprtes

   def setup(self):
       """
       Configurer les variables de votre jeu ici. Il faut appeler la méthode une nouvelle
       fois si vous recommencer une nouvelle partie.
       """
       # C'est ici que vous allez créer vos listes de sprites et vos sprites.
       # Prenez note que vous devriez attribuer une valeur à tous les attributs créés dans __init__

       self.game_state = game_state.GameState.ROUND_ACTIVE
       self.player = arcade.Sprite("Assets/faceBeard.png", 0.25)
       self.player.center_x = 250
       self.player.center_y = 350


       self.computer = arcade.Sprite("Assets/compy.png")
       self.computer.center_x = 655
       self.computer.center_y = 350


       self.players = arcade.SpriteList()
       self.players.append(self.player)
       self.players.append(self.computer)

       self.rock = AttackAnimation(AttackType.ROCK)
       self.rock.center_x = 90
       self.rock.center_y = 130


       self.paper = AttackAnimation(AttackType.PAPER)
       self.paper.center_x = 260
       self.paper.center_y = 135


       self.scissors = AttackAnimation(AttackType.SCISSORS)
       self.scissors.center_x =405
       self.scissors.center_y = 135

       self.computer_rock = AttackAnimation(AttackType.ROCK)
       self.computer_rock.center_x = 700
       self.computer_rock.center_y = 130

       self.computer_paper = AttackAnimation(AttackType.PAPER)
       self.computer_paper.center_x = 900
       self.computer_paper.center_y = 135

       self.computer_scissors = AttackAnimation(AttackType.SCISSORS)
       self.computer_scissors.center_x = 800
       self.computer_scissors.center_y = 135

       self.player_score = 0
       self.computer_score = 0


       self.player_attack_type = {AttackType.ROCK: False, AttackType.PAPER: False, AttackType.SCISSORS: False}
       self.computer_attack_type = {AttackType.ROCK: False, AttackType.PAPER: False, AttackType.SCISSORS: False}

       if self.computer_attack_type == AttackType.ROCK:
           self.computer_rock.center_x = 660
           self.computer_rock.center_y = 130

       if self.computer_attack_type == AttackType.PAPER:
           self.computer_paper.center_x = 660
           self.computer_paper.center_y = 140

       if self.computer_attack_type == AttackType.SCISSORS:
           self.computer_scissors.center_x = 655
           self.computer_scissors.center_y = 140

       self.player_attack_chosen = False
       self.player_won_round = False
       self.draw_round = None




   def validate_victory(self):
       """
       Utilisé pour déterminer qui obtient la victoire (ou s'il y a égalité)
       Rappel: après avoir validé la victoire, il faut changer l'état de jeu
       """

       #if game_state == GameState.ROUND_ACTIVE:

       if self.player_attack_type == AttackType.ROCK:
           if self.computer_attack_type == AttackType.ROCK:
               self.computer_score +=1

           if self.computer_attack_type == AttackType.PAPER or AttackType.SCISSORS:
               self.player_won_round = True
               self.player_score +=1


       if self.player_attack_type == AttackType.PAPER:
           if self.computer_attack_type == AttackType.PAPER:
               self.computer_score += 1

           if self.computer_attack_type == AttackType.ROCK:
               self.player_won_round = True
               self.player_score += 1

           if self.computer_attack_type == AttackType.SCISSORS:
               self.computer_score +=1


       if self.player_attack_type == AttackType.SCISSORS:

           if self.computer_attack_type == AttackType.SCISSORS:
               self.computer_score += 1

           if self.computer_attack_type == AttackType.ROCK:
               self.computer_score += 1

           if self.computer_attack_type == AttackType.PAPER:
               self.player_won_round = True
               self.player_score += 1




       self.game_state = GameState.ROUND_DONE

   def draw_possible_attack(self):
       """
       Méthode utilisée pour dessiner toutes les possibilités d'attaque du joueur
       (si aucune attaque n'a été sélectionnée, il faut dessiner les trois possibilités)
       (si une attaque a été sélectionnée, il faut dessiner cette attaque)
       """
       if self.player_attack_chosen:


           if self.player_attack_type == AttackType.ROCK:

               self.rock.draw()

           elif self.player_attack_type == AttackType.PAPER:
               self.paper.draw()

           elif self.player_attack_type == AttackType.SCISSORS:
               self.scissors.draw()

       if not (self.player_attack_chosen) and self.game_state == GameState.ROUND_ACTIVE:
           self.rock.draw()
           self.paper.draw()
           self.scissors.draw()






   def draw_computer_attack(self):
       """
       Méthode utilisée pour dessiner les possibilités d'attaque de l'ordinateur
       """
       #if (self.player_attack_chosen):
       if self.computer_attack_type == AttackType.ROCK:

           self.computer_rock.draw()

       elif self.computer_attack_type == AttackType.PAPER:
           self.computer_paper.draw()

       elif self.computer_attack_type == AttackType.SCISSORS:
           self.computer_scissors.draw()

       #if not (self.player_attack_chosen) and game_state == GameState.ROUND_ACTIVE:

           #self.computer_attack_type.draw()

       self.rectangle_outline = (ATTACK_FRAME_WIDTH, ATTACK_FRAME_HEIGHT,)

       arcade.draw_rectangle_outline()


   def draw_scores(self):
       """
       Montrer les scores du joueur et de l'ordinateur
       """
       arcade.draw_text("Le pointage du jouer est " + str(self.player_score) + ".",50,70,arcade.color.GIANTS_ORANGE, 16)
       arcade.draw_text("Le pointage de l'ordinateur est " + str(self.computer_score) + ".",600, 70,arcade.color.GIANTS_ORANGE, 16)


       if self.game_state == GameState.ROUND_DONE:
           if self.player_won_round == True:

               arcade.draw_text("Vous avez gagné la partie! La partie est terminée!", 300, 160, arcade.color.GIANTS_ORANGE, 16)
           else:
               arcade.draw_text("L'ordinateur a gagné la partie!", 300, 160, arcade.color.GIANTS_ORANGE, 16)



   def draw_instructions(self):
       """
       Dépendemment de l'état de jeu, afficher les instructions d'utilisation au joueur (appuyer sur espace, ou sur une image)
       """


       if self.game_state ==GameState.NOT_STARTED:
           arcade.draw_text("Appuyer sur une image pour faire une attaque!",300,140,arcade.color.GIANTS_ORANGE, 16)

       if self.game_state == GameState.ROUND_DONE:
           arcade.draw_text("Appuyer sur 'ESPACE' pour commencer une nouvelle ronde!",300,140, arcade.color.GIANTS_ORANGE, 16)

       #le game state qui est game over est definit dans la methode on_update() d'apres qui a gagne
       if self.game_state == game_state.GameState.GAME_OVER:
           arcade.draw_text("Appuyer sur 'ESPACE' pour commencer une nouvelle ronde!", 300, 140, arcade.color.GIANTS_ORANGE, 16)



   def on_draw(self): #s'assurer ont est dans quelle état de jeu if game_state = round...
       """
       C'est la méthode que Arcade invoque à chaque "frame" pour afficher les éléments
       de votre jeu à l'écran.
       """

       # Cette commande permet d'effacer l'écran avant de dessiner. Elle va dessiner l'arrière
       # plan selon la couleur spécifié avec la méthode "set_background_color".
       arcade.start_render()

       # Display title
       arcade.draw_text(SCREEN_TITLE,0,SCREEN_HEIGHT - DEFAULT_LINE_HEIGHT * 2,arcade.color.BRIGHT_PINK, 40, width=SCREEN_WIDTH, align="center")

       self.draw_instructions()
       self.players.draw()
       self.draw_possible_attack()
       self.draw_scores()

       #afficher l'attaque de l'ordinateur selon l'état de jeu
       #afficher le résultat de la partie si l'ordinateur a joué (ROUND_DONE)



   def on_update(self, delta_time):
       """
       Toute la logique pour déplacer les objets de votre jeu et de
       simuler sa logique vont ici. Normalement, c'est ici que
       vous allez invoquer la méthode "update()" sur vos listes de sprites.
       Paramètre:
           - delta_time : le nombre de milliseconde depuis le dernier update.

       """
       if not(self.player_attack_chosen) and self.game_state == GameState.ROUND_ACTIVE:
           # d'apres la methode on_update dans attack_animation
           self.rock.on_update()
           self.paper.on_update()
           self.scissors.on_update()

       if self.player_attack_chosen and self.game_state == GameState.ROUND_ACTIVE:
           pc_attack = random.randint(0,2)
           if pc_attack == 0:
               self.computer_attack_type == AttackType.ROCK
           elif pc_attack == 1:
               self.computer_attack_type = AttackType.PAPER

           else:
               self.computer_attack_type = AttackType.SCISSORS


           self.validate_victory()


       #if self.game_state == GameState.ROUND_DONE:
            #self.reset_round()

       if self.player_score ==3 or self.computer_score ==3:
            self.game_state = GameState.GAME_OVER







   def on_key_press(self, key, key_modifiers):
       """
       Cette méthode est invoquée à chaque fois que l'usager tape une touche
       sur le clavier.
       Paramètres:
           - key: la touche enfoncée
           - key_modifiers: est-ce que l'usager appuie sur "shift" ou "ctrl" ?

       Pour connaître la liste des touches possibles:
       http://arcade.academy/arcade.key.html
       """
       if (self.game_state == GameState.NOT_STARTED and key == arcade.key.SPACE):
           self.game_state = GameState.ROUND_ACTIVE

       if (self.game_state == GameState.ROUND_DONE and key == arcade.key.SPACE):
           self.game_state = GameState.ROUND_ACTIVE
           self.reset_round()

       if (self.game_state == GameState.GAME_OVER and key == arcade.key.SPACE):
           self.setup()




   def reset_round(self):
       """
       Réinitialiser les variables qui ont été modifiées
       """
       self.computer_attack_type = -1
       self.player_attack_chosen = False
       self.player_attack_type = {AttackType.ROCK: False, AttackType.PAPER: False, AttackType.SCISSORS: False}
       self.player_won_round = False
       self.draw_round = False



   def on_mouse_press(self, x, y, button, key_modifiers): #sprite
       """
       Méthode invoquée lorsque l'usager clique un bouton de la souris.
       Paramètres:
           - x, y: coordonnées où le bouton a été cliqué
           - button: le bouton de la souris appuyé
           - key_modifiers: est-ce que l'usager appuie sur "shift" ou "ctrl" ?
       """

       #definir quel type est le attack type du player qu'il choisit d'apres son clique sur l'ecran
       #changer le attack_type change automatiquement la valeur de ce variable AttackType a True. Ce valeur de True est utilise dans la method on_update() pour les etapes suivants

       if self.rock.collides_with_point((x,y)):
           self.player_attack_type = AttackType.ROCK
           self.player_attack_chosen = True


       if self.paper.collides_with_point((x,y)):
           self.player_attack_type = AttackType.PAPER
           self.player_attack_chosen = True

       if self.scissors.collides_with_point((x,y)):
           self.player_attack_type = AttackType.SCISSORS
           self.player_attack_chosen = True




       # Test de collision pour le type d'attaque (self.player_attack_type).
       # Rappel que si le joueur choisi une attaque, self.player_attack_chosen = True



def main():
   """ Main method """
   game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
   game.setup()
   arcade.run()


if __name__ == "__main__":
   main()