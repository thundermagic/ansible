#!/usr/bin/python

import datetime
import json

def show_time():
    date = str(datetime.datetime.now())
    print json.dumps({
        "time" : date
    })

show_time()
