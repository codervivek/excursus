
from channels.routing import route
from rooms.consumers import connect_room, disconnect_room, save_post


# The channel routing defines what channels get handled by what consumers,
# including optional matching on message attributes. WebSocket messages of all
# types have a 'path' attribute, so we're using that to route the socket.
# While this is under stream/ compared to the HTML page, we could have it on the
# same URL if we wanted; Daphne separates by protocol as it negotiates with a browser.
channel_routing = [
    # Called when incoming WebSockets connect
    route("websocket.connect", connect_room, path=r'^category/(?P<slug>[^/]+)/stream/$'),

    # Called when the client closes the socket
    route("websocket.disconnect", disconnect_room, path=r'^category/(?P<slug>[^/]+)/stream/$'),

    # Called when the client sends message on the WebSocket
    route("websocket.receive", save_post, path=r'^category/(?P<slug>[^/]+)/stream/$'),

    # A default "http.request" route is always inserted by Django at the end of the routing list
    # that routes all unmatched HTTP requests to the Django view system. If you want lower-level
    # HTTP handling - e.g. long-polling - you can do it here and route by path, and let the rest
    # fall through to normal views.
]
