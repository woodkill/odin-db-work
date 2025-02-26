from const_key import *

'''
서버목록
'''
cDIC_SERVER_INFO = {
    u'오딘01'   : {kSERVER_NAME:u'오딘01'    } ,
    u'오딘02'   : {kSERVER_NAME:u'오딘02'    } ,
    u'오딘03'   : {kSERVER_NAME:u'오딘03'    } ,
    u'오딘04'   : {kSERVER_NAME:u'오딘04'    } ,
    u'오딘05'   : {kSERVER_NAME:u'오딘05'    } ,
    u'오딘06'   : {kSERVER_NAME:u'오딘06'    } ,
    u'오딘07'   : {kSERVER_NAME:u'오딘07'    } ,
    u'오딘08'   : {kSERVER_NAME:u'오딘08'    } ,
    u'오딘09'   : {kSERVER_NAME:u'오딘09'    } ,
    u'토르01'   : {kSERVER_NAME:u'토르01'    } ,
    u'토르02'   : {kSERVER_NAME:u'토르02'    } ,
    u'토르03'   : {kSERVER_NAME:u'토르03'    } ,
    u'토르04'   : {kSERVER_NAME:u'토르04'    } ,
    u'토르05'   : {kSERVER_NAME:u'토르05'    } ,
    u'토르06'   : {kSERVER_NAME:u'토르06'    } ,
    u'토르07'   : {kSERVER_NAME:u'토르07'    } ,
    u'토르08'   : {kSERVER_NAME:u'토르08'    } ,
    u'토르09'   : {kSERVER_NAME:u'토르09'    } ,
    u'로키01'   : {kSERVER_NAME:u'로키01'    } ,
    u'로키02'   : {kSERVER_NAME:u'로키02'    } ,
    u'로키03'   : {kSERVER_NAME:u'로키03'    } ,
    u'로키04'   : {kSERVER_NAME:u'로키04'    } ,
    u'로키05'   : {kSERVER_NAME:u'로키05'    } ,
    u'로키06'   : {kSERVER_NAME:u'로키06'    } ,
    u'로키07'   : {kSERVER_NAME:u'로키07'    } ,
    u'로키08'   : {kSERVER_NAME:u'로키08'    } ,
    u'로키09'   : {kSERVER_NAME:u'로키09'    } ,
    u'프레이야01' : {kSERVER_NAME:u'프레이야01' },
    u'프레이야02' : {kSERVER_NAME:u'프레이야02' },
    u'프레이야03' : {kSERVER_NAME:u'프레이야03' },
    u'프레이야04' : {kSERVER_NAME:u'프레이야04' },
    u'프레이야05' : {kSERVER_NAME:u'프레이야05' },
    u'프레이야06' : {kSERVER_NAME:u'프레이야06' },
    u'프레이야07' : {kSERVER_NAME:u'프레이야07' },
    u'프레이야08' : {kSERVER_NAME:u'프레이야08' },
    u'프레이야09' : {kSERVER_NAME:u'프레이야09' },
    u'헤임달01'  : {kSERVER_NAME:u'헤임달01'   },
    u'헤임달02'  : {kSERVER_NAME:u'헤임달02'   },
    u'헤임달03'  : {kSERVER_NAME:u'헤임달03'   },
    u'헤임달04'  : {kSERVER_NAME:u'헤임달04'   },
    u'헤임달05'  : {kSERVER_NAME:u'헤임달05'   },
    u'헤임달06'  : {kSERVER_NAME:u'헤임달06'   },
    u'헤임달07'  : {kSERVER_NAME:u'헤임달07'   },
    u'헤임달08'  : {kSERVER_NAME:u'헤임달08'   },
    u'헤임달09'  : {kSERVER_NAME:u'헤임달09'   },
    u'티르01'   : {kSERVER_NAME:u'티르01'    } ,
    u'티르02'   : {kSERVER_NAME:u'티르02'    } ,
    u'티르03'   : {kSERVER_NAME:u'티르03'    } ,
    u'티르04'   : {kSERVER_NAME:u'티르04'    } ,
    u'티르05'   : {kSERVER_NAME:u'티르05'    } ,
    u'티르06'   : {kSERVER_NAME:u'티르06'    } ,
    u'티르07'   : {kSERVER_NAME:u'티르07'    } ,
    u'티르08'   : {kSERVER_NAME:u'티르08'    } ,
    u'티르09'   : {kSERVER_NAME:u'티르09'    } ,
    u'발두르01'  : {kSERVER_NAME:u'발두르01'   },
    u'발두르02'  : {kSERVER_NAME:u'발두르02'   },
    u'발두르03'  : {kSERVER_NAME:u'발두르03'   },
    u'발두르04'  : {kSERVER_NAME:u'발두르04'   },
    u'발두르05'  : {kSERVER_NAME:u'발두르05'   },
    u'발두르06'  : {kSERVER_NAME:u'발두르06'   },
    u'발두르07'  : {kSERVER_NAME:u'발두르07'   },
    u'발두르08'  : {kSERVER_NAME:u'발두르08'   },
    u'발두르09'  : {kSERVER_NAME:u'발두르09'   },
    u'이둔01'   : {kSERVER_NAME:u'이둔01'    } ,
    u'이둔02'   : {kSERVER_NAME:u'이둔02'    } ,
    u'이둔03'   : {kSERVER_NAME:u'이둔03'    } ,
    u'이둔04'   : {kSERVER_NAME:u'이둔04'    } ,
    u'이둔05'   : {kSERVER_NAME:u'이둔05'    } ,
    u'이둔06'   : {kSERVER_NAME:u'이둔06'    } ,
    u'이둔07'   : {kSERVER_NAME:u'이둔07'    } ,
    u'이둔08'   : {kSERVER_NAME:u'이둔08'    } ,
    u'이둔09'   : {kSERVER_NAME:u'이둔09'    } ,
    u'미미르01'  : {kSERVER_NAME:u'미미르01'   },
    u'미미르02'  : {kSERVER_NAME:u'미미르02'   },
    u'미미르03'  : {kSERVER_NAME:u'미미르03'   },
    u'미미르04'  : {kSERVER_NAME:u'미미르04'   },
    u'미미르05'  : {kSERVER_NAME:u'미미르05'   },
    u'미미르06'  : {kSERVER_NAME:u'미미르06'   },
    u'미미르07'  : {kSERVER_NAME:u'미미르07'   },
    u'미미르08'  : {kSERVER_NAME:u'미미르08'   },
    u'미미르09'  : {kSERVER_NAME:u'미미르09'   },
    u'수르트01'  : {kSERVER_NAME:u'수르트01'   },
    u'수르트02'  : {kSERVER_NAME:u'수르트02'   },
    u'수르트03'  : {kSERVER_NAME:u'수르트03'   },
    u'수르트04'  : {kSERVER_NAME:u'수르트04'   },
    u'수르트05'  : {kSERVER_NAME:u'수르트05'   },
    u'수르트06'  : {kSERVER_NAME:u'수르트06'   },
    u'수르트07'  : {kSERVER_NAME:u'수르트07'   },
    u'수르트08'  : {kSERVER_NAME:u'수르트08'   },
    u'수르트09'  : {kSERVER_NAME:u'수르트09'   },
    u'에기르01'  : {kSERVER_NAME:u'에기르01'   },
    u'에기르02'  : {kSERVER_NAME:u'에기르02'   },
    u'에기르03'  : {kSERVER_NAME:u'에기르03'   },
    u'에기르04'  : {kSERVER_NAME:u'에기르04'   },
    u'에기르05'  : {kSERVER_NAME:u'에기르05'   },
    u'에기르06'  : {kSERVER_NAME:u'에기르06'   },
}


