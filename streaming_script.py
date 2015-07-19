import MyStreamer, words, sqlite3
from twython import Twython
from twython import TwythonStreamer
from credentials import *

#Init database connection
sqlite_db_conn = sqlite3.connect('words_db.sqlite')

#Setup streamer class
streamer = MyStreamer.MyStreamer(consumer_key,consumer_secret,my_acc_access_token,my_acc_access_secret)
streamer.db_conn = sqlite_db_conn

#Go!! - A list of the party twitter IDs is definted in the words.py file
streamer.statuses.filter(follow=words.party_id_comma_list)
