import os
from flask import Flask, Blueprint, render_template,request,Request,session,flash,url_for,current_app
import pandas as pd
from weather_data import get_data

views=Blueprint("views",__name__)



@views.route("/", methods=["GET"])
def home():
    place = request.args.get("place")
    day = request.args.get("day")
    option2 = request.args.get('dropdown2')

    if place and day and option2:
        if option2 =="Sky":
            skycondotion=get_data(place=place,forecast_day=day,kind=option2)
            image={"Clear":"images/clear.png","Clouds":"images/cloud.png","Rain":"images/rain.png","Snow":"images/snow.png"}
            image_path=[ image[weather] for weather in skycondotion]
            return render_template('weather.html', select_day=day, select_option2=option2, select_place=place,images=image_path)
        elif option2=="Temperature":
            filter_data=get_data(place=place,forecast_day=day,kind=option2)
            temps=[round(dict["main"]["temp"],1) for dict in filter_data]
            dates=[ dict["dt_txt"] for dict in filter_data]
            return render_template('weather.html', select_day=day, select_option2=option2, select_place=place,temps=temps,dates=dates)
    else:
        return render_template('weather.html')