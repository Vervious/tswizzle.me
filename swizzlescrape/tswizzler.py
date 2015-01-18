import random
import sys
import re
import os
dir = os.path.dirname(__file__)

from moviepy.editor import VideoFileClip, concatenate, CompositeVideoClip, TextClip
from data import shake, oursong, blank, trouble, lovestory, youbelongwithme, neverbacktogether

videos = {
    'shake': VideoFileClip(os.path.join(dir, 'videos/ShakeItOff.mp4')),
    'blank': VideoFileClip(os.path.join(dir, 'videos/BlankSpace.mp4')),
    'oursong': VideoFileClip(os.path.join(dir, 'videos/oursong.mp4')),
    'trouble': VideoFileClip(os.path.join(dir, 'videos/IKnewYouWereTrouble.mp4')),
    'lovestory': VideoFileClip(os.path.join(dir, 'videos/lovestory.mp4')),
    'youbelongwithme': VideoFileClip(os.path.join(dir, 'videos/youbelongwithme.mp4')),
    'neverbacktogether': VideoFileClip(os.path.join(dir, 'videos/neverbacktogether.mp4'))
}

db = {}
regex = re.compile('[^a-z]')

def build_db(name, words):
    for item in words:
        w, start, end = list(item)
        word = w.lower()
        word = regex.sub('', word)
        if word in db:
            db[word].append([name, start, end])
        else:
            db[word] = [[name, start, end]]

build_db('shake', shake.words)
build_db('oursong', oursong.words)
build_db('blank', blank.words)
build_db('trouble', trouble.words)
build_db('lovestory', lovestory.words)
build_db('youbelongwithme', youbelongwithme.words)
build_db('neverbacktogether', neverbacktogether.words)

def make_video(word, start, end):
    video.subclip(start, end).to_videofile('words/' + word + '.mp4')

def compare_cut_len(x, y):
    return int((y[2] - y[1]) - (x[2] - x[1]) * 1000)

def get_cuts(words):
    cuts = []
    for word in words:
        word = word.lower()
        word = regex.sub('', word)
        if word in db:
            cuts.append((word, (sorted(db[word], cmp=compare_cut_len)[0])))
            # cuts.append(random.choice(db[word]))
    return cuts;

def assemble_cuts(cuts, filename, hasText=False):
    finalcuts = []
    for (word, (video, start, end)) in cuts:
        cut = videos[video].subclip(start, end)
        if hasText:
            txt_clip = (TextClip(word, font="helvetica", fontsize=100, color='white')
                     .set_position('center')
                     .set_duration(end - start) )
            cut = CompositeVideoClip([cut, txt_clip]) # Overlay text on video
        finalcuts.append(cut)

    final = concatenate(finalcuts)
    final.to_videofile(os.path.join(dir, filename))

def swizzle(sentence, output="swizzled.mp4", hasText=False):
    words = sentence.split()
    cuts = get_cuts(words)
    assemble_cuts(cuts, output, hasText=hasText)

def fmtcols(mylist, cols):
    lines = ("\t".join(mylist[i:i+cols]) for i in xrange(0,len(mylist),cols))
    return '\n'.join(lines)

def help():
    print len(db.keys()), 'Words in the Tswizzletionary'
    print fmtcols(sorted(list(db.keys())),10)

help()
