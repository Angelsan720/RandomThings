"""
Angel A. Sanquiche Sanchez

angelsan720@gmail.com
angel.sanquiche@upr.edu
"""

"""
This script is a command line tool if both screed and sourmash are in the PATH
This script should also be able to be imported by anothe python script
"""

"""
This little script takes two assembled transcriptomes A and B 
For every sequence in A finds the sequence in B such that the jaccard of A and B is larger than T, T being 0.95 by default
"""

"""
This script requires sourmash of UC Davis dib-lab https://github.com/dib-lab/sourmash
This script requires screed of UC Davis dib-lab https://github.com/dib-lab/screed
"""



import time

import sys

try:

	import screed
	import sourmash_lib

except ImportError:
	print("screed and sourmash need to be installed and in the path")
	sys.exit(0)



def usage(use):
	if ( use == "command" ):
		print("Usage:\npython %s <file A> <file B>  "%(sys.argv[0]))
	elif( use == "function" ):
		print("Usage: s1=<file A> , s2=<file B>")
	sys.exit(0)

def compare_sequences(s1=None , s2=None , T=0.95):
	#if imported
	if s1 and s2:
		seqfile1 = screed.open(s2)
		seqfile2 = screed.open(s1)
	#if ran standalone
	elif (sys.argv[1] and sys.argv[2]):
		seqfile1 = screed.open(sys.argv[1])
		seqfile2 = screed.open(sys.argv[2])
	#in case of some sort of input error
	else:
		usage()

	#lists to hold all the sequences in the files
	f1 , f2 = [] , []


	t1 = time.time()

	#load the file into the list
	for read in seqfile1:
		E = sourmash_lib.Estimators(n=20, ksize=3)
		E.add_sequence(read.sequence)
		f1.append((read.name , read.sequence , E))

	t2 = time.time()

	print("Loaded file %s in %s seconds"%(sys.argv[1] , t2 - t1))


	t1 = time.time()

	#load the other file into the list
	for read in seqfile2:
		E = sourmash_lib.Estimators(n=20, ksize=3)
		E.add_sequence(read.sequence)
		f2.append((read.name , read.sequence , E))

	t2 = time.time()

	print("Loaded file %s in %s seconds"%(sys.argv[2] , t2 - t1))

	#output file
	out = open("%s-in-%s.txt"%(sys.argv[1] , sys.argv[2]) , "w")

	t1 = time.time()

	#for every sequence in file A
	for seq1 in f1:

		#set start asuming nothing matches and the minimum threshold
		max = (None,None,T)

		#for every sequence in file B
		for seq2 in f2:

			#get the jaccard index
			j = seq2[2].jaccard(seq1[2])

			#if the index is larger than the previous maximum
			if j > max[2]:

				#it becomes the new max secuence
				max = (seq1[0] , seq2[0] , j )

		#write out the maximum sequence in the output
		out.write("\n%s\n%s\ncorrespondence:%s\n"%(max[0] , max[1] , max[2]))


	t2 = time.time()


	print("Finished comparing all the sequences in %s seconds"%(t2 - t1))
	print("output:%s-in-%.txts"%(sys.argv[1] , sys.argv[2]))

	
	"""
	TODO:
	Accumulate all the sequences that all have the highest jaccard
	Script currently only take the first it finds
	"""
if (__name__ == "__main__"):
	compare_sequences(use="command")
