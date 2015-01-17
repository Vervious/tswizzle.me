import re

def convert_time(timestring):
    """ Converts a string into seconds """
    nums = map(float, re.findall(r'\d+', timestring))
    return 3600*nums[0] + 60*nums[1] + nums[2] + nums[3]/1000

songname = raw_input('songName: ')

with open('videos/' + songname + '/' + songname + '.srt') as f:
    lines = f.readlines()

lines = [line.strip().rstrip() for line in lines]

num = re.compile("^[0-9]*$")

lines = filter(lambda x: len(x) > 1, lines)
lines = filter(lambda x: not num.match(x) , lines)

times_texts = []
current_times, current_text = None, None
for i, line in enumerate(lines):
    times = re.findall("[0-9]*:[0-9]*:[0-9]*,[0-9]*", line)
    if times != []:
        current_times = map(convert_time, times)
    else:
        current_text = line
        times_texts.append((current_times, current_text))
        current_times, current_text = None, None
for elt in times_texts:
    print elt
