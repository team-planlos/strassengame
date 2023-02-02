## 0) Filepath----------------------------------------------------------------------------------------------------------
##    
#!/usr/bin/env pybricks-micropython



## 1) Commentation Zone-------------------------------------------------------------------------------------------------
##    
##    Author: Johannes
##    Language: Micropython (Python) v 2.0
##    Important comments: This program requires LEGO EV3 MicroPython v2.0 or higher.
##                        Garbage Collector might needed.
##    File: 
##         Program (x) 
##         Module  ( )



## 2) Import Zone-------------------------------------------------------------------------------------------------------
##    

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotic import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

import threading

import random

import time



## 3) Definition Zone---------------------------------------------------------------------------------------------------
##    

class Strassengame(EV3Brick):

    class Straße(threading.Thread):

        def __init__(self, id="default", port=Port.A, test_=False): ################################################################################################FINE
            threading.Thread.__init__(self)
            if type(port)!=String:
                self.mot=Motor(port)
            else:
                pass
            self.id=id
            self.tempo=100
            self.hinbeschleunigen={}
            self.test_=test_
            self.run_=True
            self.end_=False
            if self.test_==True:
                print("Straße ist betriebsbereit. ")

        def beschleunige_hin(self):
            if self.mot.speed>self.tempo:
                while self.mot.speed!=self.tempo:
                pass
            elif self.mot.speed<self.tempo:
                while self.mot.speed!=self.tempo:
                pass
            else:
                pass

            if self.test_==True:
                print("Neuer Term zum Hinbeschleunigen wurde erfolgreich geladen. ")
        
        def run(self): ######################################################################################################################FINE
            if self.test_==True:
                print("Thread wurde gestartet, in Kürze wird die Straße wahrscheinlich anfangen zu laufen")

            while True:
                self.run_()
                if self.end_==False:
                    continue
                elif self.end_==True:
                    break
                else:
                    pass

            if self.test_==True:
                print("Thread wurde beendet. Die Straße wird nun in diesem Thread nicht mehr laufen. ")

        def run_(self):
            while self.run_=True:
                pass

        def run_beschleuniger(self, level=0):
            if self.test_==True:
                print("Thread wurde gestartet, in Kürze wird die Straße wahrscheinlich anfangen zu laufen")

            pass

            if self.test_==True:
                print("Thread wurde beendet. Die Straße wird nun in diesem Thread nicht mehr laufen. ")

        def run_tempo(self, level=0):
            if self.test_==True:
                print("Thread wurde gestartet, in Kürze wird die Straße wahrscheinlich anfangen zu laufen")

            pass

            if self.test_==True:
                print("Thread wurde beendet. Die Straße wird nun in diesem Thread nicht mehr laufen. ")

    def __init__(self, test_=False): ######################################################################################################################FINE
        self.l=Straße(id="l", port=Port.A, test_=test_)
        self.m=Straße(id="m", port=Port.B, test_=test_)
        self.r=Straße(id="r", port=Port.C, test_=test_)
        self.beschleuniger=Straße(id="beschleuniger", port=None, test_=test_)
        self.tempo=Straße(id="tempo", port=None, test_=test_)
        self.test_=test_
        if self.test_==True:
            print("Straßengame wurde betriebsfertig gemacht. ")
    
    def sel_menu_item(self, args=[]): ######################################################################################################################FINE
        self.screen.clear()
        emph=0
        i=0
        while not (Button.CENTER in self.buttons.pressed()):
            for arg in args:
                if emph==i:
                    self.screen.draw_text(x=15, y=10+15*i, text=arg, text_color=Color.WHITE, background_color=Color.BLACK)
                else:
                    self.screen.draw_text(x=15, y=10+15*i, text=arg, text_color=Color.BLACK, background_color=Color.WHITE)
                i=i+1
            if (Button.RIGHT in self.buttons.pressed()) or (Button.DOWN in self.buttons.pressed()):
                emph=(emph+1)%5
            elif (Button.LEFT in self.buttons.pressed()) or (Button.UP in self.buttons.pressed()):
                emph=(emph-1)%5
            self.screen.clear()
        return emph

    def anleitung(self): ######################################################################################################################FINE
        texte=["Bei diesem Spiel geht es darum, mit dem Auto möglichst lange den Hindernissen auszuweichen.",
             "Das alleine wäre ja langweilig, doch währrend dem Spiel verändert sich deine Geschwindigkeit!",
             "Mit der Zeit wechselt die Geschwindigkeit öfter, schneller und zufälliger!",
             "Durch einen Druck auf die Mittlere Bricktaste kannst du das Spiel unterbrechen, durch einen zweiten Druck beenden."
             "Lenken kannst du mit dem Lenkrad, aber jetzt viel Spaß dir!"]
        emph=0
        while not (Button.CENTER in self.buttons.pressed()):
            self.screen.clear()
            self.screen.print(texte[emph])
            self.screen.print(" [Hoch/Links=Zurück, Runter/Rechts=Vor, Mitte=Ende] ")
            self.screen.print(emph +" / " +len(texte))
            if (Button.RIGHT in self.buttons.pressed()) or (Button.DOWN in self.buttons.pressed()):
                emph=(emph+1)%len(texte)
            elif (Button.LEFT in self.buttons.pressed()) or (Button.UP in self.buttons.pressed()):
                emph=(emph-1)%len(texte)

    def game(self, level=0):
        #WAS BEDEUTET WELCHES LEVEL?
        # Schwierigkeitsstufe    | Beschleunigen                                                                      | Zielgeschwindigkeit
        # Leicht(0)              | Pol vom Grad 2;              wird per randint am Anfang festgelegt, dann konstant  | Variiert alle 5 Sekunden
        # Eher Leicht(1)         | Pol vom Grad 3;              wird per randint am Anfang festgelegt, dann konstant  | Variiert alle randint(4, 8) Sekunden
        # Mittel(2)              | Pol vom Grad randint(2, 5);  Variiert alle 5 Sekunden                              | Variiert alle randint(3, 7) Sekunden
        # Eher Schwer(3)         | Pol vom Grad randint(2, 6);  Variiert alle randint(4, 8) Sek                       | Variiert alle randint(2, 6) Sekunden
        # Schwer(4)              | Pol vom Grad randint(3, 6);  Variiert alle randint(3, 7) Sek                       | Variiert alle randint(1, 5) Sekunden
        # ----------------------------------------------------------------------------------------------------------------------------------------------
        # 5 Schwierigkeiten      |  Polynomiell;                 fest/(variabel) variierend                           | (variabel) variierend              (RANDINT-variator)

        if level>=2:
            self.beschleuniger.run_beschleuniger(level=level)
        elif level=1:
            self.l.hinbeschleunigen[0]=random.randint(1, 10); self.l.hinbeschleunigen[1]=random.randint(1, 10); self.l.hinbeschleunigen[2]=random.randint(1, 10)
             self.l.hinbeschleunigen[3]=random.randint(1, 10)
            self.m.hinbeschleunigen[0]=random.randint(1, 10); self.m.hinbeschleunigen[1]=random.randint(1, 10); self.m.hinbeschleunigen[2]=random.randint(1, 10)
             self.m.hinbeschleunigen[3]=random.randint(1, 10)
            self.r.hinbeschleunigen[0]=random.randint(1, 10); self.r.hinbeschleunigen[1]=random.randint(1, 10); self.r.hinbeschleunigen[2]=random.randint(1, 10)
             self.r.hinbeschleunigen[3]=random.randint(1, 10)
        elif level=0:
            self.l.hinbeschleunigen[0]=random.randint(1, 10); self.l.hinbeschleunigen[1]=random.randint(1, 10); self.l.hinbeschleunigen[2]=random.randint(1, 10)
            self.m.hinbeschleunigen[0]=random.randint(1, 10); self.m.hinbeschleunigen[1]=random.randint(1, 10); self.m.hinbeschleunigen[2]=random.randint(1, 10)
            self.r.hinbeschleunigen[0]=random.randint(1, 10); self.r.hinbeschleunigen[1]=random.randint(1, 10); self.r.hinbeschleunigen[2]=random.randint(1, 10)
        else:
            pass
        self.l.run()
        self.r.run()
        self.m.run()
        self.beschleuniger.run_beschleuniger(level=level)
        self.tempo.run_tempo(level=level)
        global starttime=time.perf_counter()
        while not (Button.CENTER in self.buttons.pressed()):
            self.screen.clear()
            self.screen.print("Dein Score ist: " +str(int((time.perf_counter()-starttime)*100)))
            self.screen.print("[Mitte=Unterbrechung]")

    def advertisement(self):
        pass                        #optional

    def play(self): ######################################################################################################################FINE
        # Teil 1: Willkommen
        self.screen.draw_text(x=10, y=10, 
        text="Willkommen! Du willst spielen? Dann bist du hier genau richtig! Drücke den Mittleren Knopf, um fortzufahren. ")
        while not (Button.CENTER in self.buttons.pressed()):
            pass
        if self.test_=True:
            print("Teil 1 ist erfolgreich abgelaufen. ")

        # Teil 2: Menü (Anleitung, Spiel beginnen)
        opt=self.sel_menu_item(["Erst Anleitung", "Spiel sofort beginnen"])
        if self.test_=True:
            print("Teil 2 ist erfolgreich abgelaufen. ")

        # Teil 3: Anleitung bzw. Spiel beginnen
        if opt=0:
            self.anleitung()
        else:
            pass
        level=self.sel_menu_item(["Leicht", "Eher Leicht", "Mittel", "Eher Schwer", "Schwer"])

        if self.test_=True:
            print("Teil 3 ist erfolgreich abgelaufen. ")

        # Teil 4: CENTER-Abfrage und Spiel
        self.screen.draw_text(x=10, y=10, text="Viel Spaß! Drücke den Mittleren Knopf, um fortzufahren. ")
        while not (Button.CENTER in self.buttons.pressed()):
            pass
        self.screen.clear()
        wait(2000)
        if self.test_=True:
            print("self.game() wird jetzt gestartet. ")
        self.l.run()
        self.r.run()
        self.m.run()
        self.beschleuniger.run_beschleuniger(level=level)
        self.tempo.run_tempo(level=level)
        global starttime=time.perf_counter()
        while end_==False:
            while not (Button.CENTER in self.buttons.pressed()):
                self.screen.clear()
                self.screen.print("Dein Score ist: " +str(int((time.perf_counter()-starttime)*100)))
                self.screen.print("[Mitte=Unterbrechung]")
            
        if self.test_=True:
            print("Teil 4 ist erfolgreich abgelaufen. ")



## 4) Programming Zone--------------------------------------------------------------------------------------------------
##   
game=Strassengame(test_=True)
game.play()


