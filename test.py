import time
import pykeyboard
import random
# TODO: Replace following two lines with the code that activate the application.
print('Activate the application 3 seconds.')
time.sleep(3)

#account testxzh 
#xzhsgdtc1
#Jetson
def add_MP(k):
	time.sleep(0.05) 
	k.tap_key('l')
	time.sleep(0.05) 

def add_HP(k):
	time.sleep(0.05) 
	k.tap_key('h')
	time.sleep(0.05) 

def blast(k):
	time.sleep(0.05) 
	k.tap_key('shift')
	time.sleep(0.05) 

def attack(k):
	time.sleep(0.05) 
	k.tap_key('a')
	time.sleep(0.05) 

def pick_up_attact_sleep(k,t=1):
	interval = 1 * (1 + random.random())
	for i in range(int(t/interval)):
		k.tap_key('a')
		time.sleep(interval)
		k.tap_key('z')


def move_left(k,d=3):
	k.press_key('left')
	pick_up_attact_sleep(k,d)
	k.release_key('Left')

def move_right(k,d=3):
	k.press_key('right')
	pick_up_attact_sleep(k,d)
	k.release_key('right')

def pick_up(k):
	k.tap_key('z')

def change_chanel(k):
	time.sleep(4)
	k.tap_key('escape')
	k.tap_key('return')
	k.tap_key('right')
	k.tap_key('return')



k = pykeyboard.PyKeyboard()

for i in range(10000):
	# move_right(k,25)
	# move_left(k,25)
	time.sleep(60)
	if i % 10== 9:
		change_chanel(k)
	# if i % 50 == 40:
	# 	k.tap_key('j')


