# -*- coding: utf-8 -*-
import os
from posixpath import expanduser
from underthesea import word_tokenize
import requests
import bs4
from bs4 import BeautifulSoup
import traceback
import logging
import random

logging.basicConfig(level=logging.INFO)

force = False
input_base_url = 'G:/My Drive/PROJECT/nvck/truyenfull.vn/stories'
output_base_url = 'G:/My Drive/PROJECT/audio/vos'

def process_word(word, voice):
    word = word.translate ({ord(c): "" for c in "!@#$%^&*()[]{};:,./<>?\|`~-=_+"})
    word = word.strip()
    logging.info(f'Process word: {word}')
    if not force:
        if os.path.exists(f'{output_base_url}/{voice}/{word}.mp3'):
            return

    resp = requests.post('https://ailab.hcmus.edu.vn/vos/demo.php', data = {
        "text": word,
        "voice": voice,
        "speed": "1"
    })

    soup = BeautifulSoup(resp.text, 'html.parser')
    soup_source = soup.select('source')[0]

    link = soup_source.attrs['src']
    r = requests.get(f'https://ailab.hcmus.edu.vn/vos/{link}', allow_redirects=True)
    try:
        open(f'{output_base_url}/{voice}/{word}.mp3', 'wb').write(r.content)
        logging.info(f'\t Write file: {voice}/{word}.mp3')
    except:
        logging.error(f'\t ERROR: {voice}/{word}.mp3')

try:
    stories = os.listdir(f'{input_base_url}')
    random.shuffle(stories)
    for story in stories:
        chapters = os.listdir(f'{input_base_url}/{story}')
        random.shuffle(chapters)
        for chapter in chapters:
            if os.path.exists(f'{input_base_url}/{story}/{chapter}/content.txt'):
                with open(f'{input_base_url}/{story}/{chapter}/content.txt', encoding = 'utf-8') as f:
                    logging.info(f'Process file: {story}/{chapter}/content.txt')
                    text = f.read()
                    words = word_tokenize(text)
                    for word in words:
                        process_word(word, "kp")
                        process_word(word, "bg")
                        process_word(word, "bt")
except:
    pass
            


