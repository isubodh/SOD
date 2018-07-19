import MySQLdb
import datetime

DBNAME = 'SOD'

def CreateSOD():
	conn = MySQLdb.connect("127.0.0.1", "root", "", "sod")
	cursor = conn.cursor()
	cursor.execute('''
	CREATE TABLE IF NOT EXISTS SOD (
	SID INTEGER,
	QID INTEGER,
	STATUS TEXT,
	REM TEXT,
	AT DATE
	);''')
	cursor.close()
	conn.commit()


## sql = "INSERT INTO SOD (SID, QID, STATUS, REM, AT) VALUES ('%d', '%d', '%s', '%s', '%s' )" % (15, 20, 'BLUE', 'mySQK', '2000-07-15')
##cursor.execute("INSERT INTO SOD (SID, QID, STATUS, REM, AT)VALUES ('%s', '%s', '%s', '%s', '%s' )" % (sod['sid'], sod['qid'], sod['status'], sod['rem'],datetime.date.today()))


def update_SOD(sod):
	conn = MySQLdb.connect("127.0.0.1", "root", "", "sod")
	cursor = conn.cursor()
	cursor.execute('''
	INSERT INTO SOD (SID, QID, STATUS, REM, AT)
	VALUES ('%s', '%s', '%s', '%s', '%s' );''',(sod['sid'], sod['qid'], sod['status'], sod['rem'],datetime.date.today()))
	cursor.close()
	conn.commit()

def display_SOD():
	"""
		Returns the list of dictionary of results.
	"""
	conn = MySQLdb.connect("127.0.0.1", "root", "", "sod")
	cursor = conn.cursor()
	RS = cursor.execute('''select SID, QID, STATUS, REM, AT from SOD order by AT;''')
	results = list()
	for row in RS:
		results.append({'sid; : row[0],'qid; : row[1],'status; : row[2],'rem; : row[3],'at; : row[4]})
	cursor.close()
	conn.commit()	
	return results
	
	
'''
sod = {'sid' : 16, 'qid' : 39, 'status' : 'GREEN' , 'rem' : 'MySQL'}

cursor.execute("INSERT INTO SOD (SID, QID, STATUS, REM, AT)VALUES ('%s', '%s', '%s', '%s', '%s' )" % (sod['sid'], sod['qid'], sod['status'], sod['rem'],datetime.date.today()))

cursor.execute('''INSERT INTO SOD (SID, QID, STATUS, REM, AT)VALUES (?,?,?,?,?);''',(15, 07, 'BLUE', 'with it work',datetime.date.today()))
'''