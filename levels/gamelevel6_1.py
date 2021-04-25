import gamelevel6_x
from player import *
from pgu import tilevid
import os, sys
from human import Villager
from random import randrange

# don't set the tileset yet
#from tilesets.templetiles import Tileset
from tilesets.commontiles import Tileset

end_game = True
class GameLevel(gamelevel6_x.GameLevel):
	levelFileName = "kilopowa"
	level_min = 1
	
	villagersPraising = False
	
	def OnStart(self):
		self.skip = False
		if base.num_bibles < base.NEEDED_BIBLES:
			self.hud.show_dialog(A_("""Oh no! You only have %d Bibles! You need at least %d total! Dave now has to back track and pick up more Bibles!""" % (base.num_bibles, base.NEEDED_BIBLES)))
			
			base.NEED_MORE_BIBLES = True
		else:
			base.NEED_MORE_BIBLES = False
			
		
	def OnLoop(self):
		pass
	
	def OnRunSpecial1(self, g, t, a):
		s = tilevid.Sprite(g.images['hut1'],t.rect)
		g.sprites.append(s)
		
	def OnRunSpecial2(self, g, t, a):
		s = Villager(g, t.rect)
		g.sprites.append(s)
		
	def OnRunSpecial3(self, g, t, a):
		s = tilevid.Sprite(g.images['cauldron'],t.rect)
		g.sprites.append(s)
		
	def OnRunSpecial4(self, g, t, a):
		pass
		
	def OnRunSpecial5(self, g, t, a):
		def trigger(g, s, a):
			g.hud.show_dialog(A_("\"Aah there, I can see it, the Kilapowa village!\nPraise the Lord, I'm on time!!\""))
			s.agroups = None	## Remove the groups from colliding with this object in the future	

		self.addTriggerCallback(t.rect,trigger)
		
	def OnRunSpecial6(self, g, t, a):
		def trigger(g, s, a):
			s.agroups = None	## Remove the groups from colliding with this object in the future	

		self.addTriggerCallback(t.rect,trigger)

	def OnRunSpecial7(self, g, t, a):
		def trigger(g, s, a):
			s.agroups = None ## Remove the groups from colliding with this object in the future
			self.skip = True
			

		self.addTriggerCallback(t.rect,trigger)
			
	def OnRunSpecial8(self, g, t, a):
		def trigger(g, s, a):
			s.agroups = None	## Remove the groups from colliding with this object in the future	
		
			g.hud.add_pending_dialog(A_(""""""))

		self.addTriggerCallback(t.rect,trigger)

	def OnExit(self):
		if base.NEED_MORE_BIBLES == True:
			base.DATA["chapter"] = randrange(1,5)
			base.DATA["level"] = randrange(1,2) - 1
			self.nextState = base.NEXTLEVEL
		else:
			if self.skip == True:
				self.nextState = base.SHOWGAMEOVER
		
	def loadLevelImages(self):
		gamelevel6_x.GameLevel.loadLevelImages(self)
		self.load_images(self.idata2)

	idata2 = [
		('blank',os.path.join('images', 'blank.png'), (0, 0, 32, 32)),
		('bible',os.path.join('images', 'bible.png'), (0, 0, 32, 32)),
		('hut1', os.path.join('images', 'hut.gif'), (0, 0, 130, 104)),
		('cauldron', os.path.join('images', 'cauldron.png'), (0, 0, 130, 52)),
		('villager_1', os.path.join('images', 'villager_1.png'), (0, 0, 32, 48)),
		('villager_2', os.path.join('images', 'villager_2.png'), (0, 0, 32, 48)),
		('villager_3', os.path.join('images', 'villager_3.png'), (0, 0, 32, 48)),
		('villager_4', os.path.join('images', 'villager_4.png'), (0, 0, 32, 48)),
		('villager_5', os.path.join('images', 'villager_5.png'), (0, 0, 32, 48)),
	]
