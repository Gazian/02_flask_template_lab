from models.event import *

event_1 = Event("2021-10-31", "Halloween Party", 25, "Grand Hall", "Scary, spooky night of fun",True)
event_2 = Event("2021-12-23", "Christmas Feast", 100, "Rooftop Terrace", "Festive treats and fun for all",False)

events =[event_1,event_2]

def add_new_event(event):
    events.append(event)

def delete_event(input_event):
    for event in events:
        if event.name == input_event: 
            events.remove(event)


