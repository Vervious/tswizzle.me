import random

from moviepy.editor import VideoFileClip, concatenate
from data import shake

videos = {
    'shake': VideoFileClip('videos/ShakeItOff.mp4'),
    'blank': VideoFileClip('videos/BlankSpace.mp4')
}

db = {}

def build_db(name, words):
    for item in words:
        word, start, end = item
        if word in db:
            db[word].append([name, start, end])
        else:
            db[word] = [[name, start, end]]

build_db('shake', shake.words)

def make_video(word, start, end):
    video.subclip(start, end).to_videofile('words/' + word + '.mp4')

def get_cuts(words):
    cuts = []
    for word in words:
        if word in db:
            cuts.append(random.choice(db[word]))
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

print fmtcols(sorted(list(db.keys())),8)

# make_video('dates', 18.025, 18.777)

# def unique_words():
#     s = set()
#     for item in times_texts:
#         words = item[1].split()
#         for w in words:
#             s.add(w.lower())
#     return s

# with open('shake-unique.txt', 'w') as f:
#     for item in times_texts:
#         f.write(str(item) + '\n')
#     for word in sorted(list(unique_words())):
#         f.write(word + '\n')