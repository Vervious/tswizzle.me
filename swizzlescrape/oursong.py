import re
from swizzle import parse

from moviepy.editor import VideoFileClip, concatenate

video = VideoFileClip("videos/oursong.mp4"),

times_texts = parse('videos/ShakeItOff/ShakeItOff.srt'),

def  (word, start, end),:
    video.subclip(start, end),.to_videofile('words/' + word + '.mp4'),
        
        [('riding', 12.710, 13.150),
         ('shot', 13.150, 13.525),
         ('gun', 13.525, 13.810),
         ('seat',15.765, 16.111),
         ('car', 16.674, 17.252),
         ('one', 18.206, 18.509),
         ('hand', 18.498, 18.831),
         ('feel', 18.822, 19.195),
         ('on', 19.248, 19.520),
         ('steering', 19.591, 20.068),
         ('wheel', 20.065, 20.631),
         ('other', 20.854, 21.397),
         ('my', 21.909, 22.472),
         ('heart', 22.487, 23.795),
         ('around', 24.204, 24.594),
         ('radio', 24.990, 25.494),
         ('baby', 26.382, 26.706),
         ('something', 26.787, 27.505),
         ('wrong', 27.523, 28.301),
         ('say', 28.905, 29.311),
         ('nothing', 29.287, 30.005),
         ('thinking', 30.732, 31.328),
         ('how', 31.316, 31.736),
         ('song', 32.701, 33.738),
         ('our', 36.083, 36.423),
         ('slamming', 37.064, 37.400),
         ('screen', 37.481, 37.814),
         ('door', 37.850, 38.369),
         ('sneaking', 38.384, 38.813),
         ('tapping', 38.403, 39.844),
         ('window', 40.523, 41.339),
         ('phone', 42.370, 42.874),
         ('talk', 43.157, 43.473),
         ('real', 43.503, 44.024),
         ('slow', 44.009, 44.596),
         ('late', 45.186, 45.520),
         ('momma', 45.865, 46.220),
         ('know', 46.548, 46.890),
         ('laugh', 48.279, 48.967),
         ('first', 49.232, 49.599),
         ('date', 49.605, 49.894),
         ('man', 49.876, 50.150),
         ('kiss', 50.561, 50.832),
         ('should', 51.196, 51.562),
         ('have', 51.542, 52.197),
         ('and', 52.635, 53.011),
         ('when', 53.005, 53.371),
         ('I', 53.377, 53.940),
         ('got', 53.997, 54.643),
         ('home', 54.626, 55.287),
         ('before', 55.275, 55.734),
         ('said', 55.990, 56.649),
         ('a', 56.696, 57.310),
         ('men', 57.340, 58.055),
         ('amen', 56.696, 58.055),
         ('asking', 58.007, 58.571),
         ('god', 58.717, 59.459),
         ('he', 59.697, 60.758),
         ('could', 60.026, 61.416)
         ('play', 61.395, 61.809),
         ('again', 62.188, 62.849),
         ('walking', 68.785, 69.175)
         ('front', 69.402, 69.819),
         ('porch', 69.783, 70,161),
         ('steps', 70.140, 70.504),
         ('after', 70.510, 71.043),
         ('every', 71.037, 71.550),
         ('everything', 71.061, 71.982),
         ('that', 71.988, 72.405),
         ('day', 72.396, 73.207),
         (
         
         
         
         
         
         
         
         
         
         
         # def unique_words(),:
         #     s = set(),
         #     for item in times_texts:
         #         words = item[1].split(),
         #         for w in words:
         #             s.add(w.lower(),),
         #     return s
         
         # with open('shake-unique.txt', 'w'), as f:
         #     for item in times_texts:
         #         f.write(str(item), + '\n'),
         #     for word in sorted(list(unique_words(),),),:
         #         f.write(word + '\n'),