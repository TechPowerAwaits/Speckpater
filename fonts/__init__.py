import pygame.font
pygame.font.init()
fdir = os.path.dirname(os.path.realpath(__file__))

global font_objects
font_objects = {}
FONT_DICT = 
{"COPR": ["BD_Cartoon_Shout.ttf", 10],
{"MENU_BUTTON": ["BD_Cartoon_Shout.ttf", 26]},
{"INTRO_SMALL": ["BD_Cartoon_Shout.ttf", 26]},
{"INTRO_LARGE": ["BD_Cartoon_Shout.ttf", 40]},
{"SETTINGS": ["BD_Cartoon_Shout.ttf", 26]},
{"SELECTION": ["BD_Cartoon_Shout.ttf", 26]},
{"ABOUT": ["BD_Cartoon_Shout.ttf", 15]},
{"CONTROL_CAPTION": ["BD_Cartoon_Shout.ttf", 26]},
{"CREDITS": ["BD_Cartoon_Shout.ttf", 15]},
{"HELP": ["BD_Cartoon_Shout.ttf", 15]},
{"GAME_FINISH": ["BD_Cartoon_Shout.ttf", 30]},
{"HUD_HEALTH": ["SF Comic Script.ttf", 10]},
{"HUD_BIBLE_VAL": ["SF Comic Script", 28]},
{"HUD_BANANA_VAL": ["SF Comic Script", 28]},
{"HUD": ["SF Comic Script", 24]}
}
FONT_FILENAME = "SF Comic Script.ttf"

def get(font_cat):
	font_name = FONT_DICT[font_cat][0]
	font_size = FONT_DICT[font_cat][1]
	font_id = font_name + "-" + str(font_size)
	if not font_objects.has_key(font_id):
		font_objects[font_id] = pygame.font.Font(os.path.join(fdir,
		font_name), font_size)
	return font_objects[font_id]

def blitText(size,color, text, pos, shaOff = None):
		font = pygame.font.Font(FONT_FILENAME, size)
		
		if shaOff != None:
				txt = font.render(text, True, (0,0,0))
				screen.blit(txt, (pos[0] + shaOff[0],pos[1] + shaOff[1]))
		
		txt = font.render(text, True, color)
		screen.blit(txt, pos)

# This function is used by the HUD to determine when a line is too long, and when it should split.
def getTextRenderWidth(fontsize, message):
    font = pygame.font.Font(FONT_FILENAME, fontsize)    
    txt = font.render(message, True, (0,0,0))
    return txt.get_width()
