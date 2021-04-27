# ------------------- #
#			Bible Dave Engine		 #
# ------------------- #
#-- Load imports - -#
try:
	import os, sys
	
	import pygame
	from pygame.locals import *
	from pygame import mixer
	from pygame.mixer import music
	from pgu import timer
	from pgu import engine

except ImportError, err:
	print "Could not load module! Error message:"
	print err
	sys.exit(2)
				
import base
#from base import Testing
from base import saveGame
from base import loadGame
import basegamelevel
import menu
import music
from sounds import DaveSound

from base import initLevel, initCustomLevel
from base import testLevelname

class Main(engine.Game):
	def init(self):
		pygame.init()
		
		#if '-t' in sys.argv:
		base.Testing = True #MAYO: set this to always be on !!!
		#else:
		#	base.Testing = False #Just until I find time to fix bugs caused by this being off.
		self.timer = timer.Timer(base.FPS) #Set the max FPS
		self.screenChanged = False
		
		
		self.settings = base.loadGameSettings() #Load the default game settings
		if not os.path.exists(base.path):
			base.saveGameSettings(self.settings)
			
		self.gameVariables = {}
		base.DATA = base.loadGame()
		self.playingMusic = {"jungle":False, "menu":False}
		
		self.screenMode = base.getFullScreenFlag(self.settings)
		

		self.screen = pygame.display.set_mode((base.SCREEN_WIDTH, base.SCREEN_HEIGHT),self.screenMode)
		base.SOUND = True
		self.sound = base.SOUND
		pygame.display.set_caption("Speckpater %s" % base.VERSION)
		pygame.display.set_icon(pygame.image.load(os.path.join("images","bible.png")))
		self.music = 1
		base.sound = DaveSound()
		base.initLocalization(self.settings) #Get all settings for game that are saved to the settings file

		base.setScreenMode(self.screenMode,int(self.settings['bpp'])) #Get bits per pixel (colour depth) mode from settings file and set it
		base.enableSounds(int(self.settings['sounds'])) #Get sounds from the settings file and enable them
		
		gamma = float(self.settings['gamma']) #Get gama settings from settings file
		pygame.display.set_gamma(gamma,gamma,gamma) #Set gamma
		#MAYO
		
		
		#Joystick initialization
		if (pygame.joystick.get_count() > 0): #Seems like there is a virtual joystick in some computer
			for joy_id in range(pygame.joystick.get_count()):
				base.joy = pygame.joystick.Joystick(joy_id)
				if pygame.version.vernum[0] < 2:
					# Deprecated since version 2.0.0 of pygame.
					base.joy.init()
				# Need to check whether the joystick is functional or not.
				horz_test = False
				vert_test = False
				if base.joy.get_numbuttons() < 2:
					# No point in using the joystick if it is lacking buttons.
					pass
				elif base.joy.get_numaxes() >= 2:
					horz_test = abs(base.joy.get_axis(0)) < 0.1
					vert_test = abs(base.joy.get_axis(1)) < 0.1
				else:
					pass
				
				if horz_test and vert_test:
					print "Valid Joystick Detected: #" + str(joy_id)
					base.has_joy = True
					break
				else:
					base.joy.quit()
					base.joy = None
					print
					print "Joystick #" + str(joy_id) + " has been disabled, as it appeared faulty."
					print "If the Joystick is known to be working, check if a button was being pushed down during startup."
					print "If it is still not working, please file a bug at https://github.com/TechPowerAwaits/Speckpater."
					print
			if not base.has_joy:
				print
				print "No Valid Joysticks Detected."
				print
		
		print self.settings
		print base.DATA
	
	def tick(self):
		self.timer.tick()
		
	def event(self,e):
		if e.type is QUIT:
			self.state = engine.Quit(self)
			return 1
		
		if e.type is KEYDOWN:
			if e.key == K_F2:
				if base.SOUND:
					pygame.mixer.quit()
					base.SOUND = False
				else:
					pygame.mixer.init()
					base.SOUND = True
				return 1
		
			#if e.key == K_F10:
				
				## save changes
				#if int(self.settings['fullScreen']) == 0:
					#self.settings['fullScreen'] = "1"
				#elif int(self.settings['fullScreen']) == 1:
					#self.settings['fullScreen'] = "0"
				#base.saveGameSettings(self.settings)
				#print self.settings['fullScreen']
				


#if '-t' in sys.argv:
base.Testing = True

try:
	if base.Testing == True:
		main = Main()
		base.SOUND = True
		main.run(menu.Intro(main))
	else:
		main = Main()
		main.run(menu.Intro(main))
except base.ResourceException, e:
	print e
	print base.HELP_OR_BUGS
pygame.quit()
