from flask import Flask, render_template, flash, request, redirect, url_for, session, logging
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
app=Flask(__name__)
app.config['SECRET_KEY']=  'you-will-never-guess'



@app.route('/getcalories',methods=['POST'])
def getcalories():
    
    height=None
    weight=None
    gender=None
    Disease=None
    location=None
    
    request_data = request.get_json()
    if request_data:
        if 'height' in request_data:
            height  = request_data['height']
        if 'weight' in request_data:
            weight  = request_data['weight']
        if 'Gender' in request_data:
            gender=request_data['Gender']
        if 'Disease' in request_data:
            Disease=request_data['Disease']
        if 'Location' in request_data:
            location = request_data['Location']
    return '''
           The height value is: {}
           The weight value is: {}
           The location value is: {}
           The Gender is:{}
           The Disease are:{}
           '''.format(height, weight,location,gender,Disease)
if __name__ == "__main__":
    app.run()