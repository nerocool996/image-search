from flask import Flask, render_template, request, redirect, url_for,flash, jsonify,make_response
from datetime import date,timedelta
from database_setup import Base,Links
app = Flask(__name__)

from sqlalchemy import create_engine,desc,func
from sqlalchemy.orm import sessionmaker
from urlparse import urlparse
from random import random

engine = create_engine('postgres://eftouahahwepdz:L1bqXJw6TrrHoASeNh8XmjpgRB@ec2-54-243-212-72.compute-1.amazonaws.com:5432/d56424prqdm2cu')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
def mainpage():
	return render_template('main.html')



        
@app.route('/new/<path:url>')
def TimeStamp(url):
	Purl = 	urlparse(url)	
	if (Purl.netloc):
		st,en = 97,122
		sURL = ""
		
		for i in range(0,4):
			ch= 26*random()+97
			sURL += chr(int(ch))
		newURL = Links(url=url,short_URL=sURL)
		session.add(newURL)
		session.commit()
		return sURL
	else:
		return jsonify({"URL":url,"Short URL":"Not a valid url"})
	
@app.route('/<string:url>')
def redir(url):
	if (len(url)==4):
		try:
			res = session.query(Links).filter_by(short_URL =url).one()
			return redirect(res.url)
		except:
			return jsonify({"short_URL":"Does not exist in data base"})
	else:
		return jsonify({"short_URL":"Does not exist in data base"})

##if __name__ == '__main__':
app.secret_key = 'uberBlack'
app.debug = True
##	app.run(host = '0.0.0.0', port = 5000)
