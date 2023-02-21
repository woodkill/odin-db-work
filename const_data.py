"""
 collection key
"""
kCOL_ODINDATA = "OdinData"
kCOL_ODINGUILD = u'OdinGuild'

"""
 document key
"""
kDOC_ODINDATA = u'OdinData'

"""
 field name
"""
kFLD_SERVER_LIST = u'serverList'
kFLD_BOSS_DIC = u'bossDictionary'

"""
 dictionary key
"""
kCHAP_NO = u'chapNumber'
kBOSS_LEVEL = u'bossLevel'
kBOSS_ORDER = u'bossOrder'
kBOSS_NAME = u'bossName'
kBOSS_ALIAS = u'bossAlias'
kBOSS_INTERVAL = u'interval'

cSERVER_SET = {
    u'오딘01',
    u'오딘02',
    u'오딘03',
    u'오딘04',
    u'오딘05',
    u'오딘06',
    u'오딘07',
    u'오딘08',
    u'오딘09',
    u'토르01',
    u'토르02',
    u'토르03',
    u'토르04',
    u'토르05',
    u'토르06',
    u'토르07',
    u'토르08',
    u'토르09',
    u'로키01',
    u'로키02',
    u'로키03',
    u'로키04',
    u'로키05',
    u'로키06',
    u'로키07',
    u'로키08',
    u'로키09',
    u'프레이야01',
    u'프레이야02',
    u'프레이야03',
    u'프레이야04',
    u'프레이야05',
    u'프레이야06',
    u'프레이야07',
    u'프레이야08',
    u'프레이야09',
    u'해임달01',
    u'해임달02',
    u'해임달03',
    u'해임달04',
    u'해임달05',
    u'해임달06',
    u'해임달07',
    u'해임달08',
    u'해임달09',
    u'티르01',
    u'티르02',
    u'티르03',
    u'티르04',
    u'티르05',
    u'티르06',
    u'티르07',
    u'티르08',
    u'티르09',
    u'발두르01',
    u'발두르02',
    u'발두르03',
    u'발두르04',
    u'발두르05',
    u'발두르06',
    u'발두르07',
    u'발두르08',
    u'발두르09',
    u'이둔01',
    u'이둔02',
    u'이둔03',
    u'이둔04',
    u'이둔05',
    u'이둔06',
    u'이둔07',
    u'이둔08',
    u'이둔09',
    u'미미르01',
    u'미미르02',
    u'미미르03',
    u'미미르04',
    u'미미르05',
    u'미미르06',
    u'미미르07',
    u'미미르08',
    u'미미르09'
}

