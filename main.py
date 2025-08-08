from heapq import merge

import firebase_admin  # pip install firebase-admin
from firebase_admin import credentials
from firebase_admin import firestore
from functools import cmp_to_key
import logging
import json
import datetime

from odin_common import constants as c

# import humanize

cSERVER_DICT_JSON_FILEPATH = './json/serverdict.json'
cBOSS_DICT_JSON_FILEPATH = './json/bossdict.json'

logging.basicConfig(level=logging.DEBUG)

# Use a service account.
cred = credentials.Certificate('firebase.json')
app = firebase_admin.initialize_app(cred)
db = firestore.client()


def reset_server_dic():
    '''
    firestore의 오딘 서버목록을 이 프로그램안에 하드코딩되어 있는 마스터 데이타셋을 덮어쓴다.
    :return:
    '''
    server_dic = c.cDIC_SERVER_INFO
    # logging.info(f"{server_dic}")
    db.collection(c.COL_ODIN_DATA).document(c.DOC_ODIN_SERVER).set(server_dic, merge=False)


def make_json_server_dic_from_firestore(filepath: str):
    '''
    firestore의 오딘 서버목록을 다운로드 받아서 json화일로 저장한다.
    firestore의 서버목록이 이 프로그램안에 하드코딩되어 있는 마스터 데이타셋보다 더 최신일 경우 다운받는 기능으로 활용한다.
    :param filepath: 저장할 json화일 Path
    :return:
    '''
    doc = db.collection(c.COL_ODIN_DATA).document(c.DOC_ODIN_SERVER).get()
    dicServer = doc.to_dict()
    # logging.info(dicServer)
    with open(filepath, 'w', encoding="utf-8") as outfile:
        json.dump(dicServer, outfile, indent=4, ensure_ascii=False)


def upload_json_server_dic_fo_firestore(filepath: str):
    '''
    firestore에서 다운로드 받아서 만들어 놓은 server dict json 화일을 다시 읽어서
    firestore의 서버목록을 덮어 쓴다.
    :param filepath:
    :return:
    '''
    with open(filepath, 'r', encoding="utf-8") as infile:
        server_dic = json.load(infile)
    # logging.info(dicServer)
    db.collection(c.COL_ODIN_DATA).document(c.DOC_ODIN_SERVER).set(server_dic, merge=False)

def check_duplicates_alias() -> bool:
    # 모든 'bossAlias' 리스트에 있는 문자열을 모은 리스트
    alias_list = []
    for value in c.cDIC_BOSS_INFO.values():
        alias_list.extend(value.get(c.K_BOSS_ALIAS, []))

    # 중복된 값들을 찾기 위한 코드
    seen = set()  # 이미 본 값들
    duplicates = set()  # 중복된 값들

    for alias in alias_list:
        if alias in seen:
            duplicates.add(alias)
        else:
            seen.add(alias)

    # 결과 출력
    if duplicates:
        print("중복된 'bossAlias' 값들:", duplicates)
        return True
    else:
        print("중복된 'bossAlias' 값이 없습니다.")
        return False

def reset_boss_dic():
    '''
    오딘 보스목록 마스터 데이타 리셋
    :return:
    '''
    boss_dic = c.cDIC_BOSS_INFO
    logging.info(f"{boss_dic}")
    if check_duplicates_alias():
        return
    db.collection(c.COL_ODIN_DATA).document(c.DOC_ODIN_BOSS).set(boss_dic, merge=False)


def make_json_boss_dic_from_firestore(filepath: str):
    '''
    firestore의 오딘 보스목록을 다운로드 받아서 json화일로 저장한다.
    firestore의 보스목록이 이 프로그램안에 하드코딩되어 있는 마스터 데이타셋보다 더 최신일 경우 다운받는 기능으로 활용한다.
    :param filepath: 저장할 json화일 Path
    :return:
    '''
    doc = db.collection(c.COL_ODIN_DATA).document(c.DOC_ODIN_BOSS).get()
    dicBoss = doc.to_dict()
    # logging.info(dicBoss)
    with open(filepath, 'w', encoding="utf-8") as outfile:
        json.dump(dicBoss, outfile, indent=4, ensure_ascii=False)


def upload_json_boss_dic_fo_firestore(filepath: str):
    '''
    firestore에서 다운로드 받아서 만들어 놓은 boss dict json 화일을 다시 읽어서
    firestore의 서버목록을 덮어 쓴다.
    :param filepath:
    :return:
    '''
    with open(filepath, 'r', encoding="utf-8") as infile:
        boss_dic = json.load(infile)
    # logging.info(dicServer)
    db.collection(c.COL_ODIN_DATA).document(c.DOC_ODIN_BOSS).set(boss_dic, merge=False)

def reset_chap_boss_list():
    '''
    오딘 챕터 보스 정보 마스터 데이타 리셋
    :return:
    '''
    chap_boss_list = c.cCHAPTER_BOSS_INFO
    chap_boss_info = {c.K_CHAP_BOSS_LIST:chap_boss_list}
    logging.info(f"{chap_boss_list}")
    db.collection(c.COL_ODIN_DATA).document(c.DOC_ODIN_CHAPTER_BOSS).set(chap_boss_info, merge=False)


# reset_server_dic()
# make_json_server_dic_from_firestore(cSERVER_DICT_JSON_FILEPATH)
# upload_json_server_dic_fo_firestore(cSERVER_DICT_JSON_FILEPATH)

# reset_boss_dic()
# make_json_boss_dic_from_firestore(cBOSS_DICT_JSON_FILEPATH)
# upload_json_boss_dic_fo_firestore(cBOSS_DICT_JSON_FILEPATH)

# reset_chap_boss_list()

# humanize.i18n.activate("ko_KR")
# print(humanize.naturalday(datetime.datetime.now()))
# print(humanize.naturalday(datetime.datetime.now() - datetime.timedelta(days=1)))
# print(humanize.naturalday(datetime.date(2007, 6, 5)))
# print(humanize.naturaldate(datetime.date(2007, 6, 5)))
# print(humanize.naturaltime(datetime.datetime.now() - datetime.timedelta(seconds=1)))
# print(humanize.naturaltime(datetime.datetime.now() - datetime.timedelta(seconds=3600)))
