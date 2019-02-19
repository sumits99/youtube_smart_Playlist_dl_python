import youtube_dl
import pytube
import clipboard
import os
import shutil
from pathlib import Path
home = str(Path.home())
home
path = home + '\\Desktop\\'
path
os.chdir(path)

if not os.path.exists(path+'All_files'):
    print('creating folder....\n')
    os.mkdir(path+'All_files')
    os.chdir(path+'All_files')
    if not os.path.exists(path+'All_files\\'+'youtube_videos'):
        print("creating youtube_videos folder in " +path+'All_files\\')
        os.mkdir(path+'All_files\\'+'youtube_videos')
    else:
        print("..Youtube_videos already exists \nhence skipping..")
        
    
else:
    print('..All_files folder already exist..\nHence skipping')
    os.chdir(path+'All_files')
    if not os.path.exists(path+'All_files\\'+'youtube_videos'):
        print("creating youtube_videos folder in " +path+'All_files\\')
        os.mkdir(path+'All_files\\'+'youtube_videos')
    else:
        print("..Youtube_videos already exists \nhence skipping..")

ytt=pytube.Playlist(clipboard.paste())
ytt.populate_video_urls()
url=ytt.video_urls[0]
video = pytube.YouTube(url)
title=video.title

path = path+'All_files\\'+'youtube_videos\\'

if not os.path.exists(str(path + title[:25])):
		print('creating folder')
		os.mkdir(str(path + title[:25]))
else:
		print('folder already exist')
fpath=str(path + title[:25])
print("Your video will be saved to: {}".format(fpath))

youtube_dl.os.chdir(fpath)
yt=youtube_dl.YoutubeDL()
yt.extract_info(clipboard.paste(),download=True)



