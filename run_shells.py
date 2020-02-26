#!/usr/bin/python

import os
import sys

def separate_line():
	global TERMINAL_SIZE
	print('-' * TERMINAL_SIZE.columns)

def debug(variable):
	print('debug:', variable)

def int_list(given_list):
	result = []
	for element in given_list:
		result.append(int(element))
	return result


HOME = '/home/bruce'
DIRECTORY_PATH = f'{HOME}/coding/scripts'
TERMINAL_SIZE = os.get_terminal_size()

os.chdir(DIRECTORY_PATH)
scripts = os.listdir()

for index, script in enumerate(scripts):
	print(f'[{index}] - {script}')

separate_line()
indexs_to_run = int_list(input(
	"Which of them you wanna run?\n--> ") \
	.replace(',',' ') \
	.split())

for index in indexs_to_run:
	os.system(f'sh {scripts[index]}')

""" default run
sh touchpad.sh
sh keyboard.sh
sh xflux.sh
sh set-background.sh
"""

