"""
Angel A. Sanquiche Sanchez
angelsan720@gmail.com
angel.sanquiche@upr.edu
"""

"""
Ok Ill be the first to admit
I have no clue how video formats work
This script just takews some filenames splits
them at '.' and a adds the new extension for ffmpeg

this is for simple bulk processing
no big details can be added

also I wonder how thisll run on my server
Little warrior runs a celeron
"""

import sys
import os
import time

try:
	import ffmpy
except ImportError:
	print("install ffmpy and FFmpeg")
	sys.exit(0)

def Usage(msg=None):
	print("Usage:")
	print("python %s [path_to_files] olf_format new_format"%sys.argv[0])
	print("python %s -h\t\t\t\tDisplay this help"%sys.argv[0])

	if msg:
		print("Something don goofed:\n")
		print(msg)
		open("errorlog","w").write(e)
	sys.exit(0)

def bulkConvert(dir , oldFormat , newFormat):
	if dir:
		os.chdir(dir)
	files = os.listdir()
	log = open("log" , "a")

	for i in range(0 , len(files)):
		newFile = files[i].split(".")
		if (len(newFile)==2 and newFile[1] == oldFormat):

			ff = ffmpy.FFmpeg(
			inputs={files[i]:None},
			outputs={"%s.%s"%(newFile[0] , newFormat):"-strict -2"})

			
			log.write("%s\n"%(ff.cmd))
			print("%s\n"%(ff.cmd))

			start=time.time()
			ff.run()
			end = time.time()

			log.write("Time in seconds:%s\n"%(end - start))
			print("Time in seconds:%s\n"%(end - start))

if __name__ == "__main__":
	if len(sys.argv) < 2 or sys.argv[1] == "-h":
		Usage()

	elif len(sys.argv) == 3:
		old = sys.argv[1]
		new = sys.argv[2]
		dir = None

	elif len(sys.argv) == 4:
		dir = sys.argv[1]
		old = sys.argv[2]
		new = sys.argv[3]

	else:
		Usage()
	
	bulkConvert(dir=dir , oldFormat=old , newFormat=new)

