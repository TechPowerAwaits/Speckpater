import os
fdir = os.path.dirname(os.path.realpath(__file__))
parent_fdir = os.path.dirname(fdir)
import pygame.mixer
import sys
sys.path.append(parent_fdir)
import base

class DaveSound:
	def __init__(self):
		pygame.mixer.init(22050,8,1,2048)
		self.sounds = {}
		self.sounds['LevelExit'] = pygame.mixer.Sound(os.path.join(fdir, 'sound09.ogg'))
		self.sounds['LevelStart'] = pygame.mixer.Sound(os.path.join(fdir, 'sound08.ogg'))
		self.sounds['GameStart'] = pygame.mixer.Sound(os.path.join(fdir, 'sound01.ogg'))
		self.sounds['BiblePickup'] = pygame.mixer.Sound(os.path.join(fdir, 'sound10.ogg'))

	def Play(self, soundName):

		if not base.soundsEnabled: 
			return
		
		if (not self.sounds.has_key(soundName)):
			self.sounds[soundName] = pygame.mixer.Sound(os.path.join(fdir, soundName + ".ogg"))
			
		soundToPlay = self.sounds.get(soundName)
		
        	if (soundToPlay != None):
            		soundToPlay.play()
        	else:
            		print "Could not play sound " + soundName
