import re
import requests
import json
import urllib.request
import os
import sys
from random import random
import argparse


def download(username, html):
	a = html.split("window.__PRELOADED_STATE__ = ", 1)[1]
	data = a.split("\n",1)[0]

	array = json.loads(data).get("medias").get("byId")

	for content in array:
	    
	    file_url = array.get(content).get("media").get("videoUrl")
	    
	    # If there is not video, then look for the image
	    if file_url == None:
	    	file_url = array.get(content).get("media").get("responsiveUrl")
	    
	    # Need to have https:// to have valid url
	    file_url = "https://"+file_url
	    
	    fname = str(random())[3:9]+file_url.split("/")[-1]
	    dir_name = username+"/"
	    path = dir_name+fname

	    urllib.request.urlretrieve(file_url, path)
	    print("\033[92m[+] Downloaded:\033[0m {}".format(path.replace(dir_name, "")))


def main():
	
	parser = argparse.ArgumentParser(description = "Download all of the images and videos from a VSCO user")

	parser.add_argument('username', action="store",
		help="Username of VSCO user")

	parser.add_argument('pages', action="store",
    	help="Number of pages the user has",
    	type=int)

	args = parser.parse_args()


	for page in range(args.pages):
		url = url ="https://vsco.co/{}/images/{}"

		r = requests.get(url.format(args.username, page+1))

		if r.status_code == 404:
			print("\033[91m[-] Invalid username\033[0m")
			sys.exit()

		print("\033[92m[+] Fetched data\033[0m")
		os.makedirs(args.username, exist_ok=True)
		html = r.text

		download(username=args.username, html=html)

main()
