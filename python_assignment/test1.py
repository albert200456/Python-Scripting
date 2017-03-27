import glob
import os
import re

key = '*.*'
key1 = '^[a-zA-Z]+_TESTResult.*'
l = glob.glob(key)
res = [f for f in os.listdir('dir') if re.search(r'%s' % key1, f)]
print len(glob.glob(key))
print l
print len(res), res

