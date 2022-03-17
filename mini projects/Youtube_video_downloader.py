from pytube import YouTube
import os
import time

name = os.getlogin()
dictionary = 'Youtube videos'
parent_dictionary = '/home/' + name + '/Downloads'
path = os.path.join(parent_dictionary, dictionary)
video = None
try:
    os.mkdir(path)
except FileExistsError:
    pass
found = False
while not found:
    globals()
    video_url = input("Enter video url: ")
    try:
        video = YouTube(video_url)
        found = True
    except:
        found = False
        print("video not found")

resolutions = [i.resolution for i in video.fmt_streams if i.resolution != None]
types = [i.type for i in video.fmt_streams if i.type != None]
res = []
type = []
def fli(before, after):
    for item in before:
        if item not in after:
            after.append(item)

fli(resolutions, res)

fli(types, type)

def download(type):
    globals()
    print(video)
    print(video.title)
    file_name = video.streams.filter(mime_type="audio/mp4").first().download(path)
    #print(file_name)
    print(path+'/'+video.title+'.mp4')

# print(f"resolution: {res}")
# resolution_index = int(input("choise resolution, 1, 2, ..."))

print(f"type: {type}")
type_index = int(input("choise resolution, 1, 2, ..."))
download(type[type_index])

time.sleep(5)
print(path)
video_list = os.listdir(path)
os.renames(path + '/' + video_list[0], path+'/'+video.title+'.mp3')


