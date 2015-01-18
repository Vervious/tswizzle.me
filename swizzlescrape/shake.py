import re
from swizzle import parse

from moviepy.editor import VideoFileClip, concatenate

video = VideoFileClip("videos/ShakeItOff/ShakeItOff.mp4")

times_texts = parse('videos/ShakeItOff/ShakeItOff.srt')

def make_video(word, start, end):
    video.subclip(start, end).to_videofile('words/' + word + '.mp4')

make_video('dates', 18.025, 18.777)

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