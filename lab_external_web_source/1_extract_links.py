import argparse
import json
import time
from random import random

from selenium import webdriver
from selenium.webdriver.common.by import By

'''
Simple script to scape a website using Selenium + Standard Browser

Why? Often the other methods won't work (e.g. due to website sensing the automated tool)

'''

# Settings
MAX_RANDOM_SLEEP_TIME=3 # Max time to sleep between requests

# script level variables
links={} # store links as url,already processed (True/False)
driver = webdriver.Chrome()




def get_links(url):

     global links
     global driver
     
     # Sleep for a random time to avoid getting blocked
     rand_time= random() * MAX_RANDOM_SLEEP_TIME
     print(f"Sleeping for {rand_time} seconds")
     time.sleep(rand_time)

     #Now open the url and get links
     driver.get(url)
     with open("dump.html", "w") as f:
          print(driver.page_source, file=f)
     quit()

     #page_links = driver.find_elements(By.TAG_NAME,'a')
     page_links = driver.find_elements(by=By.XPATH, value="//a[@href]")

     for link in page_links:
          new_link = link.get_attribute('href')

          #Check if this starts with our base URL
          if(new_link in links):
               print(f"Already in dict: {new_link}")
          else:
               print(f"Add new found link: {new_link}")
               links.update({new_link:False})

     
               
####### Main Script #######

# Get the Arguments the user has passed in
parser = argparse.ArgumentParser()
parser.add_argument("-u","--url_start", help="URL to start scraping")
args=parser.parse_args()

if args.url_start is None:
     print("\nSimple Script to recursively extract all URLs from a website\n")
     print("Usage: python 1_extract_links.py -u <URL>")
     print("    where <URL> is the link to the website.")
     quit()

print(f"\nstarting to extract links from: {args.url_start}\n")

# add the first link to the list of links to process
links[args.url_start]=False 

loop_counter=0

while True:
     #Note we test and break later
     loop_counter+=1
     
     # copy the dictionary to avoid python complaining about changing size during iteration
     links_copy = links.copy()

     # Now Recursively extract links from this page
     for key,value in links_copy.items():

          if value == True:
               # already processed, skip
               print(f"Skipping link: {key}")
               pass

          elif (key.startswith(args.url_start)):
               
                #process the value
               get_links(key)

               #remove the item from the dictionary
               links[key]=True
               links_copy[key]=True

          else:
               print(f"stepping over external link {key}")
               

     # Now check if we need to break (i.e. no new links added)
     print(F"=== LOOP CHECK BEFORE {len(links_copy)} AFTER {len(links)}==")

     if len(links) == len(links_copy):
          print("No new links added, stopping")
          break

     if loop_counter>10:
          print("finished after x loops")
          break
     

#FINISH UP
print ("\n\n")
print(json.dumps(links_copy,indent=4))

driver.close()