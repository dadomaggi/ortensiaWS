#!/usr/bin/python

import datetime

def secs_from_midnight():
    now = datetime.datetime.now()
    midnight = datetime.datetime.combine(now.date(), datetime.time())
    return(now - midnight).seconds
