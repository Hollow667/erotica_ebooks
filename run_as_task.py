#!/usr/bin/python3.6
# -*- coding: utf-8 -*-

import logging
import socket
import sys, argparse, datetime, threading, traceback

lock_socket = None  # we want to keep the socket open until the very end of
                    # our script so we use a global variable to avoid going
                    # out of scope and being garbage-collected

def is_lock_free():
	global lock_socket
	lock_socket = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
	try:
		lock_id = "zadieblack.twitterbot2"   # this should be unique. using your username as a prefix is a convention
		lock_socket.bind('\0' + lock_id)
		logging.debug("Acquired lock %r" % (lock_id,))
		return True
	except socket.error:
		# socket already locked, task must already be running
		logging.info("Failed to acquire lock %r" % (lock_id,))
		return False

if not is_lock_free():
	logging.info("Bot already running.")
	sys.exit()

# then, either include the rest of your script below,
# or import it, if it's in a separate file:
import names
import people
import misc

from io import BytesIO
from random import *
from util import *
from generators import *
from twitter_stuff import *

from ee_bot import *

InitBot(1800, 300, bTweet = True, bLoop = True)