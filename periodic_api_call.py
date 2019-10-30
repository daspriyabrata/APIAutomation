from threading import Timer
from api_call_manager import API_Call_Manager

_host_name = "https://hacker-news.firebaseio.com/v0/"
t = Timer(300.0, API_Call_Manager.top_stories_api(_host_name))
try:
    print(t.start())
except KeyboardInterrupt:
    print("Process ended")