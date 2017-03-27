import unittest
import assignment as a
import sys
import os
import time
import re


class FooTests(unittest.TestCase):
	def test_find_key(self):
		self.assertTrue(a.find_key('test_dir', 'test_find_key', 'find'))
	
	def test_find_key_if_fail(self):
		self.assertFalse(a.find_key('test_dir', 'test_find_key', 'are'))

	def test_key_regex(self):
		self.assertTrue(a.key_regex('find', 'see if you can find it.'))

	def test_key_regex_if_substring(self):
		self.assertTrue(a.key_regex('are', 'I am aware of the situation.'))

	def test_key_regex_if_fail(self):
		self.assertFalse(a.key_regex('do', 'What else?'))

	def test_output_length(self):
		time_now = time.strftime('%b_%d_%Y_%H_%M_%S_%p_%Z').strip()
		o = a.Output()
		self.assertEqual(len(o.traverse('test_dir', 'find', time_now)), 5)

	def test_output_length_for_plot(self):
		time_now = time.strftime('%b_%d_%Y_%H_%M_%S_%p_%Z').strip()
		o = a.Output()
		self.assertTrue(len(o.traverse('test_dir', 'find', time_now)) < 32768)

	def test_if_output_key_exists(self):
		time_now = time.strftime('%b_%d_%Y_%H_%M_%S_%p_%Z').strip()
		o = a.Output()
		output = o.traverse('test_dir', 'find', time_now)
		for (key, value) in output.iteritems():
			self.assertTrue(os.path.exists(key))

def main():
	unittest.main()

if __name__ == '__main__':
	main()