from moviepy.editor import VideoFileClip, concatenate

video = VideoFileClip("../videos/IKnewYouWereTrouble.mp4")

def make_video(word, start, end):
    video.subclip(start, end).to_videofile('words/' + word + '.mp4')

lyrics = '''Once upon a time a few mistakes ago
I was in your sights, you got me alone
You found me, you found me, you found me
I guess you didn't care, and I guess I liked that
And when I fell hard you took a step back
Without me, without me, without me

And he's long gone when he's next to me
And I realize the blame is on me

'Cause I knew you were trouble when you walked in
So shame on me now
Flew me to places I'd never been
'Til you put me down, oh
I knew you were trouble when you walked in
So shame on me now
Flew me to places I'd never been
Now I'm lying on the cold hard ground
Oh, oh, trouble, trouble, trouble
Oh, oh, trouble, trouble, trouble

No apologies. He'll never see you cry,
Pretends he doesn't know that he's the reason why.
You're drowning, you're drowning, you're drowning.
Now I heard you moved on from whispers on the street
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
numbers = [18.1616, 19.9823, 21.2701, 21.8301, 24.4807, 25.0699, 26.0799, 27.2857, 31.0939, 31.9581, 32.7737, 33.4938, 34.2179, 37.4703, 38.2209, 38.91, 39.838, 42.9894, 43.6776, 46.6852, 49.3098, 50.0128, 52.9807, 55.446, 56.1811, 59.2686, 68.1252, 68.7096, 69.4692, 70.189, 71.7099, 73.9969, 74.5251, 74.8772, 75.605, 76.301, 77.2391, 80.284, 80.9811, 81.9808, 82.612, 83.5741, 86.5571, 87.4207, 88.2452, 88.8679, 90.2766, 92.7329, 96.6445, 98.9719, 102.82, 105.363, 109.076, 120.967, 123.919, 124.426, 131.079, 135.007, 136.318, 136.782, 141.838, 143.436, 147.398, 149.27, 149.99, 158.39, 158.95, 160.024, 160.774, 162.142, 167.837, 168.669, 169.933, 171.47, 172.958, 174.565, 176.141, 176.917, 177.685, 179.109, 186.32, 187.287, 188.645, 189.99, 191.733, 193.845, 196.526, 198.023, 199.653, 201.46, 202.677, 204.127, 210.556, 211.396, 211.982, 213.636, 215.284, 216.844, 218.434, 219.756, 221.276, 222.748, 224.411, 226.172, 227.1, 227.724, 229.124, 236.124, 237.028, 238.548, 239.892, 241.468, 244.963, 246.515, 247.611, 249.356, 250.956, 252.139, 253.979, 260.438, 261.299, 261.963, 263.531, 264.139, 264.963, 266.563, 268.173, 284.058, 284.371, 284.602]
base = 121.78
prevItem = -1


for x in xrange(0, len(numbers)):
    item = numbers[x] * 0.25 + base
    if prevItem > 0:
        print "[\"" + lyrics[x - 1] + "\", " + str(prevItem - 0.03) + ', ' + str(item + 0.04) + "],"
        #make_video(lyrics[x - 1], prevItem - 0.03, item + 0.05)
    prevItem = item


