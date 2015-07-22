#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import argparse
from DetectEmpties import *

def main():

   # Usage: --csv          [droid report]
   #        --blfilepath   [path of objects selected for deletion]
   #        --blpuid       [puids we've blacklisted]
   #        --blzeros      [elect to delete zero byte files, non-records]
   #
   # Handle command line arguments for the script
   parser = argparse.ArgumentParser(description='Detect empty folders in DROID CSV Reports.')

   # Just the one argument here, DROID csv... 
   parser.add_argument('--csv', help='Single DROID CSV to read.', default=False, required=True)
   parser.add_argument('--blfilepath', help='Blacklist files to delete.', default=False, required=False)   
   parser.add_argument('--blpuid', help='Blacklist PUIDs to delete.', default=False, required=False)   
   parser.add_argument('--blzeros', help='Remove zero byte files.', default=False, required=False)   

   if len(sys.argv)==1:
      parser.print_help()
      sys.exit(1)

   #	Parse arguments into namespace object to reference later in the script
   global args
   args = parser.parse_args()
   
   if args.csv:
      empty = DetectEmpties()
      empty.detectEmpties(args.csv, args.blfilepath, args.blpuid, args.blzeros)
   else:
      parser.print_help()
      sys.exit(1)

if __name__ == "__main__":
   main()
