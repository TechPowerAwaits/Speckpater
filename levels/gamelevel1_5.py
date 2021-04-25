import gamelevel1_x
from player import *
from pgu import tilevid

class GameLevel(gamelevel1_x.GameLevel):
	level_maj = 1
	level_min = 5
	levelFileName = "level1_5"
	
	def OnStart(self):
		self.cracked_branch = 0

	def OnRunSpecial1(self, g, t, a):
		pass

	def OnRunSpecial2(self, g, t, a):
		def special_hit(g, s, a):
			g.hud.add_pending_dialog(A_("\"Try jumping on the stepping stones to cross the waterfall.\""));
			s.agroups = None
		
		s = tilevid.Sprite(g.images['blank'],t.rect)
		g.sprites.append(s)
		s.agroups = g.string2groups('player')
		s.hit = special_hit

	def OnRunSpecial3(self, g, t, a):
		def special_hit(g, s, a):
			if (not g.cracked_branch):
				g.cracked_branch = 1
				g.hud.show_dialog(A_("\"Uh oh! Dave has slipped!\""));
			s.agroups = None
		
		s = tilevid.Sprite(g.images['blank'],t.rect)
		g.sprites.append(s)
		s.agroups = g.string2groups('player')
		s.hit = special_hit


	def OnExit(self):
		self.gotoNextLevel()
