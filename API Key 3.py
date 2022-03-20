# Api key AIzaSyBERGmPpGvlPq24uFaXV7sAS6-pIMl7o30
import urllib.request
import json
import webbrowser
import googlemaps
api_key = 'AIzaSyC7gEiJi2eQKs64JWnRCl0c64cBMLfrw2g(old)' 
request = input("What's Your Location?: ")
request = request.replace(' ','+')
gmaps = googlemaps.Client(key='AIzaSyC7gEiJi2eQKs64JWnRCl0c64cBMLfrw2g(old)')
geocode_result = gmaps.geocode(request)
strgeocode_result = str(geocode_result)
sensor = False
print(geocode_result)
for result in geocode_result:
    try:
        lat = result['geometry']['location']['lat']
        lng = result['geometry']['location']['lng']
        address = result['formatted_address']
    except KeyError:
        lat = None
        lng = None
        address = None
endpoint = 'https://maps.googleapis.com/maps/api/geocode/json?address='+request+'&sensor=False''&key='+api_key+''
response = urllib.request.urlopen(endpoint).read()
tests = json.loads(response)
resp_json_payload = tests
#latlng = (lat,lng)
strlat = str(lat)
strlng = str(lng)
url = ("https://www.google.com/maps/search/?api=1&query="+address)
strurl = str(url)
webbrowser.open(strurl)

text_file = open("Address_Output.txt", "w")
text_file.write(address)
text_file.close()
    
