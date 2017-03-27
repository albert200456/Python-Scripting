import sys
import os
import glob
import imp
import re
import datetime
class myThread (threading.Thread):
    def __init__(self, threadID, name, key):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.key
    def run(self):
    	count = find_key(self.name, self.key)

class Output(object):
	def __init__(self):
		self.array = {}

	def traverse(self, root_dir, key_string):
		subdir_list = [x[0] for x in os.walk(root_dir)]
		print subdir_list
		for i in len(subdir_list):
			self.array[i] = find_key(i, key_string)
		print self.array
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
	print root_dir, key_string
	return root_dir, key_string

def find_key(subdir, key_string):
	return len([file for file in os.listdir(subdir) 
				if re.search(r'%s' % key_string, file)])

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
def count_plot(output, root_dir):
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
		plt.savefig('output/graph_%s.png' % root_dir)


def main():
	start = datetime.now()
	o = Output()
	# Check input and assign root directory and key string.
	root_dir, key_string = input_check() #order should be first
	# Traverse with input root directory and key string.
	o.traverse(root_dir, key_string)
	# Check availability of matplotlib module and plot the 
	# graph with output dictionary.
	if check_matplotlib():
		count_plot(o.array, root_dir)
	else:
		print "Please install module \'matplotlib\' to output graph."
	print "Please check output directory for output file and graph."

	print datetime.now() - start

if __name__ == "__main__":
	main()


