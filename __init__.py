import ugfx
import badge
import random
import time
import appglue

click_text = '*Click*'
lost_text = 'You lost!'
big_font = 'Roboto_BlackItalic24'
round = 0 # Which round is going on
bullet = 0 # Where is the bullet

def fire_button(pressed, bullet):
	global round
	if pressed:
		round += 1
		fire_gun(round, bullet)

def reset_game():
	global round, bullet
	ugfx.clear(ugfx.WHITE)
	ugfx.flush()
	round = 0
	bullet = random.randint(1, 6)
	bullet = random.randint(1, 6)
	print_start()

def print_start():
	ugfx.clear(ugfx.WHITE)
	badge.png(0, 0, '/lib/russian_roulette_9000/gun.png')
	ugfx.string(5, 45, str('Start to pull the trigger'), "Roboto_BlackItalic22", ugfx.BLACK)
	ugfx.flush()

def fire_gun(round, bullet):
	print(str('round ') + str(round) + str(' vs ') + str(bullet))
	if bullet == round:
		ugfx.clear(ugfx.WHITE)
		badge.png(0, 0, '/lib/russian_roulette_9000/shot.png')
		ugfx.flush()
		time.sleep(4.0)
		ugfx.clear(ugfx.WHITE)
		ugfx.string(0, 30, lost_text, big_font, ugfx.BLACK)
		ugfx.flush()
		time.sleep(4.0)
		reset_game()
	else:
		ugfx.clear(ugfx.WHITE)
		ugfx.string(10, 20, click_text, big_font, ugfx.BLACK)
		ugfx.flush()
		time.sleep(1.0)
		print_start()

badge.init()
ugfx.init()
ugfx.input_init()
ugfx.input_attach(ugfx.BTN_START, lambda pressed: fire_button(pressed, bullet))
ugfx.input_attach(ugfx.BTN_B, lambda pressed: appglue.home())
reset_game()
