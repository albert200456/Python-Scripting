# File Traversing script
This script recursively walk through "root_dir" and every sud_directories and files in order
to search for the "key_string".

# I/O
Input: 
1. root_dir name
2. key_string

Output (with time when script starts running):
1. Dictionary with tuples of key being subdir string and values being counts of files containing the keyword.
2. Graph with subdir string as x-axis and counts of files containing the keyword as y-axis.


# Note
* The "assignment.py" script is based on Python 2.7 and under OSX environment.
* Please install module 'matplotlib' in order to output graph.
* Please run the following command to run the script (root_dir as the Root directory to start 
  traversing, key_string as the Interested Keyword)

  	python assignment.py root_dir key_string


* For test purpose, please run the following command:

	python test.py




