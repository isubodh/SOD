
from flask import Flask, request
import sqlite3, datetime

DBNAME = 'SOD.sqlite'

app = Flask(__name__)

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

CreateSOD()

def update_SOD(sod):
	conn = sqlite3.connect(DBNAME)
	cursor = conn.cursor()
	cursor.execute('''
	INSERT OR IGNORE INTO SOD (SID, QID, STATUS, REM, AT)
	VALUES (?,?,?,?,?);''',(sod['sid'], sod['qid'], sod['status'], sod['rem'],datetime.date.today()))
	cursor.close()
	conn.commit()



@app.route('/api', methods=['GET','POST'])
def sod_api():
	sod = dict()
	try:
		sod['sid'] = str(request.args.get('sid'))
		sod['qid'] = str(request.args.get('qid'))
		sod['status'] = str(request.args.get('status'))
		sod['rem'] = str(request.args.get('rem'))
		update_SOD(sod)
	except Exception as e:
		return ("<p>API Error : %s</p>" %e)
	return '''<H1>Flask !</H1> I know now that {0},{1},{2},{3}'''.format(sod['sid'],sod['qid'],sod['status'],sod['rem'])
	
@app.route('/sod_state', methods=['GET'])
def sod_state():
	CreateSOD()
	conn = sqlite3.connect(DBNAME)
	cursor = conn.cursor()
	sodRS = cursor.execute('''select SID, QID, STATUS, REM, AT from SOD order by AT;''')

	sodstate = '<HTML><HEAD>SOD State</HEAD><BODY><BR>'
	for row in sodRS:
		sodstate = sodstate + str(row[0]) +' - '+ str(row[1]) +' - '
		sodstate = sodstate + str(row[2]) +' - '+ str(row[3]) +' - '
		sodstate = sodstate + str(row[4]) +' - '+ str(len(sodstate)) 
		sodstate = sodstate + '<BR>'
	sodstate = sodstate + '<BR></BODY></HTML>'
	return  sodstate
	
if __name__ == '__main__':
    app.run(port=10101, debug=True)