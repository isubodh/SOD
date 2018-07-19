from flask import Flask, request
import sod_dao as dao
from sod import sod

#app = Flask(__name__)
dao.CreateSOD()

@sod.route('/api', methods=['GET','POST'])
def sod_api():
	'''
	API function to be called remotely to update the status.
	'''
	sod = dict()
	try:
		sod['sid'] = str(request.args.get('sid'))
		sod['qid'] = str(request.args.get('qid'))
		sod['status'] = str(request.args.get('status'))
		sod['rem'] = str(request.args.get('rem'))
		dao.update_SOD(sod)
	except Exception as e:
		return ("<p>API Error : %s</p>" %e)
	return '''<H1>Flask !</H1> I know now that AppID{0}, QuesID {1}, 
               has status :{2}, with comments{3}
	       '''.format(sod['sid'],sod['qid'],sod['status'],sod['rem'])

@sod.route('/', methods=['GET', 'POST'])
def show_nothing():
	'''
	This just a test function for default page.
	'''
	return '<HTML><HEAD>Welcome to SOD site</HEAD><BODY><BR>'
	
@sod.route('/sod_state', methods=['GET'])
def sod_state():
	'''
	This is to view the listing back from the database
	'''
	dao.CreateSOD()
	sodRS = dao.display_SOD()
	sodstate = '<HTML><HEAD>SOD State</HEAD><BODY><BR><HR><BR>'
	for row in sodRS:
		sodstate = sodstate + str(row[0]) +' - '+ str(row[1]) +' - '
		sodstate = sodstate + str(row[2]) +' - '+ str(row[3]) +' - '
		sodstate = sodstate + str(row[4]) +' - '+ str(len(sodstate)) 
		sodstate = sodstate + '<BR>'
	sodstate = sodstate + '<BR></BODY></HTML>'
	return  sodstate
	
if __name__ == '__main__':
    sod.run(port=10101, debug=True)