cDIC_BOSS_INFO = {
    # 던전
    '000':{kCHAP_NO:0, kBOSS_LEVEL:0, kBOSS_ORDER:0, kBOSS_INTERVAL:'01:12:00', kBOSS_NAME:u'혼돈의마수굴베이그' , kBOSS_ALIAS:[u'최하층굴베', u'최하층5']   },
    '001':{kCHAP_NO:0, kBOSS_LEVEL:0, kBOSS_ORDER:1, kBOSS_INTERVAL:'01:12:00', kBOSS_NAME:u'혼돈의사제강글로티' , kBOSS_ALIAS:[u'강글', u'최하층막']        },
    '002':{kCHAP_NO:0, kBOSS_LEVEL:0, kBOSS_ORDER:2, kBOSS_INTERVAL:'00:12:00', kBOSS_NAME:u'분노의모네가름'     , kBOSS_ALIAS:[u'4층']                      },
    '003':{kCHAP_NO:0, kBOSS_LEVEL:0, kBOSS_ORDER:3, kBOSS_INTERVAL:'00:24:00', kBOSS_NAME:u'나태의드라우그'     , kBOSS_ALIAS:[u'7층']                      },
    # 미스가르드
    '100':{kCHAP_NO:1, kBOSS_LEVEL:0, kBOSS_ORDER:0, kBOSS_INTERVAL:'00:00:10', kBOSS_NAME:u'그로아'             , kBOSS_ALIAS:[u'그로아']                   },
    '101':{kCHAP_NO:1, kBOSS_LEVEL:0, kBOSS_ORDER:1, kBOSS_INTERVAL:'00:00:10', kBOSS_NAME:u'칼바람하피'         , kBOSS_ALIAS:[u'하피']                     },
    '102':{kCHAP_NO:1, kBOSS_LEVEL:0, kBOSS_ORDER:2, kBOSS_INTERVAL:'00:00:10', kBOSS_NAME:u'매트리악'           , kBOSS_ALIAS:[u'매트리악']                 },
    '103':{kCHAP_NO:1, kBOSS_LEVEL:0, kBOSS_ORDER:3, kBOSS_INTERVAL:'00:00:10', kBOSS_NAME:u'레라드'             , kBOSS_ALIAS:[u'레라드']                   },
    '104':{kCHAP_NO:1, kBOSS_LEVEL:0, kBOSS_ORDER:4, kBOSS_INTERVAL:'00:00:10', kBOSS_NAME:u'탕그뇨스트'         , kBOSS_ALIAS:[u'탕그뇨스트']               },
    # 요툰하임
    '200':{kCHAP_NO:2, kBOSS_LEVEL:0, kBOSS_ORDER:0, kBOSS_INTERVAL:'00:12:00', kBOSS_NAME:u'파르바'             , kBOSS_ALIAS:[u'파르바']                   },
    '201':{kCHAP_NO:2, kBOSS_LEVEL:0, kBOSS_ORDER:1, kBOSS_INTERVAL:'00:12:00', kBOSS_NAME:u'셀로비아'           , kBOSS_ALIAS:[u'셀로']                     },
    '202':{kCHAP_NO:2, kBOSS_LEVEL:0, kBOSS_ORDER:2, kBOSS_INTERVAL:'00:12:00', kBOSS_NAME:u'흐니르'             , kBOSS_ALIAS:[u'흐니르']                   },
    '203':{kCHAP_NO:2, kBOSS_LEVEL:0, kBOSS_ORDER:3, kBOSS_INTERVAL:'00:12:00', kBOSS_NAME:u'페티'               , kBOSS_ALIAS:[u'페티']                     },
    '204':{kCHAP_NO:2, kBOSS_LEVEL:0, kBOSS_ORDER:4, kBOSS_INTERVAL:'00:12:00', kBOSS_NAME:u'바우티'             , kBOSS_ALIAS:[u'바우티']                   },
    '205':{kCHAP_NO:2, kBOSS_LEVEL:0, kBOSS_ORDER:5, kBOSS_INTERVAL:'00:12:00', kBOSS_NAME:u'니드호그'           , kBOSS_ALIAS:[u'니드']                     },
    '206':{kCHAP_NO:2, kBOSS_LEVEL:0, kBOSS_ORDER:6, kBOSS_INTERVAL:'00:12:00', kBOSS_NAME:u'야른'               , kBOSS_ALIAS:[u'야른']                     },
    '207':{kCHAP_NO:2, kBOSS_LEVEL:1, kBOSS_ORDER:0, kBOSS_INTERVAL:'03:00:00', kBOSS_NAME:u'티르'               , kBOSS_ALIAS:[u'티르']                     },
    '208':{kCHAP_NO:2, kBOSS_LEVEL:2, kBOSS_ORDER:0, kBOSS_INTERVAL:'00:00:00', kBOSS_NAME:u'갸름'               , kBOSS_ALIAS:[u'갸름', u'가름']            },
    # 니다벨리르
    '300':{kCHAP_NO:3, kBOSS_LEVEL:0, kBOSS_ORDER:0, kBOSS_INTERVAL:'00:12:00', kBOSS_NAME:u'라이노르'           , kBOSS_ALIAS:[u'라이']                     },
    '301':{kCHAP_NO:3, kBOSS_LEVEL:0, kBOSS_ORDER:1, kBOSS_INTERVAL:'00:12:00', kBOSS_NAME:u'비요른'             , kBOSS_ALIAS:[u'비요른']                   },
    '302':{kCHAP_NO:3, kBOSS_LEVEL:0, kBOSS_ORDER:2, kBOSS_INTERVAL:'00:12:00', kBOSS_NAME:u'헤르모드'           , kBOSS_ALIAS:[u'헤르모드']                 },
    '303':{kCHAP_NO:3, kBOSS_LEVEL:0, kBOSS_ORDER:3, kBOSS_INTERVAL:'00:12:00', kBOSS_NAME:u'스칼라니르'         , kBOSS_ALIAS:[u'스칼']                     },
    '304':{kCHAP_NO:3, kBOSS_LEVEL:0, kBOSS_ORDER:4, kBOSS_INTERVAL:'00:12:00', kBOSS_NAME:u'브륀힐드'           , kBOSS_ALIAS:[u'브륀', u'브린']            },
    '305':{kCHAP_NO:3, kBOSS_LEVEL:0, kBOSS_ORDER:5, kBOSS_INTERVAL:'00:12:00', kBOSS_NAME:u'라타토스크'         , kBOSS_ALIAS:[u'라타']                     },
    '306':{kCHAP_NO:3, kBOSS_LEVEL:0, kBOSS_ORDER:6, kBOSS_INTERVAL:'00:12:00', kBOSS_NAME:u'수드리'             , kBOSS_ALIAS:[u'수드리']                   },
    '307':{kCHAP_NO:3, kBOSS_LEVEL:1, kBOSS_ORDER:0, kBOSS_INTERVAL:'03:00:00', kBOSS_NAME:u'토르'               , kBOSS_ALIAS:[u'토르']                     },
    '308':{kCHAP_NO:3, kBOSS_LEVEL:2, kBOSS_ORDER:0, kBOSS_INTERVAL:'00:00:00', kBOSS_NAME:u'발두르'             , kBOSS_ALIAS:[u'발두르']                   },
    # 알브하임
    '401':{kCHAP_NO:4, kBOSS_LEVEL:0, kBOSS_ORDER:1, kBOSS_INTERVAL:'00:24:00', kBOSS_NAME:u'두라스로르'         , kBOSS_ALIAS:[u'두라']                     },
    '402':{kCHAP_NO:4, kBOSS_LEVEL:0, kBOSS_ORDER:2, kBOSS_INTERVAL:'00:24:00', kBOSS_NAME:u'모네가름'           , kBOSS_ALIAS:[u'모네']                     },
    '403':{kCHAP_NO:4, kBOSS_LEVEL:0, kBOSS_ORDER:3, kBOSS_INTERVAL:'00:24:00', kBOSS_NAME:u'드라우그'           , kBOSS_ALIAS:[u'드라']                     },
    '404':{kCHAP_NO:4, kBOSS_LEVEL:0, kBOSS_ORDER:4, kBOSS_INTERVAL:'00:24:00', kBOSS_NAME:u'굴베이그'           , kBOSS_ALIAS:[u'굴베', u'굴배']            },
    '400':{kCHAP_NO:4, kBOSS_LEVEL:0, kBOSS_ORDER:0, kBOSS_INTERVAL:'00:24:00', kBOSS_NAME:u'스바르트'           , kBOSS_ALIAS:[u'스바']                     },
    '405':{kCHAP_NO:4, kBOSS_LEVEL:1, kBOSS_ORDER:0, kBOSS_INTERVAL:'03:00:00', kBOSS_NAME:u'오딘'               , kBOSS_ALIAS:[u'오딘']                     },
    '406':{kCHAP_NO:4, kBOSS_LEVEL:2, kBOSS_ORDER:0, kBOSS_INTERVAL:'00:00:00', kBOSS_NAME:u'파프니르'           , kBOSS_ALIAS:[u'파르']                     },
    # 무스펠하임
    '500':{kCHAP_NO:5, kBOSS_LEVEL:0, kBOSS_ORDER:0, kBOSS_INTERVAL:'00:36;00', kBOSS_NAME:u'메기르'             , kBOSS_ALIAS:[u'메기르']                   },
    '501':{kCHAP_NO:5, kBOSS_LEVEL:0, kBOSS_ORDER:1, kBOSS_INTERVAL:'00:36;00', kBOSS_NAME:u'신마라'             , kBOSS_ALIAS:[u'신마라']                   },
    '502':{kCHAP_NO:5, kBOSS_LEVEL:0, kBOSS_ORDER:2, kBOSS_INTERVAL:'00:36;00', kBOSS_NAME:u'헤르가름'           , kBOSS_ALIAS:[u'헤르']                     },
    '503':{kCHAP_NO:5, kBOSS_LEVEL:0, kBOSS_ORDER:3, kBOSS_INTERVAL:'00:36;00', kBOSS_NAME:u'탕그리스니르'       , kBOSS_ALIAS:[u'탕그']                     },
    '504':{kCHAP_NO:5, kBOSS_LEVEL:0, kBOSS_ORDER:4, kBOSS_INTERVAL:'00:36;00', kBOSS_NAME:u'엘드룬'             , kBOSS_ALIAS:[u'엘드']                     },
    '505':{kCHAP_NO:5, kBOSS_LEVEL:0, kBOSS_ORDER:5, kBOSS_INTERVAL:'00:36;00', kBOSS_NAME:u'우로보로스'         , kBOSS_ALIAS:[u'우로']                     },
    '506':{kCHAP_NO:5, kBOSS_LEVEL:1, kBOSS_ORDER:0, kBOSS_INTERVAL:'03:00;00', kBOSS_NAME:u'수르트'             , kBOSS_ALIAS:[u'수르트']                   },
    '507':{kCHAP_NO:5, kBOSS_LEVEL:2, kBOSS_ORDER:0, kBOSS_INTERVAL:'00:00;00', kBOSS_NAME:u'아우둠라'           , kBOSS_ALIAS:[u'둠라']                     },
    # 아스가르드
    '600':{kCHAP_NO:6, kBOSS_LEVEL:0, kBOSS_ORDER:0, kBOSS_INTERVAL:'00:36:00', kBOSS_NAME:u'발리'               , kBOSS_ALIAS:[u'발리']                     },
    '601':{kCHAP_NO:6, kBOSS_LEVEL:0, kBOSS_ORDER:1, kBOSS_INTERVAL:'00:36:00', kBOSS_NAME:u'노트'               , kBOSS_ALIAS:[u'노트']                     },
    '602':{kCHAP_NO:6, kBOSS_LEVEL:0, kBOSS_ORDER:2, kBOSS_INTERVAL:'00:36:00', kBOSS_NAME:u'샤무크'             , kBOSS_ALIAS:[u'샤무크']                   },
    '603':{kCHAP_NO:6, kBOSS_LEVEL:0, kBOSS_ORDER:3, kBOSS_INTERVAL:'00:36:00', kBOSS_NAME:u'스칼드메르'         , kBOSS_ALIAS:[u'스칼드메르']               },
    '604':{kCHAP_NO:6, kBOSS_LEVEL:0, kBOSS_ORDER:4, kBOSS_INTERVAL:'00:36:00', kBOSS_NAME:u'화신그로아'         , kBOSS_ALIAS:[u'화신']                     },
    '605':{kCHAP_NO:6, kBOSS_LEVEL:1, kBOSS_ORDER:0, kBOSS_INTERVAL:'03:00:00', kBOSS_NAME:u'미미르'             , kBOSS_ALIAS:[u'미미르']                   },
    '606':{kCHAP_NO:6, kBOSS_LEVEL:2, kBOSS_ORDER:0, kBOSS_INTERVAL:'00:00:00', kBOSS_NAME:u'헤임달'             , kBOSS_ALIAS:[u'해임달']                   }
}
