import random

from moviepy.editor import VideoFileClip, concatenate
from data import shake, oursong, blank

videos = {
    'shake': VideoFileClip('videos/ShakeItOff.mp4'),
    'blank': VideoFileClip('videos/BlankSpace.mp4'),
    'oursong': VideoFileClip('videos/oursong.mp4')
}

db = {}

def build_db(name, words):
    for item in words:
        w, start, end = list(item)
        word = w.lower()
        if word in db:
            db[word].append([name, start, end])
        else:
            db[word] = [[name, start, end]]

build_db('shake', shake.words)
build_db('oursong', oursong.words)
build_db('blank', blank.words)

def make_video(word, start, end):
    video.subclip(start, end).to_videofile('words/' + word + '.mp4')

def compare_cut_len(x, y):
    return int((y[2] - y[1]) - (x[2] - x[1]) * 1000)

def get_cuts(words):
    cuts = []
    for word in words:
        if word in db:
            print word
            cuts.append(sorted(db[word], cmp=compare_cut_len)[0])
            # cuts.append(random.choice(db[word]))
    return cuts;

def assemble_cuts(cuts, filename):
    final = concatenate([videos[video].subclip(start, end)
                         for (video, start, end) in cuts])
    final.to_videofile(filename)

def swizzle(sentence, output="swizzled.mp4"):
    words = sentence.split()
    cuts = get_cuts(words)
    assemble_cuts(cuts, output)

def fmtcols(mylist, cols):
    lines = ("\t".join(mylist[i:i+cols]) for i in xrange(0,len(mylist),cols))
    return '\n'.join(lines)

def help():
    print len(db.keys()), 'Words in the Tswizzletionary'
    print fmtcols(sorted(list(db.keys())),10)

help()