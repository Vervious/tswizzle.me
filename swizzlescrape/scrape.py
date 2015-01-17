import rap_genius_data
from lxml import html
import requests

def get_lyrics():
    for song in rap_genius_data.songs:
        print song['title']
        page = requests.get(song['url'])
        tree = html.fromstring(page.text)

        lyrics = tree.xpath('//div[@class="lyrics"]')[0].text_content()
        with open('lyrics/' + song['title'] + '.txt', 'w') as f:
            f.write(song['title'] + '\n')
            f.write(lyrics.encode('utf-8').strip())

    
