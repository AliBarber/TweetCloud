#! /usr/bin/python
import sqlite3
import json

conn = sqlite3.connect('/home/alastair/electionwords_test/words_db.sqlite')
cursor = conn.cursor()

# qry = 'select * from words where count > 5 order by count desc limit 150';
qry = 'select t1.word,t1.count,t1.con,t1.lab,t1.lbd,t1.ukp,t1.grn,t1.snp,t1.last_tweet,t1.last_tweet_from,t1.last_tweet_text from words t1 left join boringwords t2 on t2.word = t1.word where t2.word is null and t1.count > 5 order by count desc limit 200';

cursor.execute(qry);
rows = [x for x in cursor]
cols = [x[0] for x in cursor.description]
words = []
for row in rows:
	word_row = {}
	for prop, val in zip(cols,row):
		word_row[prop] = val
	words.append(word_row)

wordsJSON = json.dumps(words)
print wordsJSON

with open('www/data.json','wb') as datafile:
	datafile.write(wordsJSON)