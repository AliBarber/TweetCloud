from twython import Twython
from twython import TwythonStreamer
import string
import words
import sqlite3
class MyStreamer(TwythonStreamer):

	#Take the tweet - get the words out of it and figure out who it's from, then call wordRead with it to check it and 
	# add it to the database 
	def on_success(self,data):
		if 'text' in data:
			#Bit of a hack for dealing with special characters
			tweet_user_id = data['user']['id_str'].encode('utf-8')
			if tweet_user_id in words.party_id_lookup.keys():
				tweet_text = data['text'].encode('utf-8','ignore')
				tweet_id = data['id_str'].encode('utf-8','ignore')
				print tweet_user_id+"--"+ tweet_text
				print "Tweet from: "+words.party_id_lookup[tweet_user_id]+" "+tweet_text
				for tweet_word in tweet_text.split(' '):
					if (not tweet_word.startswith('https://')) and (not tweet_word.startswith('http://')) and (tweet_word.find('@') == -1) and (tweet_word.find('#') == -1) and (tweet_word.find('\xc2\xa3') == -1):
						tweet_word = tweet_word.translate(string.maketrans("",""), string.punctuation)
					words.wordRead(self.db_conn, tweet_word, tweet_user_id, tweet_id, tweet_text)
					# print str(data['user']['id'])+' -- '+data['text'].encode('utf-8')
				self.db_conn.commit()
	def on_error(self,status_code,data):
		print status_code
		self.disconnect()
