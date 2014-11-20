#
# XYZ Pt Chain creator between electrodes. 
# The result will be dumped on stdout
# 
# Author: Gonzalo Aguirre <graguirre@gmail.com>
#

import sys, getopt
import numpy as np


def usage():
	print >> sys.stderr, "Options:"
	print >> sys.stderr, " -h Show help"
	print >> sys.stderr, " -e <element> Element (Supported: Pt, Au)"
	print >> sys.stderr, " -n <integer> chain length (default 0)"
	print >> sys.stderr, "Syntax: python2 chain.py -e Pt -n 1"
	sys.exit(1)


def main(argv):
	# electrodes, don't modify these lines.
	top = open('elec-top.xyz')
	bot = open('elec-bottom.xyz')

	chl = 0 	# chain len (default 0 just tips)
	gap = 1.405 	# r = 2.77468
	e = 'Pt'	# default element

	 # manage parameters
	try:
		opts, args = getopt.getopt(argv,"he:n:")
	except getopt.GetoptError:
		usage()


	for opt, arg in opts:
		if opt == '-h':
			usage()
		elif opt == '-e':
			e = arg
		elif opt == '-n':
			chl = int(arg)

	# init array	
	arr = np.array([]).reshape(0,3)

	# XYZ file header
	print 2*10+chl # number of atoms
	print 		# empty line 	  
	
	# bottom electrode
	for i in bot:
		b = i.strip().split()
		b = [float(j) for j in b[1:4]]
		tmp = np.array(b)
		arr = np.vstack([arr,tmp])
		
	# chain
	for i in range(chl):
		tmp = np.array(3*[gap])
		arr = np.vstack([arr,(i+1)*tmp])
		
	# top electrode
	for i in top:
		t = i.strip().split()
		t = [float(j)+(chl+1)*gap for j in t[1:4]]
		tmp = np.array(t)
		arr = np.vstack([arr,tmp])

	for i in map(list,arr):
		print e + '\t' + '\t'.join(map(str,i))


if __name__ == "__main__":
	main(sys.argv[1:])
