#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Import libraries
import pync
import time

n = 10# number of seconds between notifications
start = 0# number of second at the beginning of running code

while True:
    start += n
    pync.notify("Type notification message here, e.g., ALERT!!!,"
                +str(start)+"seconds have passed!")
    time.sleep(n)# number of seconds between notifications
