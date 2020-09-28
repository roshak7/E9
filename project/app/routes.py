from datetime import datetime, timedelta
from flask import Flask, request, render_template, jsonify, make_response
from random import randint
from app import app

CITY = 'Amsterdam'


class Week:
    def __init__(self, start):
        self.start = start.strftime('%d-%m-%y')
        self.end = (start + timedelta(days=7)).strftime('%d-%m-%y')
        self.week_days = self.get_weekdays(start)

    def get_weekdays(self, start):
        weekdays = []
        for i in range(8):
            weekdays.append((start + timedelta(days=i)).strftime('%d-%m-%y'))
        return weekdays


def get_weather_for_date(day):
    return randint(5, 15)


@app.route('/')
@app.route('/week')
def weather_week():
    week = Week(datetime.today())
    week_weather = {day: get_weather_for_date(day) for day in week.week_days}
    return render_template('week_overview.html', week=week, city=CITY, week_weather=week_weather)


@app.route('/your_city')
def weather_your_city():
    week = Week(datetime.today())
    return render_template('week_overview.html', week=week)


CITIES = ['amsterdam', 'moscow']


@app.route('/week/<city>')
def weather_in_city(city):
    if city in CITIES:
        week = Week(datetime.today())
        week_weather = {day: get_weather_for_date(day) for day in week.week_days}
        return render_template('week_overview.html', week=week, city=city, week_weather=week_weather)
    return render_template('404.html'), 404


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404