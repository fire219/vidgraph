# VidGraph
## A simple tool for creating animated bar graphs for video projects

### Installation
```
git clone https://github.com/fire219/vidgraph.git
pip install matplotlib ffmpeg-python
```
Then, download/compile ffmpeg for your system. By default, **VidGraph** looks for a local copy at `./ffmpeg/bin/ffmpeg.exe`. You may change this to your preference of folder within the `grapher.py` script, or comment out this line if you have it included in your system\'s PATH variable (e.g. is available via the `ffmpeg` command in your terminal).

### Usage

#### Live View:
`grapher.py dummy.json`

*Outputs:* a live view of the animation in a new window

#### Video Output:
`grapher.py dummy.json dummy.mp4`

*Outputs:* 

https://user-images.githubusercontent.com/6289427/170777169-a046b56a-7dcf-4bcc-912e-bedb036dd3f7.mp4

### License:
```
Copyright (c) 2022 Matthew Petry (fireTwoOneNine)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
