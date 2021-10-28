from models.event import *

event_1 = Event("31/10/2021", "Halloween Party", 25, "Grand Hall", "Scary, spooky night of fun",True)
event_2 = Event("20/12/2021", "Christmas Feast", 100, "Rooftop Terrace", "Festive treats and fun for all",False)

events =[event_1,event_2]

def add_new_event(event):
    events.append(event)

