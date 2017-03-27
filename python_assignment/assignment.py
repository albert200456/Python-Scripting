import sys
import os
import time
import re
import imp
import glob


class Output(object):
	def __init__(self):
		self.array = {}

	def traverse(self, root_dir, key_string, time_now):
		if os.access(root_dir, os.F_OK):
			# Walk through all directories and files.
			for (path, dirs, files) in os.walk(root_dir):
			    key_counts = 0
			    print path, dirs, files
			    for file in files:
			    	# Avoid hidden files
			    	if not file.startswith('.'):
				    	if find_key(path, file, key_string):
				    		key_counts += 1
			    self.array[path] = key_counts
		# output dir exists?
		try:
			f = open('%s/dictionary_%s_%s' % ('output', root_dir, time_now), 'w')
		except IOError:
			print "ERROR: Can\'t open file"
		else:
			for (key, value) in self.array.iteritems():
				f.write('%s: %d\n' % (key, value))

		print(self.array) # python 3 not recognize
		# sys.stdout
		# sys.stderr
		return self.array

def input_check():
	if len(sys.argv) < 3:
		sys.exit("ERROR: Input directory or key string not found.\
			      \nIf you want to search for a blank, use \' \' instead. ")
	elif len(sys.argv) > 3:
		sys.exit("ERROR: Input arguments more than expected.")
	else:
	    root_dir = sys.argv[1]
	    if not os.path.exists(root_dir):
			sys.exit("ERROR: Directory '%s' not found" % sys.argv[1])
	    key_string = sys.argv[2]
	return root_dir, key_string

# Take keyword as regular expression
def key_regex(key_string, test):
	regex = re.compile(r'(%s)' % (key_string))
	match = regex.search(test)
	if match:
		return True
	else:
		return False

def find_key(path, file, key_string):
	found = False
	if not file.startswith('.'):
		path_file = '%s/%s' %(path, file)
	# Check if file is empty, if file exists, if file readable
	if (os.stat(path_file).st_size != 0 and
		os.path.exists(path_file) and 
		os.access(path_file, os.R_OK)):
		try:
			f = open('%s/%s' %(path, file), 'r+')
		except IOError:
			print "ERROR: Could not read file: ", path_file
			pass
		else:
			for line in f.readlines():
				if key_regex(key_string, line):
					found = True
			f.close()
	return found

def check_matplotlib():
	try:
		imp.find_module('matplotlib')
		found = True
	except ImportError:
		print "ERROR: Module 'matplotlib' not found."
		found = False
	return found

# Plot the graph of x: file path and y: key string counts.
# Also save the output graph named after root_dir.
def count_plot(output, root_dir, time_now):
	import matplotlib.pyplot as plt
	length = len(output)
	# Matplotlib module can't plot graph with width and height over 32768.
	if length * 10 > 32768:
		print 'Width and Height of the graph must be lower than 32768.'
	else:
		plt.figure(figsize=(length * 2, 5))
		plt.xlabel('File Path')
		plt.ylabel('Counts')
		plt.xticks(range(length), output.keys())
		plt.xlim(-1, length)
		plt.bar(range(length), output.values(), align='center', alpha=0.5)
		plt.savefig('%s/graph_%s_%s.png' % ('output', root_dir, time_now))



def main():
	o = Output()
	time_now = time.strftime('%b_%d_%Y_%H_%M_%S_%p_%Z').strip()
	# Check input and assign root directory and key string.
	root_dir, key_string = input_check() #order should be first
	# Traverse with input root directory and key string.
	o.traverse(root_dir, key_string, time_now)
	# Check availability of matplotlib module and plot the 
	# graph with output dictionary.
	if check_matplotlib():
		count_plot(o.array, root_dir, time_now)
	else:
		print "Please install module \'matplotlib\' to output graph."
	print "Please check output directory for output file and graph."


if __name__ == "__main__":
	main()
