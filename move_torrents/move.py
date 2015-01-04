__author__ = 'Zhuravskiy'
# coding: utf8
import os
import shutil
sourcepath='/Users/Zhuravskiy/Downloads/'                         #источник
destinationpath = '/Volumes/Download/torrents_file/'              #куда копировать
source = os.listdir(sourcepath)                                   #возвращает список всех файлов в папке
for files in source:
    if files.endswith('.torrent'):                                #если файл заканчивается на ...
        shutil.move(os.path.join(sourcepath,files), os.path.join(destinationpath,files))
                                                                  # shutil перемещает файлы
                                                                  # join соединяет путь source с названием
                                                                  # файла files в один путь.