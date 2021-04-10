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
Music = {"MenuMusic":None, "JungleMusic":None, "CaveMusic":None, "MountainMusic":None, "TempleMusic":None}


def LoadMusic():
	if base.SOUND == True:
		if base.MUSIC_LOADED == False:
			Music["MenuMusic"] = pygame.mixer.Sound(os.path.join(fdir, 'bgmusic.ogg'))
			Music["JungleMusic"] = pygame.mixer.Sound(os.path.join(fdir, 'jungle.ogg'))
			Music["CaveMusic"] = pygame.mixer.Sound(os.path.join(fdir, 'cave.ogg'))
			Music["MountainMusic"] = pygame.mixer.Sound(os.path.join(fdir, 'mountain.ogg'))
			Music["TempleMusic"] = pygame.mixer.Sound(os.path.join(fdir, 'temple.ogg'))
			base.MUSIC_LOADED = True

def Play(category):
	if base.SOUND == True:
		if base.MUSIC_LOADED == True:
				Music[category].play(-1)

def Stop(category):
	if base.SOUND == True:
		if base.MUSIC_LOADED == True:
				Music[category].fadeout(1800)
