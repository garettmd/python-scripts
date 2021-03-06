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

__name__ = "__main__"
__author__ = "garettmd@gmail.com"

DESTDIR = '/home/garettmd/Pictures/'
SRCDIR = '/home/garettmd/Pictures/Mobile/'
DESCRIPTION = 'Move photos from source directory to destination directory'
EXIFERRORDIR = 'shutil.move(srcdir + filename, EXIFERRORDIR)'

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
parser.add_argument(
    '-d', '--destination', help='destination directory', required=True)
args = parser.parse_args()
srcdir = args.source
destdir = args.destination
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
                     (src, dest), exc_info=True)
    else:
        logger.info("File %s successfully moved to %s" % (src, dest))


def main():
    logger.info('\n\nStarting main function')
    dirs = srcdir
    for filename in listdir(dirs):
        logger.debug('File: %s \t Type: %s' % (filename, guess_type(filename)))
        if guess_type(filename)[0] == "image/jpeg":
            # Get EXIF data from image
            try:
                date = datetime.strptime(
                    str(piexif.load(filename)["Exif"][36867]).strip('b\''), '%Y:%m:%d %H:%M:%S')
            except:
                logger.error("Could not extract EXIF data from %s" %
                             filename, exc_info=True)
		shutil.move(srcdir + filename, EXIFERRORDIR)
            else:
                year = date.strftime("%Y")
                month = date.strftime("%m")
                shortmonth = date.strftime("%b")
                filepath = "%s%s-%s(%s)/" % (destdir, year, month, shortmonth)
                move(srcdir + filename, filepath)
        else:
            logger.info('File: %s not supported.' % filename)

if __name__ = '__main__':
    main()
