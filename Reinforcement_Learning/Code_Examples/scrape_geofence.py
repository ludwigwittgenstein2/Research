#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 14:22:11 2017

@author: rstudio
"""

from stream_listener import SListener
from http.client import IncompleteRead
import time, tweepy, sys, json

## authentication
import tweepy

from pathlib import Path
home = str(Path.home())

with open(home + '????\keys.json', 'r') as infile: # Make sure you have a keys.json file with the Twitter Access keys. The '???' will need a absolute path of that file. Update this line
    keys = json.load(infile)


consumer_key = keys['consumer_key']
consumer_secret = keys['consumer_secret']
access_key = keys['access_token']
access_secret = keys['access_token_secret']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)

api = tweepy.API(auth)

def main():
 
    listen = SListener(api, 'Italy') # Update the 'GF_Canada' line to whichever country you are collecting data for. This will rename the output files accordingly
    stream = tweepy.Stream(auth, listen)

    print("Streaming started...")

    while True:
        try:
            stream.filter(locations=[-152.9, 35.9, -47.27, 84.22]) # This is where you add the geolocation of the country. Format = SouthWest Corner(Long, Lat), NorthEast Corner(Long, Lat)
        except KeyboardInterrupt:
            break

        except:
            print("error!")
            time.sleep(60*15)
            continue

        #stream.disconnect()

if __name__ == '__main__':
    main()
