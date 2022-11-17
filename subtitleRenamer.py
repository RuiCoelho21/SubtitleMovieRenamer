import os
import glob

folder = os.getcwd()

for filename in os.listdir(folder):
    infilename = os.path.join(folder, filename)
    if not os.path.isfile(infilename):
        continue
    oldbase = os.path.splitext(filename)
    newname = infilename.replace('.mkv', '.mp4')
    output = os.rename(infilename, newname)


for index, oldfile in enumerate(glob.glob("*.mp4"),  start=1):
    newfile = '{}.mp4'.format(index)
    os.rename(oldfile, newfile)

for index, oldfile in enumerate(glob.glob("*.srt"),  start=1):
    newfile = '{}.srt'.format(index)
    os.rename(oldfile, newfile)
