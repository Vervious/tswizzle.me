import random
import sys
import re
import os
dir = os.path.dirname(__file__)

from moviepy.editor import VideoFileClip, concatenate_videoclips, CompositeVideoClip, TextClip
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
    # finalcuts = []
    # final = None
    # for (word, (video, start, end)) in cuts:
    #     cut = videos[video].subclip(start, end)
    #     if hasText:
    #         txt_clip = (TextClip(word, font="helvetica", fontsize=100, color='white')
    #                   .set_position('center')
    #                   .set_duration(end - start) )
    #         cut = CompositeVideoClip([cut, txt_clip]) # Overlay text on video
    #     finalcuts.append(cut)
    #     if end - start < 0.3:
    #         final = concatenate_videoclips(finalcuts)
    #         finalcuts = [final]

    # final = concatenate_videoclips(finalcuts)
    # # final.write_videofile(os.path.join(dir, filename))
    #     final = concatenate_videoclips([CompositeVideoClip([videos[video].subclip(start, end), TextClip(word, font="helvetica", fontsize=100, color='white')]) for (word,(video, start, end)) in cuts])

    final = concatenate_videoclips([videos[video].subclip(start, end)
                         for (word, (video, start, end)) in cuts])
    final.to_videofile(filename)

def swizzle(sentence, output="swizzled.mp4", hasText=False):
    words = sentence.split()
    cuts = get_cuts(words)
    assemble_cuts(cuts, output, hasText=hasText)

def fmtcols(mylist, cols):
    lines = ("\t".join(mylist[i:i+cols]) for i in xrange(0,len(mylist),cols))
    return '\n'.join(lines)

def wordBank():
    return str(fmtcols(sorted(list(db.keys())),10))

def words():
    return sorted(db.keys())

def help():
    print wordBank()

def getLengths():
    words = [(tup[0], tup[1][0]) for tup in db.items()]
    word_lengths = [(tup[0], (tup[1][2]  - tup[1][1]) * 10000) for tup in words]
    int_diffs = []
    for tup in word_lengths:
        try:
            int_diffs.append((tup[0], int(tup[1])))
        except:
            pass
    lengths = sorted(int_diffs, key = lambda x: -x[1])
    print [tup[0] for tup in lengths]


getLengths()
