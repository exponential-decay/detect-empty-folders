"""Detect empty folders script using a DROID file format export.
"""

import sys
import argparse
import configparser as ConfigParser
from DetectEmpties import DetectEmpties


def readconfig(configfile):
    paths = False
    puids = False
    zerobytes = False

    config = ConfigParser.ConfigParser()
    config.read(configfile)
    if config.has_section("denylist"):
        if config.has_option("denylist", "filepaths"):
            configpaths = config.get("denylist", "filepaths")
            if configpaths.lower() != "false":
                paths = configpaths.split(",")
        if config.has_option("denylist", "puids"):
            configpuids = config.get("denylist", "puids")
            if configpuids.lower() != "false":
                puids = configpuids.split(",")
        if config.has_option("denylist", "zerobytefiles"):
            zerobytefiles = config.get("denylist", "zerobytefiles")
            if zerobytefiles.lower() == "false" or zerobytefiles == "":
                zerobytes = False
            else:
                zerobytes = True

    return paths, puids, zerobytes


def main():

    # Usage: --csv          [droid report]
    #        --blfilepath   [path of objects selected for deletion]
    #        --blpuid       [puids we've denylisted]
    #        --blzeros      [elect to delete zero byte files, non-records]
    #
    # Handle command line arguments for the script
    parser = argparse.ArgumentParser(
        description="Detect empty folders in DROID CSV Reports."
    )

    # Just the one argument here, DROID csv...
    parser.add_argument(
        "--csv", help="Single DROID CSV to read.", default=False, required=True
    )
    parser.add_argument(
        "--denylist", help="Use denylist file.", default=False, required=False
    )

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    # 	Parse arguments into namespace object to reference later in the script
    global args
    args = parser.parse_args()

    denylist = args.denylist

    if args.csv:
        empty = DetectEmpties()
        if denylist:
            denylist = readconfig(denylist)
            empty.detectEmpties(args.csv, denylist[0], denylist[1], denylist[2])
        else:
            empty.detectEmpties(args.csv)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
