import MyStreamer, words, sqlite3
from twython import Twython
from twython import TwythonStreamer
from credentials import *

sqlite_db_conn = sqlite3.connect('words_db.sqlite')

streamer = MyStreamer.MyStreamer(consumer_key,consumer_secret,my_acc_access_token,my_acc_access_secret)
streamer.db_conn = sqlite_db_conn
#Go!!

streamer.statuses.filter(follow=words.party_id_comma_list)
