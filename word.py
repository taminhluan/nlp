# -*- coding: utf-8 -*-
phu_am_dau = [ 'b', 'c', 'ch', 'd', 'đ', 'g', 'gh', 'gi', 'h', 'k', 'kh', 'l', 'm', 'n', 'nh', 'ng', 'ngh', 'ph', 'q', 'qu', 'r', 's', 't', 'th', 'tr', 'v', 'x' ]
phu_am_cuoi = [ 'c', 'ch', 'm', 'n', 'nh', 'ng', 'p', 't' ]
nguyen_am_don = ['i', 'y', 'ư', 'u', 'ê', 'ơ', 'â', 'ô', 'e', 'a', 'ă', 'o']

van = [
    #-      c       ch      m       n       ng      nh      p       t
    'i',    'ic',   'ich',  'im',   'in',           'inh', 'ip',   'it',    #i
    'y',                                                                #y  
    'ư',    'ưc',           'ưm',   'ưn',   'ưng',                  'ưt',   #ư
    'u',    'uc',           'um',   'un',   'ung',          'up',   'ut',   #u
    'ê',            'êch',  'êm',   'ên',           'ênh',  'êp',   'êt',   #ê
    'ơ',                    'ơm',   'ơn',                   'ơp',   'ơt',   #ơ
    'a',    'âc',           'âm',   'ân',   'âng',          'âp',   'ât',   #a
    'ô',    'ôc',           'ôm',   'ôn',   'ông',          'ôp',   'ôt',   #ô
    'e',    'ec',           'em',   'en',   'eng',          'ep',   'et',   #e
    'a',    'ac',   'ach',  'am',   'an',   'ang',  'anh',  'ap',   'at',   #a
    'ă',    'ăc',           'ăm',   'ăn',   'ăng',          'ăp',   'ăt',   #ă
    'o',     'oc',           'om',   'on',   'ong',          'op',   'ot',   #o
    #Vần hòa âm
    #-      c       ch      m       n       ng      nh      p       t
    'eo',
    'ao',
    'ai',
    'oe',
    'oa',
    'oi',
    'êu',
    'ơi',
    'ôi',
    'ia',
    'iu',
    'ưa',
    'ưi',
    'ưu',
    'ua',
    'uê',                           'uên',          'uênh',
    'ui',
    'uy',                           'uyn',                          'uyt'
    # vần hợp âm
    #i u c m n p t ng
    'oăc', 'oăm', 'oăn', 'oăt', 'oăng', #oă_ 
    'uân', 'uât', 'uâng',       #uâ_
    'iêu', 'iêc', 'iêm', 'iên', 'iêp', 'iêt', 'iêng',   #iê_
    'yêu', 'yêm', 'yên', #yê_
    'uôi', 'uôc', 'uôm', 'uôn', 'uôt', 'uông', #uô_
    'ươc', 'ươm', 'ươn', 'ươp', 'ướt', 'ương' #ươ
]

dau = ['ngang', 'sac', 'huyen', 'hoi', 'nga', 'nang']




def them_dau(van_gi, dau_gi):
    if dau_gi == 'ngang':
        return van_gi
    quy_tac_chuyen = {
        'i': [    'í',    'ì',    'ỉ',    'ĩ',    'ị'],
        'y': [    'ý',    'ỳ',    'ỷ',    'ỹ',    'ỵ'],
        'ư': [    'ứ',    'ừ',    'ử',    'ữ',    'ự'],
        'u': [    'ú',    'ù',    'ủ',    'ũ',    'ụ'],
        'ê': [    'ế',    'ề',    'ể',    'ễ',    'ệ'],
        'ơ': [    'ớ',    'ờ',    'ở',    'ỡ',    'ợ'],
        'â': [    'ấ',    'ầ',    'ẩ',    'ẫ',    'ậ'],
        'ô': [    'ố',    'ồ',    'ổ',    'ỗ',    'ộ'],
        'e': [    'é',    'ề',    'ể',    'ẽ',    'ẹ'],
        'a': [    'á',    'à',    'ả',    'ã',    'ạ'],    
        'ă': [    'ắ',    'ằ',    'ẳ',    'ẵ',    'ặ'],
        'o': [    'ó',    'ò',    'ỏ',    'õ',    'ọ']
    }
    danh_dau_tai = 0

    count_chu_cai = 0
    for chu_cai in van_gi:
        if chu_cai in nguyen_am_don:
            count_chu_cai += 1
        else:
            break
    
    if count_chu_cai == len(van_gi):
        if count_chu_cai == 1:
            danh_dau_tai = 0
    else:
        danh_dau_tai = count_chu_cai - 1
    can_chuyen = van_gi[danh_dau_tai]
    chuyen_thanh =  quy_tac_chuyen[can_chuyen][dau.index(dau_gi) - 1]

    return str(van_gi[:danh_dau_tai]) + str(chuyen_thanh) + str(van_gi[danh_dau_tai + 1:])

