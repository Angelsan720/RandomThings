"""
Angel A. Sanquiche Sanchez
angelsan720@gmail.com
angel.sanquiche@upr.edu
"""
def random_rant():
	print(
	"""
	Ok Ill be the first to admit
	I have no clue how video formats work
	This script just takews some filenames splits
	them at '.' and a adds the new extension for ffmpeg

	update 09-06-17
	since ffmpeg is smart I found out this script can be used for more than just video formats.
	audio formats work as well :)

	this is for simple bulk processing
	no big details can be added

	also I wonder how thisll run on my server
	Little warrior runs a celeron
	""")

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

	#Switch working directory if needed
	if dir:
		os.chdir(dir)
		
	#get a permanent list of the files to work with
	files = os.listdir()
	
	#log when a command starts and if it ended
	log = open("log" , "a")

	for i in range(0 , len(files)):

		#like I said it takes files based on extensions
		newFile = files[i].split(".")
		if (len(newFile)==2 and newFile[1] == oldFormat):

			#use ffmpy to construct the command
			ff = ffmpy.FFmpeg(
			inputs={files[i]:None},
			outputs={"%s.%s"%(newFile[0] , newFormat):"-strict -2"})

			#log that the command started
			log.write("%s\n"%(ff.cmd))
			print("%s\n"%(ff.cmd))

			start=time.time()
			ff.run()
			end = time.time()
			#uncomment below line to remove source file
			#os.remove(file[i])

			#log that it finished
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

