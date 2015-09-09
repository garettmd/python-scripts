# python-scripts

This is a dumping ground for my random Python scripts.

- ### Photomove
  
    This is the only script that's actually used for something. It finds files in a source directory, looks for JPEGs based off their MIME type, then moves those files to directories based off the taken date in the JPEG's EXIF data. For example:
    ```
    ./photomove.py -s /home/garettmd/Pictures/Mobile -d /home/garettmd/Pictures
    ```
    It requires Python 3 and will spit out a log file in the directory you run from, so plan accordingly
  
- ### Regexin and Passexam
    These are files I used while working from the book Automate the Boring Stuff with Python - http://smile.amazon.com/dp/1593275994
