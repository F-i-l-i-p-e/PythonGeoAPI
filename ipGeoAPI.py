import requests

#set API key
API_KEY = 'LRUfoZ3NYRYjHJiQ4O8p0InUE5t524NL03izI7aX'

#define func
def functionLocation():
    #uses f intead of .format to put together url and API key
    url = f'https://freegeoip.app/json/?apikey={API_KEY}'
    reply = requests.get(url).json()
    
    location = {
        "country": reply.get("country_name"),
        "city": reply.get("city"),
        "ip": reply.get("ip")
    }
    return location

print(functionLocation())