#use this code to download YouTube videos 

from pytube import YouTube

def on_complete(stream, filepath):
    print('Download Complete')
    print(filepath)

def on_progress(stream, chunk, bytes_remaining):
    progress_string = f'{round(100 - (bytes_remaining / stream.filesize * 100), 2)}%'
    print(progress_string)

link = input('YouTube link: ')
video_object = YouTube(link, on_complete_callback = on_complete, on_progress_callback= on_progress)

#information
print(f'Tittle:  {video_object.title}')
print(f'Lenght:  {round(video_object.length / 60,2)} mins')
print(f'Views:   {round(video_object.views / 1000000,5)}M')
print(f'Channel: {video_object.author}')

#download
print('Download: (h)ighest  |  (l)owest  |  (a)udio  |  (e)xit')
download_choice = input('Choice: ')

if download_choice == 'h':
    video_object.streams.get_highest_resolution().download()

elif download_choice == 'l':
    video_object.streams.get_lowest_resolution().download()

elif download_choice == 'a':
    video_object.streams.get_audio_only().download()
