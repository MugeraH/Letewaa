import urllib.request,json
from datetime import datetime
import math

def get_weather():
    '''
    Function that gets the json response to our url request
    '''
    get_weather_url = "https://api.openweathermap.org/data/2.5/weather?q=nairobi&units=metric&appid=ef08aea75b5d267ec869c91d6f12b8fd"

    with urllib.request.urlopen(get_weather_url) as url:
        get_weather_data = url.read()
        get_weather_response = json.loads(get_weather_data)
        
        weather_data = get_weather_response.get('weather')
        
        weather_id = weather_data[0].get('id')
        weather_main = weather_data[0].get('main')
        weather_description = weather_data[0].get('description')
        
        weather_info= (weather_id,weather_main,weather_description)

    return weather_info
    
    
    
    
# get_weather()

def get_weather_information(id):
    if id == 800:
        return( 'photos/animated/day.svg','With the clear skies a cold milkshake will have you shaking the right way as you pull your dance moves')
    if id == 801:
        return ('photos/animated/cloudy.svg','Perfect day for laundry then we order a hawian pizza with fresh pinapples to get us going')
    if id == 802:
        return ('photos/animated/cloudy-day-2.svg','Its a good day to go out for a treat want some suggestions on the best places in town')
    if id == 803:
        return ( 'photos/animated/cloudy-day-3.svg','Great day for some exercise then we order a large pizza to get all the energy back')
    if id == 803:
        return ( 'photos/animated/cloudy-day-3.svg','Netflix and chill day and an easy take out to last you through the day')
    if id == 500:
        return ('photos/animated/rainy-1.svg','The kind of weather actors dance around in movies,lets carry that warm sweather just incase')
    if id == 501:
        return ('photos/animated/rainy-5.svg','A bit more rain,that sweather and an umbrella should do the trick')
    if id == 502:
        return ('photos/animated/rainy-7.svg','The rains have come its time to get our gear right,Gumboots ✔️,raincoat ✔️ and a colorful umbrella ✔️')
    if id == 503:
        return ('photos/animated/rainy-6.svg','It seems noahs times are back the rain today is insane,lets build an ark or something')
    if id == 600:
        return ('photos/animated/snowy-6.svg','Light snow lets dress warmly and go make a snow man outside')
    if id == 601:
        return ('photos/animated/snowy-6.svg','Its snowing outside lets stick indoors, and make that takeout order')
    if id == 602:
        return ('photos/animated/snowy-6.svg','Now the snow seems to be getting personal but its okay lets start up that fireplace fire')
    if id == 200:
        return ('photos/animated/thunder.svg','Thunder,Thunder,Lighnong and the thunder better keep indoors')
    if id == 201:
        return ('photos/animated/thunder.svg','Thunder,Thunder,Lighnong and the thunder better keep indoors')
    if id == 300:
        return  ('photos/animated/rainy-2.svg','Well, a bit of rain never killed anyone')
    if id == 301:
        return ('photos/animated/rainy-2.svg','Rain, but not terminal. Wear a coat i dont want you to catch a cold or something')
    if id == 302:
        return ('photos/animated/rainy-3.svg',"Rain, of the annoying variety. Don't get caught out")
    if id == 701:
        return ('photos/animated/mist.png',"The air is thick with mist and there's just barely a light rain. Tread carefully")
    if id == 711:
        return ('photos/animated/smoke.png','Smoke warning - potential forest fire hazard. Be extremely vigilant and on the lookout for the most up to date weather advisories')
    if id == 721:
        return  ('photos/animated/haze.png',"The sun's out but it's hazy.Lazy days are made of this")
    if id == 731:
        return ( 'photos/animated/dust.png',"Like walking out in the Sahara is what it looks like out there.")
    if id == 741:
        return  ('photos/animated/fog.png',"Foggy weather. Visibility severely impacted. Take extreme care when driving if you must.")
    else:
        return ('photos/animated/cloudy.svg',"Perfect day to order take out and some hot coffee")




    
def get_days(order_dateCreated):
    createdDate = datetime.fromisoformat(article_dateCreated[:-1])
    currentDate = datetime.now()
    days  = math.floor((( currentDate - createdDate ).seconds) / 86400)    
                     
    return days
def get_hours(order_dateCreated):
    createdDate = datetime.fromisoformat(article_dateCreated[:-1])
    currentDate = datetime.now()
    hours  = math.floor((( currentDate - createdDate ).seconds) / 3600)  
                     
    return hours
def get_minutes(order_dateCreated):
    createdDate = datetime.fromisoformat(article_dateCreated[:-1])
    currentDate = datetime.now()
    min = math.floor((( currentDate - createdDate ).seconds) % 3600)
    minutes  = math.floor(min / 60)
                     
    return minutes
