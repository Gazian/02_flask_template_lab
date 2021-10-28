from flask import render_template, request
from app import app
from models.event_list import add_new_event, events,delete_event
from models.event import Event

@app.route('/events')
def index():
    return render_template('index.html', title='Home', events = events)

@app.route('/events', methods=['POST'])
def add_event():
    print(request.form)
    event_date = request.form["date"]
    event_name = request.form["name"]
    event_guests = request.form["guests"]
    event_location = request.form["location"]
    event_description = request.form["description"]
    event_recurs = request.form["recurring"]
    new_event = Event(event_date,event_name,event_guests,event_location,event_description, event_recurs)
    add_new_event(new_event)
    return render_template('index.html', title='Home', events = events)

@app.route('/events/delete/<name>')
def remove_event(name):
    delete_event(name)
    return render_template('index.html', title='Home', events = events)