'''
보스타입
'''
cBOSS_TYPE_DAILY_FIXED = 0
cBOSS_TYPE_INTERVAL = 1
cBOSS_TYPE_WEEKDAY_FIXED = 2

'''
요일
'''
cWEEKDAYS = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']

'''
보스정보
'''
cDIC_BOSS_INFO = {
    # 던전
    '000':{kCHAP_ORDER: 0, kCHAP_NAME: u'던전', kBOSS_LEVEL:'지배자', kBOSS_ORDER:0, kBOSS_TYPE:cBOSS_TYPE_INTERVAL, kBOSS_INTERVAL: '01:12:00', kBOSS_NAME: u'최하층굴베이그' , kBOSS_ALIAS:[u'혼돈의마수굴베이그', u'최하층굴베이그', u'최하층굴베', u'최하층5']},
    '001':{kCHAP_ORDER: 0, kCHAP_NAME: u'던전', kBOSS_LEVEL:'지배자', kBOSS_ORDER:1, kBOSS_TYPE:cBOSS_TYPE_INTERVAL, kBOSS_INTERVAL: '01:12:00', kBOSS_NAME: u'최하층강글로티' , kBOSS_ALIAS:[u'혼돈의사제강글로티', u'최하층강글로티', u'강글', u'최하층막']},
    '002':{kCHAP_ORDER: 0, kCHAP_NAME: u'던전', kBOSS_LEVEL:'지배자', kBOSS_ORDER:2, kBOSS_TYPE:cBOSS_TYPE_INTERVAL, kBOSS_INTERVAL: '00:12:00', kBOSS_NAME: u'4층모네가름'    , kBOSS_ALIAS:[u'분노의모네가름', u'4층모네가름', u'4층']},
    '003':{kCHAP_ORDER: 0, kCHAP_NAME: u'던전', kBOSS_LEVEL:'지배자', kBOSS_ORDER:3, kBOSS_TYPE:cBOSS_TYPE_INTERVAL, kBOSS_INTERVAL: '00:24:00', kBOSS_NAME: u'7층드라우그'    , kBOSS_ALIAS:[u'나태의드라우그', u'7층드라우그', u'7층']},
    '004':{kCHAP_ORDER: 0, kCHAP_NAME: u'던전', kBOSS_LEVEL:'지배자', kBOSS_ORDER:3, kBOSS_TYPE:cBOSS_TYPE_INTERVAL, kBOSS_INTERVAL: '02:00:00', kBOSS_NAME: u'최하층스네르'   , kBOSS_ALIAS:[u'혼돈의참수자스네르', u'최하층스네르', u'스네르']},
    '005':{kCHAP_ORDER: 0, kCHAP_NAME: u'던전', kBOSS_LEVEL:'지배자', kBOSS_ORDER:3, kBOSS_TYPE:cBOSS_TYPE_INTERVAL, kBOSS_INTERVAL: '00:24:00', kBOSS_NAME: u'10층흘로크'     , kBOSS_ALIAS: [u'기만의기사다인흘로크', u'10층흘로크', u'10층', u'흘로크']},
    # 성채
    '1000':{kCHAP_ORDER: 10, kCHAP_NAME: u'성채', kBOSS_LEVEL:'지배자', kBOSS_ORDER:0, kBOSS_TYPE:cBOSS_TYPE_WEEKDAY_FIXED, kBOSS_WEEKDAY_INFO: [{kBOSS_WEEKDAY:1, kBOSS_APPEARANCE_TIME:"21:30"}, {kBOSS_WEEKDAY:3, kBOSS_APPEARANCE_TIME:"21:30"}], kBOSS_NAME: u'그로아의사념'        , kBOSS_ALIAS:[u'그로아의사념', u'성채그로아', u'성채2', u'성채2층']},
    '1001':{kCHAP_ORDER: 10, kCHAP_NAME: u'성채', kBOSS_LEVEL:'지배자', kBOSS_ORDER:1, kBOSS_TYPE:cBOSS_TYPE_WEEKDAY_FIXED, kBOSS_WEEKDAY_INFO: [{kBOSS_WEEKDAY:1, kBOSS_APPEARANCE_TIME:"21:30"}, {kBOSS_WEEKDAY:3, kBOSS_APPEARANCE_TIME:"21:30"}], kBOSS_NAME: u'헤르모드의사념'      , kBOSS_ALIAS:[u'헤르모드의사념', u'성채헤르', u'성채헤르모드', u'성채3', u'성채3층']},
    '1002':{kCHAP_ORDER: 10, kCHAP_NAME: u'성채', kBOSS_LEVEL:'지배자', kBOSS_ORDER:2, kBOSS_TYPE:cBOSS_TYPE_WEEKDAY_FIXED, kBOSS_WEEKDAY_INFO: [{kBOSS_WEEKDAY:1, kBOSS_APPEARANCE_TIME:"21:30"}, {kBOSS_WEEKDAY:3, kBOSS_APPEARANCE_TIME:"21:30"}], kBOSS_NAME: u'야른의사념'          , kBOSS_ALIAS:[u'야른의사념', u'성채야른', u'성채4', u'성채4층']},
    '1003':{kCHAP_ORDER: 10, kCHAP_NAME: u'성채', kBOSS_LEVEL:'지배자', kBOSS_ORDER:3, kBOSS_TYPE:cBOSS_TYPE_WEEKDAY_FIXED, kBOSS_WEEKDAY_INFO: [{kBOSS_WEEKDAY:1, kBOSS_APPEARANCE_TIME:"21:30"}, {kBOSS_WEEKDAY:3, kBOSS_APPEARANCE_TIME:"21:30"}], kBOSS_NAME: u'굴베이그의사념'      , kBOSS_ALIAS:[u'굴베이그의사념', u'성채굴베', u'성채굴베이그', u'성채5', u'성채5층']},
    '1004':{kCHAP_ORDER: 10, kCHAP_NAME: u'성채', kBOSS_LEVEL:'지배자', kBOSS_ORDER:4, kBOSS_TYPE:cBOSS_TYPE_WEEKDAY_FIXED, kBOSS_WEEKDAY_INFO: [{kBOSS_WEEKDAY:1, kBOSS_APPEARANCE_TIME:"21:30"}, {kBOSS_WEEKDAY:3, kBOSS_APPEARANCE_TIME:"21:30"}], kBOSS_NAME: u'천둥군주수드리의사념', kBOSS_ALIAS:[u'천둥군주수드리의사념', u'성채수드리', u'성채6', u'성채6층']},
    '1005':{kCHAP_ORDER: 10, kCHAP_NAME: u'성채', kBOSS_LEVEL:'지배자', kBOSS_ORDER:4, kBOSS_TYPE:cBOSS_TYPE_WEEKDAY_FIXED, kBOSS_WEEKDAY_INFO: [{kBOSS_WEEKDAY:1, kBOSS_APPEARANCE_TIME:"21:30"}, {kBOSS_WEEKDAY:3, kBOSS_APPEARANCE_TIME:"21:30"}], kBOSS_NAME: u'린베스트의사념'      , kBOSS_ALIAS:[u'린베스트의사념', u'린베', u'린베스트', u'성채7', u'성채7층']},
    '1006':{kCHAP_ORDER: 10, kCHAP_NAME: u'성채', kBOSS_LEVEL:'지배자', kBOSS_ORDER:4, kBOSS_TYPE:cBOSS_TYPE_WEEKDAY_FIXED, kBOSS_WEEKDAY_INFO: [{kBOSS_WEEKDAY:1, kBOSS_APPEARANCE_TIME:"21:30"}, {kBOSS_WEEKDAY:3, kBOSS_APPEARANCE_TIME:"21:30"}], kBOSS_NAME: u'파프니르의그림자'    , kBOSS_ALIAS:[u'파프니르의그림자', u'성채파프', u'성채파프니르', u'성채8', u'성채8층']},
    # 미스가르드
    '100':{kCHAP_ORDER: 20, kCHAP_NAME: u'미스가르드', kBOSS_LEVEL:'지배자', kBOSS_ORDER:0, kBOSS_TYPE: cBOSS_TYPE_INTERVAL, kBOSS_INTERVAL: '00:00:10', kBOSS_NAME: u'그로아'             , kBOSS_ALIAS:[u'그로아']},
    '101':{kCHAP_ORDER: 20, kCHAP_NAME: u'미스가르드', kBOSS_LEVEL:'지배자', kBOSS_ORDER:1, kBOSS_TYPE: cBOSS_TYPE_INTERVAL, kBOSS_INTERVAL: '00:00:10', kBOSS_NAME: u'칼바람하피'         , kBOSS_ALIAS:[u'칼바람하피', u'하피']},
    '102':{kCHAP_ORDER: 20, kCHAP_NAME: u'미스가르드', kBOSS_LEVEL:'지배자', kBOSS_ORDER:2, kBOSS_TYPE: cBOSS_TYPE_INTERVAL, kBOSS_INTERVAL: '00:00:10', kBOSS_NAME: u'매트리악'           , kBOSS_ALIAS:[u'매트리악', u'매트']},
    '103':{kCHAP_ORDER: 20, kCHAP_NAME: u'미스가르드', kBOSS_LEVEL:'지배자', kBOSS_ORDER:3, kBOSS_TYPE: cBOSS_TYPE_INTERVAL, kBOSS_INTERVAL: '00:00:10', kBOSS_NAME: u'레라드'             , kBOSS_ALIAS:[u'레라드']},
    '104':{kCHAP_ORDER: 20, kCHAP_NAME: u'미스가르드', kBOSS_LEVEL:'지배자', kBOSS_ORDER:4, kBOSS_TYPE: cBOSS_TYPE_INTERVAL, kBOSS_INTERVAL: '00:00:10', kBOSS_NAME: u'탕그뇨스트'         , kBOSS_ALIAS:[u'탕그뇨스트']},
    # 요툰하임
    '200':{kCHAP_ORDER: 30, kCHAP_NAME: u'요툰하임', kBOSS_LEVEL:'지배자'  , kBOSS_ORDER:0, kBOSS_TYPE: cBOSS_TYPE_INTERVAL, kBOSS_INTERVAL: '00:12:00', kBOSS_NAME: u'파르바'             , kBOSS_ALIAS:[u'파르바']},
    '201':{kCHAP_ORDER: 30, kCHAP_NAME: u'요툰하임', kBOSS_LEVEL:'지배자'  , kBOSS_ORDER:1, kBOSS_TYPE: cBOSS_TYPE_INTERVAL, kBOSS_INTERVAL: '00:12:00', kBOSS_NAME: u'셀로비아'           , kBOSS_ALIAS:[u'셀로비아', u'셀로']},
    '202':{kCHAP_ORDER: 30, kCHAP_NAME: u'요툰하임', kBOSS_LEVEL:'지배자'  , kBOSS_ORDER:2, kBOSS_TYPE: cBOSS_TYPE_INTERVAL, kBOSS_INTERVAL: '00:12:00', kBOSS_NAME: u'흐니르'             , kBOSS_ALIAS:[u'흐니르']},
    '203':{kCHAP_ORDER: 30, kCHAP_NAME: u'요툰하임', kBOSS_LEVEL:'지배자'  , kBOSS_ORDER:3, kBOSS_TYPE: cBOSS_TYPE_INTERVAL, kBOSS_INTERVAL: '00:12:00', kBOSS_NAME: u'페티'               , kBOSS_ALIAS:[u'페티', u'패티']},
    '204':{kCHAP_ORDER: 30, kCHAP_NAME: u'요툰하임', kBOSS_LEVEL:'지배자'  , kBOSS_ORDER:4, kBOSS_TYPE: cBOSS_TYPE_INTERVAL, kBOSS_INTERVAL: '00:12:00', kBOSS_NAME: u'바우티'             , kBOSS_ALIAS:[u'바우티']},
    '205':{kCHAP_ORDER: 30, kCHAP_NAME: u'요툰하임', kBOSS_LEVEL:'지배자'  , kBOSS_ORDER:5, kBOSS_TYPE: cBOSS_TYPE_INTERVAL, kBOSS_INTERVAL: '00:12:00', kBOSS_NAME: u'니드호그'           , kBOSS_ALIAS:[u'니드호그', u'니드']},
    '206':{kCHAP_ORDER: 30, kCHAP_NAME: u'요툰하임', kBOSS_LEVEL:'지배자'  , kBOSS_ORDER:6, kBOSS_TYPE: cBOSS_TYPE_INTERVAL, kBOSS_INTERVAL: '00:12:00', kBOSS_NAME: u'야른'               , kBOSS_ALIAS:[u'야른']},
    '207':{kCHAP_ORDER: 30, kCHAP_NAME: u'요툰하임', kBOSS_LEVEL:'절대자'  , kBOSS_ORDER:0, kBOSS_TYPE: cBOSS_TYPE_INTERVAL, kBOSS_INTERVAL: '03:00:00', kBOSS_NAME: u'티르'               , kBOSS_ALIAS:[u'티르']},
    '208':{kCHAP_ORDER: 30, kCHAP_NAME: u'요툰하임', kBOSS_LEVEL:'대륙침략자', kBOSS_ORDER:0, kBOSS_TYPE: cBOSS_TYPE_DAILY_FIXED, kBOSS_FIXED_TIME: ["12:00", "22:00"], kBOSS_NAME: u'가름'               , kBOSS_ALIAS:[u'갸름', u'가름']},
    # 니다벨리르
    '300':{kCHAP_ORDER: 40, kCHAP_NAME: u'니다벨리르', kBOSS_LEVEL:'지배자', kBOSS_ORDER:0, kBOSS_TYPE: cBOSS_TYPE_INTERVAL, kBOSS_INTERVAL: '00:12:00', kBOSS_NAME: u'라이노르'           , kBOSS_ALIAS:[u'라이노르', u'라이']},
    '301':{kCHAP_ORDER: 40, kCHAP_NAME: u'니다벨리르', kBOSS_LEVEL:'지배자', kBOSS_ORDER:1, kBOSS_TYPE: cBOSS_TYPE_INTERVAL, kBOSS_INTERVAL: '00:12:00', kBOSS_NAME: u'비요른'             , kBOSS_ALIAS:[u'비요른']},
    '302':{kCHAP_ORDER: 40, kCHAP_NAME: u'니다벨리르', kBOSS_LEVEL:'지배자', kBOSS_ORDER:2, kBOSS_TYPE: cBOSS_TYPE_INTERVAL, kBOSS_INTERVAL: '00:12:00', kBOSS_NAME: u'헤르모드'           , kBOSS_ALIAS:[u'헤르모드']},
    '303':{kCHAP_ORDER: 40, kCHAP_NAME: u'니다벨리르', kBOSS_LEVEL:'지배자', kBOSS_ORDER:3, kBOSS_TYPE: cBOSS_TYPE_INTERVAL, kBOSS_INTERVAL: '00:12:00', kBOSS_NAME: u'스칼라니르'         , kBOSS_ALIAS:[u'스칼라니르']},
    '304':{kCHAP_ORDER: 40, kCHAP_NAME: u'니다벨리르', kBOSS_LEVEL:'지배자', kBOSS_ORDER:4, kBOSS_TYPE: cBOSS_TYPE_INTERVAL, kBOSS_INTERVAL: '00:12:00', kBOSS_NAME: u'브륀힐드'           , kBOSS_ALIAS:[u'브륀힐드', u'브린힐드', u'브륀', u'브린']},
    '305':{kCHAP_ORDER: 40, kCHAP_NAME: u'니다벨리르', kBOSS_LEVEL:'지배자', kBOSS_ORDER:5, kBOSS_TYPE: cBOSS_TYPE_INTERVAL, kBOSS_INTERVAL: '00:12:00', kBOSS_NAME: u'라타토스크'         , kBOSS_ALIAS:[u'라타토스크', u'라타']},
    '306':{kCHAP_ORDER: 40, kCHAP_NAME: u'니다벨리르', kBOSS_LEVEL:'지배자', kBOSS_ORDER:6, kBOSS_TYPE: cBOSS_TYPE_INTERVAL, kBOSS_INTERVAL: '00:12:00', kBOSS_NAME: u'수드리'             , kBOSS_ALIAS:[u'수드리']},
    '307':{kCHAP_ORDER: 40, kCHAP_NAME: u'니다벨리르', kBOSS_LEVEL:'절대자', kBOSS_ORDER:0, kBOSS_TYPE: cBOSS_TYPE_INTERVAL, kBOSS_INTERVAL: '03:00:00', kBOSS_NAME: u'토르'               , kBOSS_ALIAS:[u'토르']},
    '308':{kCHAP_ORDER: 40, kCHAP_NAME: u'니다벨리르', kBOSS_LEVEL:'대륙침략자', kBOSS_ORDER:0, kBOSS_TYPE: cBOSS_TYPE_DAILY_FIXED, kBOSS_FIXED_TIME: ["12:00", "22:00"], kBOSS_NAME: u'발두르'             , kBOSS_ALIAS:[u'발두르']},
    # 알브하임
    '400':{kCHAP_ORDER: 50, kCHAP_NAME: u'알브하임', kBOSS_LEVEL:'지배자', kBOSS_ORDER:0, kBOSS_TYPE: cBOSS_TYPE_INTERVAL, kBOSS_INTERVAL: '00:24:00', kBOSS_NAME: u'스바르트'           , kBOSS_ALIAS:[u'스바르트', u'스바']},
    '401':{kCHAP_ORDER: 50, kCHAP_NAME: u'알브하임', kBOSS_LEVEL:'지배자', kBOSS_ORDER:1, kBOSS_TYPE: cBOSS_TYPE_INTERVAL, kBOSS_INTERVAL: '00:24:00', kBOSS_NAME: u'두라스로르'         , kBOSS_ALIAS:[u'두라스로르', u'두라']},
    '402':{kCHAP_ORDER: 50, kCHAP_NAME: u'알브하임', kBOSS_LEVEL:'지배자', kBOSS_ORDER:2, kBOSS_TYPE: cBOSS_TYPE_INTERVAL, kBOSS_INTERVAL: '00:24:00', kBOSS_NAME: u'모네가름'           , kBOSS_ALIAS:[u'모네가름', u'모내가름', u'모네', u'모내']},
    '403':{kCHAP_ORDER: 50, kCHAP_NAME: u'알브하임', kBOSS_LEVEL:'지배자', kBOSS_ORDER:3, kBOSS_TYPE: cBOSS_TYPE_INTERVAL, kBOSS_INTERVAL: '00:24:00', kBOSS_NAME: u'드라우그'           , kBOSS_ALIAS:[u'드라우그', u'드라']},
    '404':{kCHAP_ORDER: 50, kCHAP_NAME: u'알브하임', kBOSS_LEVEL:'지배자', kBOSS_ORDER:4, kBOSS_TYPE: cBOSS_TYPE_INTERVAL, kBOSS_INTERVAL: '00:24:00', kBOSS_NAME: u'굴베이그'           , kBOSS_ALIAS:[u'굴베이그', u'굴배이그', u'굴베', u'굴배']},
    '405':{kCHAP_ORDER: 50, kCHAP_NAME: u'알브하임', kBOSS_LEVEL:'절대자', kBOSS_ORDER:0, kBOSS_TYPE: cBOSS_TYPE_INTERVAL, kBOSS_INTERVAL: '03:00:00', kBOSS_NAME: u'오딘'               , kBOSS_ALIAS:[u'오딘']},
    '406':{kCHAP_ORDER: 50, kCHAP_NAME: u'알브하임', kBOSS_LEVEL:'대륙침략자', kBOSS_ORDER:0, kBOSS_TYPE: cBOSS_TYPE_DAILY_FIXED, kBOSS_FIXED_TIME: ["12:00", "22:00"], kBOSS_NAME: u'파프니르'           , kBOSS_ALIAS:[u'파르']},
    # 무스펠하임
    '500':{kCHAP_ORDER: 60, kCHAP_NAME: u'무스펠하임', kBOSS_LEVEL:'지배자', kBOSS_ORDER:0, kBOSS_TYPE: cBOSS_TYPE_INTERVAL, kBOSS_INTERVAL: '00:36:00', kBOSS_NAME: u'메기르'             , kBOSS_ALIAS:[u'메기르', u'매기르']},
    '501':{kCHAP_ORDER: 60, kCHAP_NAME: u'무스펠하임', kBOSS_LEVEL:'지배자', kBOSS_ORDER:1, kBOSS_TYPE: cBOSS_TYPE_INTERVAL, kBOSS_INTERVAL: '00:36:00', kBOSS_NAME: u'신마라'             , kBOSS_ALIAS:[u'신마라']},
    '502':{kCHAP_ORDER: 60, kCHAP_NAME: u'무스펠하임', kBOSS_LEVEL:'지배자', kBOSS_ORDER:2, kBOSS_TYPE: cBOSS_TYPE_INTERVAL, kBOSS_INTERVAL: '00:36:00', kBOSS_NAME: u'헤르가름'           , kBOSS_ALIAS:[u'헤르가름', u'헤르']},
    '503':{kCHAP_ORDER: 60, kCHAP_NAME: u'무스펠하임', kBOSS_LEVEL:'지배자', kBOSS_ORDER:3, kBOSS_TYPE: cBOSS_TYPE_INTERVAL, kBOSS_INTERVAL: '00:36:00', kBOSS_NAME: u'탕그리스니르'       , kBOSS_ALIAS:[u'탕그리스니르', u'탕그']},
    '504':{kCHAP_ORDER: 60, kCHAP_NAME: u'무스펠하임', kBOSS_LEVEL:'지배자', kBOSS_ORDER:4, kBOSS_TYPE: cBOSS_TYPE_INTERVAL, kBOSS_INTERVAL: '00:36:00', kBOSS_NAME: u'엘드룬'             , kBOSS_ALIAS:[u'엘드룬', u'앨드룬', u'엘드', u'앨드']},
    '505':{kCHAP_ORDER: 60, kCHAP_NAME: u'무스펠하임', kBOSS_LEVEL:'지배자', kBOSS_ORDER:5, kBOSS_TYPE: cBOSS_TYPE_INTERVAL, kBOSS_INTERVAL: '00:36:00', kBOSS_NAME: u'우로보로스'         , kBOSS_ALIAS:[u'우로보로스', u'우로']},
    '506':{kCHAP_ORDER: 60, kCHAP_NAME: u'무스펠하임', kBOSS_LEVEL:'절대자', kBOSS_ORDER:0, kBOSS_TYPE: cBOSS_TYPE_INTERVAL, kBOSS_INTERVAL: '03:00:00', kBOSS_NAME: u'수르트'             , kBOSS_ALIAS:[u'수르트']},
    '507':{kCHAP_ORDER: 60, kCHAP_NAME: u'무스펠하임', kBOSS_LEVEL:'대륙침략자', kBOSS_ORDER:0, kBOSS_TYPE: cBOSS_TYPE_DAILY_FIXED, kBOSS_FIXED_TIME: ["12:00", "22:00"], kBOSS_NAME: u'아우둠라'           , kBOSS_ALIAS:[u'둠라']},
    # 아스가르드
    '600':{kCHAP_ORDER: 70, kCHAP_NAME: u'아스가르드', kBOSS_LEVEL:'지배자', kBOSS_ORDER:0, kBOSS_TYPE: cBOSS_TYPE_INTERVAL, kBOSS_INTERVAL: '00:48:00', kBOSS_NAME: u'발리'               , kBOSS_ALIAS:[u'발리']},
    '601':{kCHAP_ORDER: 70, kCHAP_NAME: u'아스가르드', kBOSS_LEVEL:'지배자', kBOSS_ORDER:1, kBOSS_TYPE: cBOSS_TYPE_INTERVAL, kBOSS_INTERVAL: '00:48:00', kBOSS_NAME: u'노트'               , kBOSS_ALIAS:[u'노트']},
    '602':{kCHAP_ORDER: 70, kCHAP_NAME: u'아스가르드', kBOSS_LEVEL:'지배자', kBOSS_ORDER:2, kBOSS_TYPE: cBOSS_TYPE_INTERVAL, kBOSS_INTERVAL: '00:48:00', kBOSS_NAME: u'샤무크'             , kBOSS_ALIAS:[u'샤무크']},
    '603':{kCHAP_ORDER: 70, kCHAP_NAME: u'아스가르드', kBOSS_LEVEL:'지배자', kBOSS_ORDER:3, kBOSS_TYPE: cBOSS_TYPE_INTERVAL, kBOSS_INTERVAL: '00:48:00', kBOSS_NAME: u'스칼드메르'         , kBOSS_ALIAS:[u'스칼드메르', u'스칼']},
    '604':{kCHAP_ORDER: 70, kCHAP_NAME: u'아스가르드', kBOSS_LEVEL:'지배자', kBOSS_ORDER:4, kBOSS_TYPE: cBOSS_TYPE_INTERVAL, kBOSS_INTERVAL: '00:48:00', kBOSS_NAME: u'화신그로아'         , kBOSS_ALIAS:[u'화신그로아', u'화신']},
    '605':{kCHAP_ORDER: 70, kCHAP_NAME: u'아스가르드', kBOSS_LEVEL:'절대자', kBOSS_ORDER:0, kBOSS_TYPE: cBOSS_TYPE_INTERVAL, kBOSS_INTERVAL: '03:00:00', kBOSS_NAME: u'미미르'             , kBOSS_ALIAS:[u'미미르']},
    '606':{kCHAP_ORDER: 70, kCHAP_NAME: u'아스가르드', kBOSS_LEVEL:'대륙침략자', kBOSS_ORDER:0, kBOSS_TYPE: cBOSS_TYPE_DAILY_FIXED, kBOSS_FIXED_TIME: ["12:00", "22:00"], kBOSS_NAME: u'헤임달'             , kBOSS_ALIAS:[u'헤임달', u'해임달']},
    # 니플하임
    '700':{kCHAP_ORDER: 80, kCHAP_NAME: u'니플하임', kBOSS_LEVEL:'지배자', kBOSS_ORDER:0, kBOSS_TYPE: cBOSS_TYPE_INTERVAL, kBOSS_INTERVAL: '00:60:00', kBOSS_NAME: u'히로킨'               , kBOSS_ALIAS:[u'히로킨']},
    '701':{kCHAP_ORDER: 80, kCHAP_NAME: u'니플하임', kBOSS_LEVEL:'지배자', kBOSS_ORDER:1, kBOSS_TYPE: cBOSS_TYPE_INTERVAL, kBOSS_INTERVAL: '00:60:00', kBOSS_NAME: u'호드'                 , kBOSS_ALIAS:[u'호드']},
    '702':{kCHAP_ORDER: 80, kCHAP_NAME: u'니플하임', kBOSS_LEVEL:'지배자', kBOSS_ORDER:2, kBOSS_TYPE: cBOSS_TYPE_INTERVAL, kBOSS_INTERVAL: '00:60:00', kBOSS_NAME: u'헤이드'               , kBOSS_ALIAS:[u'헤이드']},
    '703':{kCHAP_ORDER: 80, kCHAP_NAME: u'니플하임', kBOSS_LEVEL:'지배자', kBOSS_ORDER:3, kBOSS_TYPE: cBOSS_TYPE_INTERVAL, kBOSS_INTERVAL: '00:60:00', kBOSS_NAME: u'대교주프레이'         , kBOSS_ALIAS:[u'대교주프레이', u'프레이']},
    '704':{kCHAP_ORDER: 80, kCHAP_NAME: u'니플하임', kBOSS_LEVEL:'절대자', kBOSS_ORDER:0, kBOSS_TYPE: cBOSS_TYPE_INTERVAL, kBOSS_INTERVAL: '03:00:00', kBOSS_NAME: u'이미르'               , kBOSS_ALIAS:[u'이미르']},
    '705':{kCHAP_ORDER: 80, kCHAP_NAME: u'니플하임', kBOSS_LEVEL:'대륙침략자', kBOSS_ORDER:0, kBOSS_TYPE: cBOSS_TYPE_DAILY_FIXED, kBOSS_FIXED_TIME: ["12:00", "22:00"], kBOSS_NAME: u'타락한이둔'             , kBOSS_ALIAS:[u'타락한이둔', u'이둔']},
    # 바나하임
    '800':{kCHAP_ORDER: 90, kCHAP_NAME: u'바나하임', kBOSS_LEVEL:'지배자', kBOSS_ORDER:0, kBOSS_TYPE: cBOSS_TYPE_INTERVAL, kBOSS_INTERVAL: '00:60:00', kBOSS_NAME: u'엘디르'               , kBOSS_ALIAS:[u'엘디르']},
    '801':{kCHAP_ORDER: 90, kCHAP_NAME: u'바나하임', kBOSS_LEVEL:'지배자', kBOSS_ORDER:1, kBOSS_TYPE: cBOSS_TYPE_INTERVAL, kBOSS_INTERVAL: '00:60:00', kBOSS_NAME: u'스카디'               , kBOSS_ALIAS:[u'스카디']},
    '802':{kCHAP_ORDER: 90, kCHAP_NAME: u'바나하임', kBOSS_LEVEL:'지배자', kBOSS_ORDER:2, kBOSS_TYPE: cBOSS_TYPE_INTERVAL, kBOSS_INTERVAL: '00:60:00', kBOSS_NAME: u'안나르엘디르'         , kBOSS_ALIAS:[u'안나르']},
    '803':{kCHAP_ORDER: 90, kCHAP_NAME: u'바나하임', kBOSS_LEVEL:'지배자', kBOSS_ORDER:3, kBOSS_TYPE: cBOSS_TYPE_INTERVAL, kBOSS_INTERVAL: '00:60:00', kBOSS_NAME: u'스쿨드'               , kBOSS_ALIAS:[u'스쿨드', u'스쿨']},
    '804':{kCHAP_ORDER: 90, kCHAP_NAME: u'바나하임', kBOSS_LEVEL:'절대자', kBOSS_ORDER:0, kBOSS_TYPE: cBOSS_TYPE_INTERVAL, kBOSS_INTERVAL: '03:00:00', kBOSS_NAME: u'에기르'               , kBOSS_ALIAS:[u'에기르']},
    '805':{kCHAP_ORDER: 90, kCHAP_NAME: u'바나하임', kBOSS_LEVEL:'대륙침략자', kBOSS_ORDER:0, kBOSS_TYPE: cBOSS_TYPE_DAILY_FIXED, kBOSS_FIXED_TIME: ["12:00", "22:00"], kBOSS_NAME: u'알수없음'             , kBOSS_ALIAS:[u'몰라']},
}

