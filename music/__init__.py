import os
fdir = os.path.dirname(os.path.realpath(__file__))
parent_fdir = os.path.dirname(fdir)
import pygame.mixer
import sys
sys.path.append(parent_fdir)
import base
from pygame.locals import *
from pgu import engine
from pgu import gui

pygame.mixer.init()
global Music
Music = {"Menu":None, "Jungle":None, "Cave":None, "JumpJungle":None, "Mountain":None, "Temple":None, "Finale":None}


def LoadMusic():
	if base.SOUND == True:
		if base.MUSIC_LOADED == False:
			Music["Menu"] = pygame.mixer.Sound(os.path.join(fdir, 'bgmusic.ogg'))
			Music["Jungle"] = pygame.mixer.Sound(os.path.join(fdir, 'jungle.ogg'))
			Music["Cave"] = pygame.mixer.Sound(os.path.join(fdir, 'cave.ogg'))
			Music["JumpJungle"] = pygame.mixer.Sound(os.path.join(fdir, 'jungle_jumping.ogg'))
			Music["Mountain"] = pygame.mixer.Sound(os.path.join(fdir, 'mountain.ogg'))
			Music["Temple"] = pygame.mixer.Sound(os.path.join(fdir, 'temple.ogg'))
			Music["Finale"] = pygame.mixer.Sound(os.path.join(fdir, 'finale.ogg'))
			base.MUSIC_LOADED = True

def Play(category):
	if base.SOUND == True:
		if base.MUSIC_LOADED == True:
				Music[category].play(-1)

def Stop(category):
	if base.SOUND == True:
		if base.MUSIC_LOADED == True:
				Music[category].fadeout(1800)
