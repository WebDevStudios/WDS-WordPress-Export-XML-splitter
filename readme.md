# WDS WordPress Export XML splitter

This script is designed to take a wordpress xml export file and split it into some
number of chunks (2 by default). The number of lines per chunk is determined by counting
the number of occurences of a particular line, '<item>\n' by default, and breaking up the
such that each chunk has an equal number occurences of that line. The appropriate header
and footer is added to each chunk.

I downloaded this from somewhere, and cannot remember the original author. Please step up up if it is you so I can give credit where it is due.

**Update:** Looks like there's an app as well: [https://github.com/suhastech/Wordpress-WXR-Splitter](https://github.com/suhastech/Wordpress-WXR-Splitter)


### Instructions for use:
in terminal
make sure you cd to the right directory
and that the two files are in that same directory

`python wp-splitter.py <filename.extension> <number of chunks>`
