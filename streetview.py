# load libraries

import os
from PIL import Image
import PIL.ImageOps
import urllib, cStringIO
from moviepy.editor import *

frameArray = []

# get images via API

for i in range(180):
    angle = 'https://maps.googleapis.com/maps/api/streetview?size=640x640&location=YOUR-LOCATION&key=YOUR-API-KEY&fov=40&heading=170&pitch=' + str((180-float(i))/2.0)
    file = cStringIO.StringIO(urllib.urlopen(angle).read()) # manages URL
    image_file = Image.open(file)
    filename = '/FOLDER/' + str(i) + '.jpg'
    image_file.save(filename, 'JPEG')
    frameArray.append(filename) # adds image to array

# build video

clip = ImageSequenceClip(frameArray, fps=25)
clip = clip.to_videofile(‘/FOLDER/result.mp4', fps=25)
