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
alias = {}
current = None
loaded = False
enabled = False

def Load():
	global alias
	global current
	global loaded
	if enabled == True:
		if loaded == False:
			alias["Menu"] = os.path.join(fdir, 'bgmusic.ogg')
			alias["Jungle"] = os.path.join(fdir, 'jungle.ogg')
			alias["Cave"] = os.path.join(fdir, 'cave.ogg')
			alias["JumpJungle"] = os.path.join(fdir, 'jungle_jumping.ogg')
			alias["Mountain"] = os.path.join(fdir, 'mountain.ogg')
			alias["Temple"] = os.path.join(fdir, 'temple.ogg')
			alias["Finale"] = os.path.join(fdir, 'finale.ogg')
			loaded = True

def Play(song_alias):
	global alias
	global current
	global loaded
	if enabled == True:
		if loaded == True:
			if pygame.mixer.music.get_busy():
				pygame.mixer.music.fadeout(1800)
			pygame.mixer.music.load(alias[song_alias])
			pygame.mixer.music.play(-1)
			current = song_alias
