##Rozhina Mousavi
#TP5

import random

import arcade

import game_state

#import arcade.gui

#appel au fichier attack_animation et game_state et leur contenu
from attack_animation import AttackType, AttackAnimation

from game_state import GameState

#mesures de l'ecran, des frames, du size du player et du computer
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

#la classe prinicpale du jeu roche papier sciseaux qui contient tout les etapes, validation, animations du jeu roche papier scisseaux
class MyGame(arcade.Window):
   """
   La classe principale de l'application

   NOTE: Vous pouvez effacer les méthodes que vous n'avez pas besoin.
   Si vous en avez besoin, remplacer le mot clé "pass" par votre propre code.
   """



    #creer les variable du jeu
   def __init__(self, width, height, title):
       super().__init__(width, height, title)

       arcade.set_background_color(arcade.color.BLIZZARD_BLUE)

       self.player = None
       self.computer = None
       self.players = None
       self.rock = None
       self.paper = None
       self.scissors = None
       self.computer_rock = None
       self.computer_paper = None
       self.computer_scissors = None
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

    #definir les variables crer en init et donner les coordones des sprites
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
       self.computer_rock.center_x = 655
       self.computer_rock.center_y = 130

       self.computer_paper = AttackAnimation(AttackType.PAPER)
       self.computer_paper.center_x = 655
       self.computer_paper.center_y = 135

       self.computer_scissors = AttackAnimation(AttackType.SCISSORS)
       self.computer_scissors.center_x = 655
       self.computer_scissors.center_y = 135

       self.player_score = 0
       self.computer_score = 0


       self.player_attack_type = {AttackType.ROCK: False, AttackType.PAPER: False, AttackType.SCISSORS: False}
       self.computer_attack_type = {AttackType.ROCK: False, AttackType.PAPER: False, AttackType.SCISSORS: False}



       self.player_attack_chosen = False
       self.player_won_round = False
       self.equal = False
       self.draw_round = None



#valider la victoire, donc dans chaque jeu entre le player et l'ordinateur  verifier qui gagne d'après les attack type du player et de l'ordinateur. egalement augmenter la score base sur les regeles du jeu
   def validate_victory(self):
       """
       Utilisé pour déterminer qui obtient la victoire (ou s'il y a égalité)
       Rappel: après avoir validé la victoire, il faut changer l'état de jeu
       """

       #if game_state == GameState.ROUND_ACTIVE:

       if self.player_attack_type == AttackType.ROCK:
           if self.computer_attack_type == AttackType.ROCK:
               self.reset_round()
               self.equal = True

           if self.computer_attack_type == AttackType.PAPER or AttackType.SCISSORS:
               self.player_won_round = True
               self.player_score +=1


       if self.player_attack_type == AttackType.PAPER:
           if self.computer_attack_type == AttackType.PAPER:
               self.reset_round()
               self.equal = True

           if self.computer_attack_type == AttackType.ROCK:
               self.player_won_round = True
               self.player_score += 1

           if self.computer_attack_type == AttackType.SCISSORS:
               self.computer_score +=1


       if self.player_attack_type == AttackType.SCISSORS:

           if self.computer_attack_type == AttackType.SCISSORS:
               self.reset_round()
               self.equal = True

           if self.computer_attack_type == AttackType.ROCK:
               self.computer_score += 1

           if self.computer_attack_type == AttackType.PAPER:
               self.player_won_round = True
               self.player_score += 1



        #chnger l'état de jeu a round done
       self.game_state = GameState.ROUND_DONE

#dessiner le ou les sprites du attack type du player dependament de si le player a choisit une attack et y dessiner les frames
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

       arcade.draw_rectangle_outline(90,130, ATTACK_FRAME_WIDTH, ATTACK_FRAME_HEIGHT,arcade.color.RED)
       arcade.draw_rectangle_outline(260, 135, ATTACK_FRAME_WIDTH, ATTACK_FRAME_HEIGHT, arcade.color.RED)
       arcade.draw_rectangle_outline(405, 135, ATTACK_FRAME_WIDTH, ATTACK_FRAME_HEIGHT, arcade.color.RED)







#dessiner l'attack de l'ordinateur qui se fait au hasard dans la methode on_update() si le player a choisit une attack. egalement dessiner le frame du attack de l'ordinateur
   def draw_computer_attack(self):
       """
       Méthode utilisée pour dessiner les possibilités d'attaque de l'ordinateur
       """
       #if (self.player_attack_chosen):
       if self.player_attack_chosen:
           if self.computer_attack_type == AttackType.ROCK:

               self.computer_rock.draw()

           elif self.computer_attack_type == AttackType.PAPER:

               self.computer_paper.draw()

           elif self.computer_attack_type == AttackType.SCISSORS:

               self.computer_scissors.draw()


           arcade.draw_rectangle_outline(650, 135, ATTACK_FRAME_WIDTH, ATTACK_FRAME_HEIGHT, arcade.color.RED)


