from bottle import request, response
from bottle import post, get, put, delete
import bottle

result= {'accuracy':1}

@get('/')
def creation_handler(): 
    '''Handles name creation'''
    return 'hola'

@get('/hello/<name>')
def names(name):
	return 'hello %s' % name

@get('/acc/')
def acc():
	return result

bottle.run(host = '127.0.0.1', port = 8000)
