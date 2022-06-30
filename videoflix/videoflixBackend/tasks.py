import subprocess


def convert_360p(source): 
    #print("conerting to 480p")
    target = source[0:-4] + "_360p.mp4"
    cmd = "ffmpeg -i '{}' -s hd480 -c:v libx264 -crf 23 -c:a aac -strict -2 '{}'".format(source, target)
    subprocess.call(cmd, shell=True)

def convert_720p(source): 
    #print("conerting to 480p")
    target = source[0:-4] + "_720p.mp4"
    cmd = "ffmpeg -i '{}' -s hd480 -c:v libx264 -crf 23 -c:a aac -strict -2 '{}'".format(source, target)
    subprocess.call(cmd, shell=True)

def convert_1080p(source): 
    #print("conerting to 480p")
    target = source[0:-4] + "_1080p.mp4"
    cmd = "ffmpeg -i '{}' -s hd480 -c:v libx264 -crf 23 -c:a aac -strict -2 '{}'".format(source, target)
    subprocess.call(cmd, shell=True)