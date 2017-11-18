import time
import random

from pymouse import PyMouse
from pykeyboard import PyKeyboard
import datetime
import threading
#xzhsgdtc, testxzh blocked
#xzhsgdtc1, jetson, jetson1 
# TODO: Replace following two lines with the code that activate the application.


def log_out(k):
	k.tap_key('escape')
	k.tap_key('up')
	k.tap_key('return')

def log_in(k,m):
	print('start to log in')
	m.move(465,317)
	m.click(465,317)
	k.type_string('xzhsgdtc')
	k.tap_key('return')
	time.sleep(at_least(1))
	k.tap_key('return')
	time.sleep(at_least(1))
	print('enter and move mouse')

	m.move(465,377)
	print('double click')
	m.click(465,377)
	m.click(465,377)
	time.sleep(at_least(1))
	m.move(248,380)
	m.click(248,380)
	m.click(248,380)
	m.click(248,380)
	m.click(248,380)


# Log out and relog in for 10 mins 
def rest(k,m,t=600):
	log_out(k)
	time.sleep(t)
	log_in(k,m)


def add_MP(k):
	k.tap_key('l')
	time.sleep(0.1)

def add_HP(k):
	time.sleep(0.05) 
	k.tap_key('h')
	time.sleep(0.1) 

def lei(k,n):
	for i in range(n*3):
		time.sleep(0.05) 
		k.press_key('shift')
		time.sleep(0.1)
		k.release_key('shift')
		time.sleep(0.05)

def buff(k):
	time.sleep(0.05) 
	k.tap_key('7')
	time.sleep(1) 

def attack(k):
	time.sleep(0.05) 
	k.tap_key('a')
	time.sleep(0.9)

def at_least(t):
	return t*(1+random.random()/5)

def teleport(k,direction,n=1):
	for i in range(n):
		random_move(k,direction,random.choice([0.3,0.6,0.9]))
		time.sleep(0.025)
		k.press_key(direction)
		time.sleep(0.025)
		k.press_key('space')
		time.sleep(0.025)
		k.release_key('space')
		k.release_key(direction)
		time.sleep(0.38)
		

def pick_up(k):
	k.tap_key('z')

def random_move(k,direction,duration):
	k.press_key(direction)
	# k.press_key('z')
	# time.sleep(at_least(duration))
	# k.release_key('z')
	k.release_key(direction)
	if random.random() > 0.95:
		k.tap_key('command')
		time.sleep(0.3)

def range_attack(k,t=1):
	for i in range(t):
		print('go left')
		teleport(k,'left',2)

	for j in range(t):
		print('go right')
		teleport(k,'right',2)
		# add_MP(k)	


def change_chanel(k):
	time.sleep(4.5)
	k.tap_key('escape')
	k.tap_key('return')
	k.tap_key('right')
	k.tap_key('return')

def pick_everything(k,t = 1):
	k.press_key('left')
	for i in range(t*10):
		pick_up(k)
		time.sleep(0.3)
	k.release_key('left')
	time.sleep(at_least(0.05))
	k.press_key('right')
	for i in range(t*10):
		pick_up(k)
		time.sleep(0.3)
	k.release_key('right')

def repeat(key_value,interval,k = PyKeyboard(),r = True):
    print('Press key ',key_value,' ',datetime.datetime.now())
    k.tap_key(key_value)
    random_time = 0
    if r:
    	random_time = (random.random()-0.5)*0.1*interval
    threading.Timer(interval+random_time, repeat,[key_value,interval]).start()


def mage():
	# shield 
	repeat('7',50)
	
	
	# jing shen li
	repeat('8',100)

	repeat('d',0.4)
	time.sleep(0.5)

	repeat('l',70)
	repeat('o',20)


if __name__ == '__main__':
	print('Activate the application 2 seconds.')
	time.sleep(2)

	mage()

	k = PyKeyboard()
	m = PyMouse()
	k.tap_key('8')
	#rest(k,m,0.1)

	time.sleep(0.5)
	start = time.time()
	#buff(k)
	for i in range(100000):
		range_attack(k,7)
		range_attack(k,7)
		lei(k,1)

		print('add MP')
		# if i %3 != 1:
		# 	add_HP(k)
		# 	add_MP(k)

		# if i % 3== 2:
		# 	print('go to another layer ')
		# 	time.sleep(10)
		# if i % 100== 99:
		# 	print('log out and log in')
		# 	rest(k,m,t=4)
		# 	start =time.time()
		# 	buff(k)

		# if time.time() - start > 450:
		# 	buff(k)
		# 	print('sheild on',i,time)
		# 	start = time.time()
	#log_out(k)

	# test mouse


