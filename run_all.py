# -*- coding: utf-8 -*-
import os
import requests
import bs4
from bs4 import BeautifulSoup
import traceback
import logging
import random

from word import them_dau, phu_am_dau, van, dau

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


for p in phu_am_dau[::-1]:
    for v in van:
        for d in dau:
            van_co_dau = them_dau(v, d)
            word = p + van_co_dau
            process_word(word, "kp")
            process_word(word, "bg")
            process_word(word, "bt")
