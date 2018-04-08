#!/usr/bin/python
# Module: m_duplicates_in_dir.py
# Description: This module has the functionality to Scan all the file in the directory provided by the user and
#             lis all the duplicate files in them.
# Author: Kailash.M.S
# Date: April 2018
# Version: 1.0

__author__ = "M.S.Kailash"

import sys
import os

# Class containing the structure of Directory and
# Functions to Identify Duplicate files
class duplicates_in_dir: 
    check_dir = ''# To hold readable "user provided" directory
    file_list = [] # To Store all the files 
    file_count=0 # Will Contain the count of readable files in the directory

    def __init__(self, udir):
        try:
            argument="";
            errnum="";
            self.check_dir=udir
            self.validate_directory()
            self.scan_files()
        except ValueError as err:
            print err.args[0]
            exit()
        except:
            print "Caught Other Exceptions"
            exit()

    def validate_directory(self):
	#To check if the given folder exists
	if os.path.isdir(self.check_dir) == False:
            raise ValueError("Invalid Directory: " + self.check_dir)
	# Check for read access to Scan
	if os.access(self.check_dir, os.R_OK) == False:
            raise ValueError("You do not have access to scan " + self.check_dir)
	return
	
    def scan_files(self):	
        print "\nScanning files in: " + self.check_dir + "\n"

	# Scan the directory and Get the file List and store it in a list
        for root, directories, filenames in os.walk(self.check_dir):
            for directory in directories:
                os.path.join(root, directory)
            for filename in filenames:
                if os.access(root, os.R_OK) == True and os.access(root, os.X_OK) == True:
                    self.file_list.append(os.path.join(root,filename))

		# Remove the files without Read Permission
        index_count=0
        loop_count=0
	while loop_count < len(self.file_list):
            if os.access(self.file_list[index_count], os.R_OK) == False:
	        print "Read access disabled for '" + self.file_list[index_count] + "'"
		del self.file_list[index_count]
		loop_count += 1
            index_count += 1
            loop_count += 1

        self.file_count=len(self.file_list) #Assigning the file count list		
				
    #Function that Identifies duplicate functions
    def scan_duplicate_filenames(self):
     try:
        print "\n\nFinding Duplicates on the basis of File-Name [Base-name]: \n"
	skip_list=[]# If duplicates are established, mark the positions to avoid rescanning
	for var_index in range(0,self.file_count-1):
            if var_index not in skip_list:# Avoid Scanning Duplicates Already Established.
		for var_traverse in range(var_index+1,self.file_count):
                    if var_traverse not in skip_list:# Avoid Scanning Duplicates Already Established.
		        #Extract the Base-name from the list of files to be checked
		        file1=self.file_list[var_index].split("/")[-1].split(".")[0]
		        file2=self.file_list[var_traverse].split("/")[-1].split(".")[0]
		        			
		        file1_mtime=os.stat(self.file_list[var_index]).st_mtime
		        file2_mtime=os.stat(self.file_list[var_traverse]).st_mtime
					
		        #Compare only files if the base names match
		        if file1 == file2:
			    if file1_mtime >= file2_mtime:
	                        print self.file_list[var_traverse] + " may be superseded by " + self.file_list[var_index]
			    else:
			        print self.file_list[var_index] + " may be superseded by " + self.file_list[var_traverse]
			        var_index=var_traverse
                            skip_list.append(var_traverse)#Create a Skip List for Duplicate File positions
     except:
      print "Unexpected Exception to be handled:"
      exit()

    def __del__(self):
        class_name = self.__class__.__name__
