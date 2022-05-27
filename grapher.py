# VidGraph
# A simple tool for creating animated bar graphs for video projects

# Copyright (c) 2022 Matthew Petry (fireTwoOneNine)

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import enum
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation, writers
import matplotlib.patheffects as PathEffects
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)
from math import log10 , floor
import numpy as np
import json
import sys

#==================================================
# CHANGE THIS TO POINT TO YOUR LOCAL FFMPEG INSTALL
plt.rcParams['animation.ffmpeg_path']='ffmpeg/bin/ffmpeg.exe'
# =================================================

# python default max() function will complain about values that are NaN
def setMaxSafe(set):
    max = 0
    for i in set:
        if (type(i) == int) or (type(i) == float):
            if i > max:
                max = i
    return max

if len(sys.argv) < 2:
    print("VidGraph usage: grapher.py <json file> [<output video file>]")
    print("VidGraph will create a live view of the animation if the output argument is not given.")
    exit()

with open(sys.argv[1], "r") as jsonfile:
    data = json.load(jsonfile)

plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['text.color'] = "white"
plt.rcParams['axes.labelcolor'] = "white"
plt.rcParams['xtick.color'] = "white"
plt.rcParams['ytick.color'] = "white"
plt.rcParams['font.sans-serif'] = [data["font"]]
plt.rc('font', size=15)

if len(sys.argv) > 2:
    fig = plt.figure(figsize = (data["videoRes"][0]/100, data["videoRes"][1]/100), facecolor=data["frameColor"])
else:
    fig = plt.figure(figsize = (16,9), facecolor=data["frameColor"])

axes = fig.add_subplot(1,1,1)
axes.set_facecolor(color=data["plotColor"]) 
axes.spines['top'].set_visible(False)
axes.spines['right'].set_visible(False)
axes.spines['bottom'].set_visible(False)
axes.spines['left'].set_visible(False)
axes.xaxis.grid(True, which='minor')
maxval = setMaxSafe(data["scores"])
xlim = round(maxval, 1-int(floor(log10(abs(maxval))))-1) + 10**int(log10(maxval))
axes.set_xlim(0, xlim)

datalen = len(data["scores"])

def animation_function(i):
    vals = []
    for x in range(0, datalen):
        if (type(data["scores"][x]) == int) or (type(data["scores"][x]) == float):    
            vals.append(data["scores"][x] * log10(100*(i+1)/data["frames"])/2)
        else:
            vals.append(0)
    plt.xlabel(data["axislab"])
      
    
    plt.barh(data["elements"],
            vals, color = data["palette"])

    if i == 0:
        for index, value in enumerate(data["scores"]):
            plt.text((0.0075*maxval),index-.015*datalen,str(value), size=20, path_effects=[PathEffects.withStroke(linewidth=1, foreground='black')])
    
  
plt.title(data["title"])

animation = FuncAnimation(fig, animation_function, 
                          frames = data["frames"], interval = 0, repeat = False)

if len(sys.argv) > 2:
    print("saving video as: "+ sys.argv[2])
    animation.save(sys.argv[2], writer = "ffmpeg", fps = 30)
else:
    plt.show()
