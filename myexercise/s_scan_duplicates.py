#!/usr/bin/python

#Description: This Program displays all the duplicate files in the given Directory
#Author: Kailash.M.S
#Date: April 2018
#Version: 1.0

__author__ = "M.S.Kailash"

import os, argparse
from m_duplicates_in_dir import duplicates_in_dir

# To Get the directory name from command line argument
# Check the Argument count and alert if it is not 2

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--debug", help="Debugging Mode Turned on",action="store_true")
parser.add_argument("scan_directory", help="Scans the Directory and displays Redundant filenames")
arguments = parser.parse_args()

if arguments.debug: #Set Debug Options
    import pdb
    pdb.set_trace()


obj_scan_dir = duplicates_in_dir(os.path.realpath(arguments.scan_directory))
print "Number of files in the Directory: ", obj_scan_dir.file_count
obj_scan_dir.scan_duplicate_filenames()
