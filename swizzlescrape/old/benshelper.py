from moviepy.editor import VideoFileClip, concatenate

video = VideoFileClip("../videos/IKnewYouWereTrouble.mp4")

def make_video(word, start, end):
    video.subclip(start, end).to_videofile('words/' + word + '.mp4')

lyrics = '''
And the saddest fear comes creeping in
That you never loved me or her, or anyone, or anything, yeah
'''

lyrics = lyrics.split()
numbers = [1.24092, 1.8813, 2.69716, 5.40826, 13.8589, 15.3846, 18.4405, 26.0328, 27.0237, 28.2077, 29.2721, 30.3764, 35.3113, 36.1441, 39.1841, 40.0722, 45.359, 45.9839, 51.8876, 58.9587]
base = 275.45
prevItem = -1


for x in xrange(0, len(numbers)):
    item = numbers[x] * 0.25 + base
    if prevItem > 0:
        print "[\"" + lyrics[x - 1] + "\", " + str(prevItem - 0.03) + ', ' + str(item + 0.04) + "],"
        #make_video(lyrics[x - 1], prevItem - 0.03, item + 0.02)
    prevItem = item


