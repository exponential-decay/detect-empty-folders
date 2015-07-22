#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import argparse
import ConfigParser
from DetectEmpties import *

def readconfig(configfile):
   paths = False
   puids = False
   zerobytes = False

   config = ConfigParser.ConfigParser()
   config.read(configfile)
   if config.has_section('blacklist'):
      if config.has_option('blacklist', 'filepaths'):
         configpaths = config.get('blacklist', 'filepaths')
         if configpaths != False:
            paths = configpaths.split(',')
      if config.has_option('blacklist', 'puids'):
         configpuids = config.get('blacklist', 'puids')
         if configpuids != False:
            puids = configpuids.split(',')
      if config.has_option('blacklist', 'zerobytefiles'):
         zerobytefiles = config.get('blacklist', 'zerobytefiles')
         if zerobytefiles.lower() == 'False' or zerobytefiles == '':
            zerobytes = False
         else:
            zerobytes = True

   return paths, puids, zerobytes

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
   parser.add_argument('--blacklist', help='Use blacklist file.', default=False, required=False)   

   if len(sys.argv)==1:
      parser.print_help()
      sys.exit(1)

   #	Parse arguments into namespace object to reference later in the script
   global args
   args = parser.parse_args()
   
   blacklist = args.blacklist
   
   if args.csv:
      if blacklist:
         blacklist = readconfig(blacklist)
      empty = DetectEmpties()
      empty.detectEmpties(args.csv, blacklist[0], blacklist[1], blacklist[2])
   else:
      parser.print_help()
      sys.exit(1)

if __name__ == "__main__":
   main()