#dessiner le pointage de l'ordinateur et du joueur. le score chnage egalement d'après la methode validate victory
#dessiner egalement celui qui a gange la partie (ordinateur, player ou egalite)
   def draw_scores(self):
       """
       Montrer les scores du joueur et de l'ordinateur
       """
       arcade.draw_text("Le pointage du joueur est " + str(self.player_score) + ".",50,70,arcade.color.GIANTS_ORANGE, 16)
       arcade.draw_text("Le pointage de l'ordinateur est " + str(self.computer_score) + ".",600, 70,arcade.color.GIANTS_ORANGE, 16)


       if self.game_state == GameState.ROUND_DONE:
           if self.player_won_round == True:

               arcade.draw_text("Vous avez gagné la partie! La partie est terminée!", 280,470, arcade.color.PURPLE, 16)

           elif self.equal == True:
               arcade.draw_text("Égalité!", 280,470, arcade.color.PURPLE, 16)
           else:
               arcade.draw_text("L'ordinateur a gagné la partie!", 280,470, arcade.color.PURPLE, 16)


#afficher les instructions pour orienter le jouer pour quoi faire dependament de l'état du jeu
   def draw_instructions(self):
       """
       Dépendemment de l'état de jeu, afficher les instructions d'utilisation au joueur (appuyer sur espace, ou sur une image)
       """


       if self.game_state == GameState.ROUND_ACTIVE:
           arcade.draw_text("Appuyer sur une image pour faire une attaque!",280,470,arcade.color.GIANTS_ORANGE, 16)

       elif self.game_state == GameState.ROUND_DONE:
           arcade.draw_text("Appuyer sur 'ESPACE' pour commencer une nouvelle ronde!",280,445, arcade.color.PURPLE, 16)

       #le game state qui est game over est definit dans la methode on_update() d'apres qui a gagne

       #si le jeu est terminer dessiner celui qui a gagne le jeu d'après celui qui a le score de 3 et egalement instructer sur comment proceder pour jouer un nouveau jeu
       elif self.game_state == game_state.GameState.GAME_OVER:
           if self.player_score ==3:
               arcade.draw_text("Vous avez gagné le jeu!",280,470, arcade.color.PURPLE, 16)

           if self.computer_score ==3:
               arcade.draw_text("L'ordinateur a gagné le jeu!",280,470, arcade.color.PURPLE, 16)

           arcade.draw_text("Appuyer sur 'ESPACE' pour commencer un nouveau jeu!", 280,445, arcade.color.PURPLE, 16)


#methode on_draw() qui permet de preparer l'ecran pour les dessinset qui permet de dessiner le screen title et les autres methodes de dessinage definit plus haut
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
       self.draw_computer_attack()
       self.draw_scores()

       #afficher l'attaque de l'ordinateur selon l'état de jeu
       #afficher le résultat de la partie si l'ordinateur a joué (ROUND_DONE)


#methode on_update() qui permet de update les sprite si aucun attack a été choisit et qu'on est dans un etat de jeu active
#methode on update() qui permet egalement de definir le sprite attack type de l'ordinateur au hasard dependament de si le joueur a choisit une attack
   #valider egalement la victoire  et chnager l'état de jeu a game over d'après si l'ordinateur ou le player a atteint un score de 3
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






#si le clavier boutton espace est pese et dependament de l'état de danslequel on est changer l'état de jeu ou remmetre le jeu a neuf avec les variable de depart
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


#methode qui permet de remetre les variables chnageable dans le jeu a leur etat initial

   def reset_round(self):
       """
       Réinitialiser les variables qui ont été modifiées
       """
       self.computer_attack_type = -1
       self.player_attack_chosen = False
       self.player_attack_type = {AttackType.ROCK: False, AttackType.PAPER: False, AttackType.SCISSORS: False}
       self.player_won_round = False
       self.draw_round = False


#methode qui permet de determiner si il y a une colision entre le boutton du souris et un sprite. Ceci permet de determiner le attack type que choisit (attack_chosen) le player
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


#fonction main pour executer le jeu mygame lors de son appel
def main():
   """ Main method """
   game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
   game.setup()
   arcade.run()

#appel au fonction main
if __name__ == "__main__":
   main()