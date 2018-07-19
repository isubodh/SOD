import sqlite3
import datetime

DBNAME = 'SOD.sqlite'

def CreateSOD():
	global DBNAME
	conn = sqlite3.connect(DBNAME)
	cursor = conn.cursor()
	cursor.execute('''
	CREATE TABLE IF NOT EXISTS SOD (
	SID INTEGER,
	QID INTEGER,
	STATUS TEXT,
	REM TEXT,
	AT TEXT
	);''')
	cursor.close()
	conn.commit()

def update_SOD(sod):
	conn = sqlite3.connect(DBNAME)
	cursor = conn.cursor()
	cursor.execute('''
	INSERT OR IGNORE INTO SOD (SID, QID, STATUS, REM, AT)
	VALUES (?,?,?,?,?);''',(sod['sid'], sod['qid'], sod['status'], sod['rem'],datetime.date.today()))
	cursor.close()
	conn.commit()

def display_SOD():
	conn = sqlite3.connect(DBNAME)
	cursor = conn.cursor()
	RS = cursor.execute('''select SID, QID, STATUS, REM, AT from SOD order by AT;''')
	return RS