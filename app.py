from flask import Flask, render_template, flash, request, redirect, url_for, session, logging
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from calorie_count import calorie
app=Flask(__name__)
app.config['SECRET_KEY']=  'you-will-never-guess'



@app.route('/getcalories',methods=['POST'])
def getcalories():
    
    height=None
    weight=None
    gender=None
    Disease=None
    location=None
    activity_level=None
    age=None
    request_data = request.get_json()
    if request_data:
        if 'age' in request_data:
            age=request_data['age']
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
    calorie_count=calorie(age,gender,weight,height,activity_level)
    bmr=calorie_count.user_info()
    bmr_with_activity=calorie_count.calculate_activity(bmr)
    return '''
           The height value is: {}
           The weight value is: {}
           The location value is: {}
           The Gender is:{}
           The Disease are:{}
           The BMR is: {}
           The BMR with acitvity is:{}
           '''.format(height, weight,location,gender,Disease, bmr,bmr_with_activity)
if __name__ == "__main__":
    app.run()