cCHAPTER_BOSS_INFO = [
    {
        kCHAP_NO: "1챕",
        kCHAP_NAME: "미드가르드",
        kCHAP_ALIAS: "미드",
        kCHAP_COLOR_CODE: '\x1b[37m',
        kCLICK_POS_S: {kX:493, kY:345},
        kCLICK_POS: {kX: 680, kY: 460},
        kBOSS_LIST: [  # 보스정보 목록
            {kBOSS_NAME: "그로아", kBOSS_SUPREME: False},
            {kBOSS_NAME: "칼바람하피", kBOSS_SUPREME: False},
            {kBOSS_NAME: "매트리악", kBOSS_SUPREME: False},
            {kBOSS_NAME: "레라드", kBOSS_SUPREME: False},
            {kBOSS_NAME: "탕그뇨스트", kBOSS_SUPREME: False}
        ]
    },
    {
        kCHAP_NO: "2챕",
        kCHAP_NAME: "요툰하임",
        kCHAP_ALIAS: "요툰",
        kCHAP_COLOR_CODE: '\x1b[37m',
        kCLICK_POS_S: {kX:589, kY:345},
        kCLICK_POS: {kX: 785, kY: 460},
        kBOSS_LIST: [  # 보스정보 목록
            {kBOSS_NAME: "파르바", kBOSS_SUPREME: False},
            {kBOSS_NAME: "셀로비아", kBOSS_SUPREME: False},
            {kBOSS_NAME: "흐니르", kBOSS_SUPREME: False},
            {kBOSS_NAME: "페티", kBOSS_SUPREME: False},
            {kBOSS_NAME: "바우티", kBOSS_SUPREME: False},
            {kBOSS_NAME: "니드호그", kBOSS_SUPREME: False},
            {kBOSS_NAME: "야른", kBOSS_SUPREME: False},
            {kBOSS_NAME: "티르", kBOSS_SUPREME: True}
        ]
    },
    {
        kCHAP_NO: "3챕",
        kCHAP_NAME: "니다벨리르",
        kCHAP_ALIAS: "니다",
        kCHAP_COLOR_CODE: '\x1b[34m',
        kCLICK_POS_S: {kX:684, kY:345},
        kCLICK_POS: {kX: 895, kY: 460},
        kBOSS_LIST: [  # 보스정보 목록
            {kBOSS_NAME: "라이노르", kBOSS_SUPREME: False},
            {kBOSS_NAME: "비요른", kBOSS_SUPREME: False},
            {kBOSS_NAME: "헤르모드", kBOSS_SUPREME: False},
            {kBOSS_NAME: "스칼라니르", kBOSS_SUPREME: False},
            {kBOSS_NAME: "브륀힐드", kBOSS_SUPREME: False},
            {kBOSS_NAME: "라타토스크", kBOSS_SUPREME: False},
            {kBOSS_NAME: "수드리", kBOSS_SUPREME: False},
            {kBOSS_NAME: "토르", kBOSS_SUPREME: True}
        ]
    },
    {
        kCHAP_NO: "4챕",
        kCHAP_NAME: "알브하임",
        kCHAP_ALIAS: "알브",
        kCHAP_COLOR_CODE: '\x1b[32m',
        kCLICK_POS_S: {kX:779, kY:345},
        kCLICK_POS: {kX: 1000, kY: 460},
        kBOSS_LIST: [  # 보스정보 목록
            {kBOSS_NAME: "스바르트", kBOSS_SUPREME: False},
            {kBOSS_NAME: "두라스로르", kBOSS_SUPREME: False},
            {kBOSS_NAME: "모네가름", kBOSS_SUPREME: False},
            {kBOSS_NAME: "드라우그", kBOSS_SUPREME: False},
            {kBOSS_NAME: "굴베이그", kBOSS_SUPREME: False},
            {kBOSS_NAME: "오딘", kBOSS_SUPREME: True}
        ]
    },
    {
        kCHAP_NO: "5챕",
        kCHAP_NAME: "무스펠하임",
        kCHAP_ALIAS: "무스펠",
        kCHAP_COLOR_CODE: '\x1b[31m',
        kCLICK_POS_S: {kX:875, kY:345},
        kCLICK_POS: {kX: 1110, kY: 460},
        kBOSS_LIST: [  # 보스정보 목록
            {kBOSS_NAME: "메기르", kBOSS_SUPREME: False},
            {kBOSS_NAME: "신마라", kBOSS_SUPREME: False},
            {kBOSS_NAME: "헤르가름", kBOSS_SUPREME: False},
            {kBOSS_NAME: "탕그리스니르", kBOSS_SUPREME: False},
            {kBOSS_NAME: "엘드룬", kBOSS_SUPREME: False},
            {kBOSS_NAME: "우로보로스", kBOSS_SUPREME: False},
            {kBOSS_NAME: "수르트", kBOSS_SUPREME: True}
        ]
    },
    {
        kCHAP_NO: "6챕",
        kCHAP_NAME: "아스가르드",
        kCHAP_ALIAS: "아스",
        kCHAP_COLOR_CODE: '\x1b[33m',
        kCLICK_POS_S: {kX:969, kY:345},
        kCLICK_POS: {kX: 1215, kY: 460},
        kBOSS_LIST: [  # 보스정보 목록
            {kBOSS_NAME: "발리", kBOSS_SUPREME: False},
            {kBOSS_NAME: "노트", kBOSS_SUPREME: False},
            {kBOSS_NAME: "샤무크", kBOSS_SUPREME: False},
            {kBOSS_NAME: "스칼드메르", kBOSS_SUPREME: False},
            {kBOSS_NAME: "화신그로아", kBOSS_SUPREME: False},
            {kBOSS_NAME: "미미르", kBOSS_SUPREME: True}
        ]
    },
    {
        kCHAP_NO: "7챕",
        kCHAP_NAME: "니플하임",
        kCHAP_ALIAS: "니플",
        kCHAP_COLOR_CODE: '\x1b[32m',
        kCLICK_POS_S: {kX:1064, kY:345},
        kCLICK_POS: {kX: 1325, kY: 460},
        kBOSS_LIST: [  # 보스정보 목록
            {kBOSS_NAME: "히로킨", kBOSS_SUPREME: False},
            {kBOSS_NAME: "호드", kBOSS_SUPREME: False},
            {kBOSS_NAME: "헤이드", kBOSS_SUPREME: False},
            {kBOSS_NAME: "대교주프레이", kBOSS_SUPREME: False},
            {kBOSS_NAME: "이미르", kBOSS_SUPREME: True}
     ]
     },
    {
        kCHAP_NO: "8챕",
        kCHAP_NAME: "바나하임",
        kCHAP_ALIAS: "바나",
        kCHAP_COLOR_CODE: '\x1b[35m',
        kCLICK_POS_S: {kX:1159, kY:345},
        kCLICK_POS: {kX: 1430, kY: 460},
        kBOSS_LIST: [  # 보스정보 목록
            {kBOSS_NAME: "엘디르", kBOSS_SUPREME: False},
            {kBOSS_NAME: "스카디", kBOSS_SUPREME: False},
            {kBOSS_NAME: "안나르엘디르", kBOSS_SUPREME: False},
            {kBOSS_NAME: "스쿨드", kBOSS_SUPREME: False},
            {kBOSS_NAME: "에기르", kBOSS_SUPREME: True}
        ]
     },
    {
        kCHAP_NO: "던전",
        kCHAP_NAME: "던전",
        kCHAP_ALIAS: "던전",
        kCHAP_COLOR_CODE: '\x1b[36m',
        kCLICK_POS_S: {kX: 1254, kY: 345},
        kCLICK_POS: {kX: 1535, kY: 460},
        kBOSS_LIST: [  # 보스정보 목록
            {kBOSS_NAME: "최하층굴베이그", kBOSS_SUPREME: False},
            {kBOSS_NAME: "최하층강글로티", kBOSS_SUPREME: False},
            {kBOSS_NAME: "최하층스네르", kBOSS_SUPREME: False},
            {kBOSS_NAME: "4층모네가름", kBOSS_SUPREME: False},
            {kBOSS_NAME: "7층드라우그", kBOSS_SUPREME: False},
            {kBOSS_NAME: "10층흘로크", kBOSS_SUPREME: False}
        ]
    }
]
