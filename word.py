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
    'o',    'oc',           'om',   'on',   'ong',          'op',   'ot',   #o
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

HUYEN = 'huyen'
NGANG = 'ngang'
SAC = 'sac'
HOI = 'hoi'
NGA = 'nga'
NANG = 'nang'
dau = [NGANG, SAC, HUYEN, HOI, NGA, NANG]

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


def phan_tich_tu(word: str):
    """
    Phân tích từ ra phụ âm đầu, vần, dấu
    @input: luyện
    @output: {'phu_am_dau': 'l', 'van': 'uyện', 'dau': 'nang'}
    """

    _phu_am_dau = ''
    for item in phu_am_dau:
        if word.startswith(item):
            if len(item) > len(_phu_am_dau):
                _phu_am_dau = item

    _van = word[len(_phu_am_dau):]

    _dau = ''
    nguyen_am_don_dau_huyen = ['ì', 'ỳ', 'ừ', 'ù', 'ề', 'ờ', 'ầ', 'ồ', 'è', 'à', 'ằ', 'ò']
    nguyen_am_don_dau_sac = ['í', 'ý', 'ứ', 'ú', 'ế', 'ớ', 'ấ', 'ố', 'é', 'á', 'ắ', 'ó']
    nguyen_am_don_dau_hoi = ['ỉ', 'ỷ', 'ử', 'ủ', 'ể', 'ở', 'ẩ', 'ổ', 'ẻ', 'ả', 'ẳ', 'ỏ']
    nguyen_am_don_dau_nga = ['ĩ', 'ỹ', 'ữ', 'ũ', 'ễ', 'ỡ', 'ẫ', 'ỗ', 'ẽ', 'ã', 'ẵ', 'õ']
    nguyen_am_don_dau_nang = ['ị', 'ỵ', 'ự', 'ụ', 'ệ', 'ợ', 'ậ', 'ộ', 'ẹ', 'ạ', 'ặ', 'ọ']
    
    for item in nguyen_am_don_dau_huyen:
        if item in _van:
            _dau = HUYEN
            break
    if _dau == '':
        for item in nguyen_am_don_dau_sac:
            if item in _van:
                _dau = SAC
                break
    if _dau == '':
        for item in nguyen_am_don_dau_hoi:
            if item in _van:
                _dau = HOI
                break
    if _dau == '':
        for item in nguyen_am_don_dau_nga:
            if item in _van:
                _dau = NGA
                break

    if _dau == '':
        for item in nguyen_am_don_dau_nang:
            if item in _van:
                _dau = NANG
                break
    if _dau == '':
        _dau = NGANG
    return {
        "phu_am_dau": _phu_am_dau,
        "van": _van,
        "dau": _dau
    }
