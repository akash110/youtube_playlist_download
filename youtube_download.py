from pytube import Playlist
from pytube import YouTube
from os.path import exists
import os

playlist = Playlist('https://www.youtube.com/playlist?list=PLybot8imS249Rnw3UCepjxo-nP7dz06Qk')
print(playlist.video_urls)
print('Number of videos in playlist: %s' % len(playlist.video_urls))

urls=playlist.video_urls
for url in urls:
    # extract only audio
    yt=YouTube(str(url))
    video = yt.streams.filter(only_audio=True).first()
    destination="C://Users/akash/Downloads/imransongs"
    out_file = video.download(output_path=destination)
    # save the file
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    if exists(new_file):
        print("exists")
    else:
       os.rename(out_file, new_file)
       # result of success
    print(yt.title + " has been successfully downloaded.")
