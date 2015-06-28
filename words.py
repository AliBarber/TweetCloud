#! /usr/bin/python
import sqlite3

party_id_lookup = {'21856384' : 'me', '14281853' : 'con', '14291684': 'lab', '5680622' : 'lbd', '15529670' : 'grn', '77821953' : 'snp', '358204197' : 'ukp'}
party_id_comma_list = '21856384,14281853,14291684,5680622,15529670,77821953,358204197'

def wordRead(connection, word, party_id,tweet_id=0,last_tweet_text=""):
	connection.text_factory = str
	c = connection.cursor();
	#word = word.decode('utf-8')
	word = word.lower()
	# command_str = 
	c.execute("update words set count = count+1, "+party_id_lookup[party_id]+" = "+party_id_lookup[party_id]+"+1,last_tweet='"+tweet_id+"',last_tweet_from='"+party_id_lookup[party_id]+"',last_tweet_text=? where word= ?;",(last_tweet_text, word))
	# (rows_affected,) = c.fetchone()
	if c.rowcount is 0:
		print "Adding word: "+word
		c.execute("insert into words (word,count,"+party_id_lookup[party_id]+",last_tweet,last_tweet_from,last_tweet_text) values (?,?,?,?,?,?);",(word,1,1,tweet_id,party_id_lookup[party_id],last_tweet_text))

