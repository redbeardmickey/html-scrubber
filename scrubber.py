import os
import re
import sys
from bs4 import BeautifulSoup
from __main__ import *

def scrub(file_name, flag):
	soup = BeautifulSoup(open(file_name), "html5lib")
	for node in soup.find_all(class_=flag):
		node.extract()

	new_html = soup.encode_contents(formatter="html")
	with open(file_name, "wb") as file:
		file.write(new_html)

	return

def main(directory, flag):

	print('Scrubbing files...')

	for root, dirs, files in os.walk(directory):
		for name in files:
			if name.endswith('.html'):
				filePath = os.path.join(root, name)

				print(filePath)
				scrub(filePath, flag)

	return 'Finished!'

if __name__ == "__main__":
	main('test_site', 'internalOnly')