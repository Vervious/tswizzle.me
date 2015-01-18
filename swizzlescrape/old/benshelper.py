from moviepy.editor import VideoFileClip, concatenate

video = VideoFileClip("../videos/IKnewYouWereTrouble.mp4")

def make_video(word, start, end):
    video.subclip(start, end).to_videofile('words/' + word + '.mp4')

lyrics = '''
No apologies. He'll never see you cry,
Pretends he doesn't know that he's the reason why.
You're drowning, you're drowning, you're drowning.
Now heard you moved on from whispers on the street
A new notch in your belt is all I'll ever be
And now I see, now I see, now I see

He was long gone when he met me
And I realize the joke is on me, yeah!

I knew you were trouble when you walked in
So shame on me now
Flew me to places I'd never been
'Til you put me down, oh
I knew you were trouble when you walked in
So shame on me now
Flew me to places I'd never been
Now I'm lying on the cold hard ground
Oh, oh, trouble, trouble, trouble
Oh, oh, trouble, trouble, trouble

And the saddest fear comes creeping in
That you never loved me or her, or anyone, or anything, yeah

I knew you were trouble when you walked in
So shame on me now
Flew me to places I'd never been
'Til you put me down, oh
I knew you were trouble when you walked in (you were right there, you were right there)
So shame on me now
Flew me to places I'd never been
Now I'm lying on the cold hard ground
Oh, oh, trouble, trouble, trouble
Oh, oh, trouble, trouble, trouble'''

lyrics = lyrics.split()
numbers = [1.49104, 2.14714, 6.75507, 7.42262, 9.08272, 9.82684, 10.5742, 12.8668, 14.7707, 15.3466, 16.8929, 19.0927, 19.5788, 21.0344, 21.5867, 23.1309, 25.4902, 26.2743, 31.6183, 32.4904, 37.8822, 38.6096, 50.4659, 51.4097, 52.1136, 52.8656, 54.1376, 56.3537, 57.1857, 58.7295, 59.6337, 60.3215, 62.8418, 63.4015, 64.2574, 64.9622, 65.7535, 66.4573, 68.5851, 69.6333, 70.6088, 71.4678, 72.9211, 74.985, 75.8723, 77.1376, 79.1531, 82.4809, 84.6009, 85.3767, 88.5689, 91.1366, 91.7605, 105.233, 105.904, 106.585, 113.6, 117.52, 118.536, 119.09, 125.976, 129.976, 130.832, 131.656, 140.799, 141.415, 142.482, 143.207, 144.687, 151.119, 152.288, 153.927, 155.255]
base = 200.97
prevItem = -1


for x in xrange(0, len(numbers)):
    item = numbers[x] * 0.25 + base
    if prevItem > 0:
        print "[\"" + lyrics[x - 1] + "\", " + str(prevItem - 0.03) + ', ' + str(item + 0.04) + "],"
        #make_video(lyrics[x - 1], prevItem - 0.03, item + 0.05)
    prevItem = item


