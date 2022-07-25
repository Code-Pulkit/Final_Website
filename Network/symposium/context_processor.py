from numpy import append
from constance import config
from .models import Event, NavLink


def extras(request):
    event = {'name': '', 'hero_image': ''}
    list1 = []
    try:
        Event_got = Event.objects.get(id=config.CURRENT_EVENT)
        event['name'] = Event_got.name
        event['hero_image'] = Event_got.image
        navbar = NavLink.objects.filter(event=Event_got)
        print(Event_got)
        for item in navbar:
            list1.append({'name': item.name, 'link': item.link})

    except Event.DoesNotExist:
        event['name'] = "e-Yantra"
        event['hero_image'] = "uploads/hero_1.png"

    pages = {"general": list1,
             "authentication": [{
                 'name': 'Register',
                 'link': '/register'
             }, {
                 'name': 'Login',
                 'link': '/login'
             }]
             }
    return {'pages': pages, 'event': event}
