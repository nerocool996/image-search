from flask import Flask, render_template, request, redirect, url_for,flash, jsonify,make_response
from datetime import date,timedelta
from database_setup import Base,Queries
app = Flask(__name__)

from sqlalchemy import create_engine,desc,func
from sqlalchemy.orm import sessionmaker
from urlparse import urlparse
from random import random

import httplib, urllib, base64,json,datetime

headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': 'Your API Key',
}

engine = create_engine('postgres://jmmodrydkyhole:HOD93bvzChb_zpa30S1ScrHvsE@ec2-54-221-235-135.compute-1.amazonaws.com:5432/d323kk8ffr81ad')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
def mainpage():
	return render_template('main.html')


@app.route('/latest')
def latest():
	allElement = session.query(Queries).order_by(Queries.time).all()
	return jsonify(latest=[i.serialize for i in allElement])
        
@app.route('/imagesearch/<string:url>')
def TimeStamp(url):
	try:
		searchcount = request.args.get('offset', '10')
		print (url, searchcount)
		params = urllib.urlencode({
    			# Request parameters
  	  		'q': 	url,
  	  		'count': searchcount,
  	  		'offset': '0',
  	  		'mkt': 'en-us',
  	  		'safeSearch': 'Moderate',
		})
		print params
		conn = httplib.HTTPSConnection('api.cognitive.microsoft.com')
	 	conn.request("GET", "/bing/v5.0/images/search?%s" % params, "{body}", headers)
		responses = conn.getresponse()
	  	##Converts a string to Dictionary object 
	  	data =  json.loads(responses.read())
	 	conn.close()
	 	new = Queries(query=url,time = datetime.datetime.now())
	 	session.add(new)
	 	session.commit()
	  	res = {"result":data["value"]}
  	  	
	   	return jsonify(res)
	except:
		return jsonify({"value":"Error"})
	
##if __name__ == '__main__':
app.secret_key = 'uberBlack'
app.debug = True
##	app.run(host = '0.0.0.0', port = 5000)
