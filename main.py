import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from functools import cmp_to_key
import const_data as cd
import logging
import datetime
import humanize


# Use a service account.
cred = credentials.Certificate('firebase.json')
app = firebase_admin.initialize_app(cred)
db = firestore.client()

"""
 오딘 서버목록 마스터 데이타 리셋
"""
def reset_server_list():
    server_list = list(cd.cSERVER_SET)
    logging.info(f"{server_list}")
    db.collection(cd.kCOL_ODINDATA).document(cd.kDOC_ODINDATA).set({
        cd.kFLD_SERVER_LIST: server_list
        }, merge=True)


"""
 오딘 보스목록 마스터 데이타 리셋
"""
def reset_boss_dic():
    boss_dic = cd.cDIC_BOSS_INFO
    logging.info(f"{boss_dic}")
    db.collection(cd.kCOL_ODINDATA).document(cd.kDOC_ODINDATA).set({
        cd.kFLD_BOSS_DIC: boss_dic
        }, merge=True)

logging.basicConfig(level=logging.DEBUG)
#reset_server_list()
#reset_boss_dic()

# humanize.i18n.activate("ko_KR")
# print(humanize.naturalday(datetime.datetime.now()))
# print(humanize.naturalday(datetime.datetime.now() - datetime.timedelta(days=1)))
# print(humanize.naturalday(datetime.date(2007, 6, 5)))
# print(humanize.naturaldate(datetime.date(2007, 6, 5)))
# print(humanize.naturaltime(datetime.datetime.now() - datetime.timedelta(seconds=1)))
# print(humanize.naturaltime(datetime.datetime.now() - datetime.timedelta(seconds=3600)))