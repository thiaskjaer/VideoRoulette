import os
from pathlib import Path
from random import randint

folders = os.listdir() #list of video folders
#only keep directories
for folder in folders:
    if not(os.path.isdir(folder)):
        folders.remove(folder)
folderPick = randint(0,len(folders)-1) #pick random folder
folderName = folders[folderPick] #hold name of picked folder

videos = os.listdir(folderName) #list of videos in picked folder
videoPick = randint(0,len(videos)-1) #pick random video
videoName = videos[videoPick] #name of random video
data_folder = Path(folderName+'/'+videoName) #the path to the video

#handles creating a tally file if it does not exist and updating the tally
def makeTally(videoName):
    #only make tally if it does not exist
    if not(os.path.exists("tally.txt")):
        file = open('tally.txt', 'w+')
        #for every folder print the folder name and contents of the folder
        for folder in folders:
            file.write(folder+'\n')
            videos = os.listdir(folder)
            for video in videos:
                file.write(video+': 0'+'\n')
            file.write('\n')
        file.close()

    #increment video counter
    with open("tally.txt", "r") as f:
        lines = f.readlines()

    updatedLine = ''
    for line in lines:
        if line.strip().startswith(videoName): #find specificed line
            stringSplit = line.split(": ") #every line has a ': ' followed by a number
            num = int(stringSplit[1].strip())+1 #the video's tally
            updatedLine = line.replace(stringSplit[1], str(num)+'\n') #the line to write

    #overwrite the file with the updated tally        
    with open("tally.txt", "w") as f:
        for line in lines:
            if not(line.strip('\n').startswith(videoName)):
                f.write(line)
            else:
                f.write(updatedLine)     

makeTally(videoName)
os.startfile(data_folder) #play the video using standard video player



