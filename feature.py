from flask import Flask
FAI=Flask(__name__)



@FAI.route('/strresponse')
def strresponse():
    return 'Hai This is the First View of Flask'

if __name__=='__main__':
    FAI.run(debug=True)
