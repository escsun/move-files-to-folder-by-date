# -*- coding: utf-8 -*-

import os, shutil, pytz

from datetime import datetime

tz = pytz.timezone('Europe/Kiev')

error_log = open("error.log", "w", encoding="utf-8")
files_log = open("files.log", "w", encoding="utf-8")

# files will be ignored to move
EXTENSIONS = (
    '.py',
    '.log',
    '.db'
)

print("Start moving files.")

for root, dirs, files in os.walk(os.getcwd()):
    for file in files:
        if not file.endswith(EXTENSIONS):
            # file create time with local timezone
            time = datetime.fromtimestamp(os.path.getmtime(os.path.join(root, file)), tz)

            dir_ctime = time.strftime("%Y_%m_%d")

            # create folder if doesn't exists
            if not os.path.isdir(dir_ctime):
                os.mkdir(dir_ctime)

            try:
                shutil.move(os.path.join(root, file), dir_ctime)
                log = "{file} has been moved to: {dir} \n".format(file=file, dir=dir_ctime)
                files_log.write(log)
            except:
                log = "{file} already exists in folder: {dir} \n".format(file=file, dir=dir_ctime)
                error_log.write(log)
            finally:
                print(log)

print("End moving files.")

error_log.close()
files_log.close()
