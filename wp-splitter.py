#!/usr/bin/python

# This script is designed to take a WordPress xml export file and split it into some
# number of chunks (2 by default). The number of lines per chunk is determined by counting
# the number of occurences of a particular line, '<item>\n' by default, and breaking up the
# such that each chunk has an equal number occurences of that line. The appropriate header
# and footer is added to each chunk.


# Instructions for use:
# in terminal
# make sure you cd to the right directory
# and that the two files are in that same directory
# python WPsplitter.py <filename.extension> <number of chunks>

import os
import sys
import math

if len(sys.argv) < 2 :
	print 'Please specify the name of WordPress export file you would like to split'
	sys.exit(0)

try :
	input_file = open(sys.argv[1], 'r')
	lines = input_file.readlines()
	(input_file_path, input_file_string) = os.path.split(sys.argv[1])
	(input_file_name, input_file_extension) = os.path.splitext(input_file_string)
except IOError :
	print 'Could not open file "%s".' % sys.argv[1]
	sys.exit(0)

number_of_chunks = max(int(sys.argv[2]), 2) if len(sys.argv) > 2 else 2
line_delimiter = '\t<item>\n'

delimiter_count = 0
for line in lines :
	if line == line_delimiter :
		delimiter_count += 1

print ''
print 'File "%s" contains %s items' % (input_file_string, delimiter_count)

delimiter_count = 1.0*delimiter_count
delimiters_per_chunk = int(math.ceil(delimiter_count/number_of_chunks))

print 'Creating %s files with at most %s items each:' % (number_of_chunks, delimiters_per_chunk)

header = ""
footer = "\n</channel>\n</rss>\n"
chunk_number = 1
output_file_name = "%s_%s%s" % (input_file_name, chunk_number, input_file_extension)
output_file = open(output_file_name, 'w')
print '   Writing chunk %s to file %s...' % (chunk_number, output_file_name)

delimiter_count = 0
for line in lines :
	if line == line_delimiter : delimiter_count += 1

	if chunk_number is 1 and delimiter_count is 0 : header += line

	if delimiter_count > delimiters_per_chunk :
		output_file.write(footer)
		output_file.close()
		chunk_number += 1
		delimiter_count = 1

		output_file_name = "%s_%s%s" % (input_file_name, chunk_number, input_file_extension)
		output_file = open(output_file_name, 'w')
		print '   Writing chunk %s to file %s...' % (chunk_number, output_file_name)
		output_file.write(header)

	output_file.write(line)

output_file.close()
print 'Done!\n'
