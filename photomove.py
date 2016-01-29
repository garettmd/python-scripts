#!/usr/bin/env python3
import shutil
import sys
import piexif
import pdb
import logging
import argparse
from os import path, makedirs, listdir
from mimetypes import guess_type
from datetime import datetime
from gi.repository.GExiv2 import Metadata

__name__ = "__main__"
__author__ = "garettmd@gmail.com"

DESTDIR = '/home/garettmd/Pictures/'
SRCDIR = '/home/garettmd/Pictures/Mobile/'
DESCRIPTION = 'Move photos from source directory to destination directory'
EXIFERRORDIR = '/home/ubuntu/errors/'

##############################
# Configure logging parameters
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
handler = logging.FileHandler('photomove.log')
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
##############################

#####################
# Configure argparser
parser = argparse.ArgumentParser(description=DESCRIPTION)
parser.add_argument('-s', '--source', help='source directory', required=True)
parser.add_argument('-d', '--destination', help='destination directory', required=True)
parser.add_argument('-l', '--loglevel', help='loglevel: Turn flag on for extra error info', required=False, action='store_true')
args = parser.parse_args()
srcdir = args.source
destdir = args.destination
logging = args.loglevel
#####################


def move(src, dest):
    try:
        if path.exists(dest):
            shutil.move(src, dest)
        else:
            makedirs(dest)
            shutil.move(src, dest)
    except:
        logger.error('Failed to move file %s to %s' %
                     (src, dest), exc_info=logging)
    else:
        logger.info("File %s successfully moved to %s" % (src, dest))


def main():
    logger.info('\n\nStarting main function\n\n')
    dirs = srcdir
    for filename in listdir(dirs):
        logger.debug('\nFile: %s \t Type: %s' % (filename, guess_type(filename)))
        try:
            data = Metadata(srcdir + filename)
        except:
            logger.error("%s: Filetype not supported" % filename, exc_info=logging)
            move(srcdir + filename, EXIFERRORDIR)
        else:
            # Get EXIF data from image
            try:
                date = data.get_date_time()
            except:
                logger.error("%s: No date-time specified in file. Leaving in current directory" %
                    filename, exc_info=logging)
            else:
                year = date.strftime("%Y")
                month = date.strftime("%m")
                shortmonth = date.strftime("%b")
                filepath = "%s%s-%s(%s)/" % (destdir, year, month, shortmonth)
                move(srcdir + filename, filepath)


main()
