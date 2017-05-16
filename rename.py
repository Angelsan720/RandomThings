
"""
Angel A. Sanquiche Sanchez
angelsan720@gmail.com
angel.sanquiche@upr.edu
"""

"""
Tis another fitting candidate for random things.

Made this script to fix a naming issue I had while
I was trying to bulk convert some stream recordings I had
apparently : is somesort or reserverd character in FFMPEG

*be careful with this thing

*one day Ill learn how to use argparse
"""

import os
import sys

def Usage(msg=None):
	print("%s:"%(sys.argv[0]))

	print("python %s -h\t\t\t\tDisplay this message"%sys.argv[0])

	print("python %s [path_to_target] target_substring replacement_substring"%sys.argv[0])
	
	if msf:	#My ocd made me add this
		print(msg)
	sys.exit()

def rename(dir , target , replacement , flag=True):
	print("got Here")
	if dir:
		os.chdir(dir)
	file_list = os.listdir()
	for old_name in file_list:
		name_split = old_name.split(target)
		new_name = name_split[0]
		for i in range(1 , len(name_split)):
			new_name = "%s%s%s"%(new_name , replacement , name_split[i])


		print("File %s - %s"%(old_name , new_name))

		if new_name != old_name and flag:
			print("Changing %s to %s"%(old_name , new_name))
			os.rename(old_name , new_name)

if __name__ == "__main__":
	dir = os.getcwd()

	if len(sys.argv) < 3:
		Usage()
	elif len(sys.argv) == 3:
		target = sys.argv[1]
		replacement = sys.argv[2]
	elif len(sys.argv) == 4:
		dir = sys.argv[1]
		target = sys.argv[2]
		replacement = sys.argv[3]

	if not os.path.isdir(dir):
		Usage("Path Doesn't Exist")

	try:
		rename(dir , target , replacement , True)
	except Exception as e:
		Usage("Something don goofed \n\n%s" % e)
