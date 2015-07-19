#! /usr/bin/python
import sqlite3

#Lookup for mapping party names to twitter ID's - makes the database table a bit nicer to read (i.e. column names are party abbreviations as opposed to twitter ids.)
# I'm on it for testing purposes ;) 
party_id_lookup = {'21856384' : 'me', '14281853' : 'con', '14291684': 'lab', '5680622' : 'lbd', '15529670' : 'grn', '77821953' : 'snp', '358204197' : 'ukp'}

#Probabnly a poor way to do this - there must be a nice pythonic way just to pull the keys from the last dict. Sorry.
party_id_comma_list = '21856384,14281853,14291684,5680622,15529670,77821953,358204197'

#Performed for every word from a tweet
def wordRead(connection, word, party_id,tweet_id=0,last_tweet_text=""):
	connection.text_factory = str
	c = connection.cursor();
	# Had some issues with encoding and special characters. 
	#word = word.decode('utf-8')
	word = word.lower()
	# command_str = 
	c.execute("update words set count = count+1, "+party_id_lookup[party_id]+" = "+party_id_lookup[party_id]+"+1,last_tweet='"+tweet_id+"',last_tweet_from='"+party_id_lookup[party_id]+"',last_tweet_text=? where word= ?;",(last_tweet_text, word))
	# (rows_affected,) = c.fetchone()
	if c.rowcount is 0:
		print "Adding word: "+word
		c.execute("insert into words (word,count,"+party_id_lookup[party_id]+",last_tweet,last_tweet_from,last_tweet_text) values (?,?,?,?,?,?);",(word,1,1,tweet_id,party_id_lookup[party_id],last_tweet_text))

