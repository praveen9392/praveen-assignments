from flask import Flask, request, Response, jsonify
import random
import xml.etree.ElementTree as ET

app = Flask(__name__)

cities = ["Vijayawada", "kolkata", "pune", "jaipur", "ahmedabad", "surat",
    "visakhapatnam", "kochi", "lucknow", "bhopal", "patna",
    "mumbai", "delhi", "bengaluru", "hyderabad", "chennai",
    "thiruvananthapuram", "nagpur", "indore", "guwahati", "vadodara"]

temperatures = [22, 27, 25, 30, 24, 26, 31, 29, 28, 23, 21, 32, 20, 33, 19, 18, 17, 34, 16, 15]
pressures = [1012, 1011, 1013, 1017, 1014, 1016, 1015, 1018, 1010, 1009, 1020, 1021, 1008, 1022, 1007, 1023, 1006, 1024, 1005, 1025]
winds = [6, 9, 8, 11, 10, 12, 7, 5, 14, 13, 15, 16, 4, 18, 3, 17, 2, 19, 1, 20]
humidities = [58, 63, 67, 52, 72, 76, 82, 88, 93, 48, 43, 38, 33, 28, 22, 18, 12, 8, 5, 85]
clouds = [18, 28, 38, 48, 58, 68, 78, 88, 8, 22, 32, 42, 52, 62, 72, 82, 92, 98, 2, 12]
visibility = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 13, 12, 14, 15, 16, 17, 18, 19, 20, 21]
air_quality = [55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155, 45, 35, 25, 15, 165, 175, 185, 195, 205]
rain_chance = [12, 22, 32, 42, 52, 62, 72, 82, 92, 99, 5, 8, 18, 28, 38, 48, 58, 68, 78, 88]

def create_fake_data():
    return {
        'city': random.choice(cities),
        'temperature': random.choice(temperatures),
        'pressure': random.choice(pressures),
        'wind_speed': random.choice(winds),
        'air_quality_index': random.choice(air_quality),
        'clouds': random.choice(clouds),
        'rain_probability': random.choice(rain_chance)
    }

weather_data = [create_fake_data() for _ in range(25)]

def get_weather(city):
    for data in weather_data:
        if data.get("city").lower() == city.lower():  
            return data

@app.route("/w/<string:city>", methods=['GET'])
def weather(city, format="json"):
    fcity = city
    fformat = format
    if request.method == 'GET':
        fcity = request.args.get('city', city)
        fformat = request.args.get('format', format)
    else:
        if request.headers.get('Content-Type') in ['application/json', 'application/xml']:
            if request.headers['Content-Type'] == 'application/json':
                fcity = request.json.get('city', city)
                fformat = request.json.get('format', format)
            elif request.headers['Content-Type'] == 'application/xml':
                root = ET.fromstring(request.data)
                el = root.findall("./name")
                fcity = el[0].text if el else city
                fformat = "xml"
        else:
            return Response("Unknown format", status=400)
    
    weather_status = get_weather(fcity.lower())
    if not weather_status:
        return Response("City not found", status=404)

    if fformat == 'json':
        return jsonify(weather_status) if city else Response("Error!!!!!!!", status=500)

    elif fformat == 'xml':
        response = f"""<?xml version="1.0" encoding="UTF-8"?>
        <data>
            <city>{weather_status['city']}</city>
            <temperature>{weather_status['temperature']}</temperature>
            <pressure>{weather_status['pressure']}</pressure>
            <wind_speed>{weather_status['wind_speed']}</wind_speed>
            <aqi>{weather_status['air_quality_index']}</aqi>
            <clouds>{weather_status['clouds']}</clouds>
            <probability_of_rain>{weather_status['rain_probability']}</probability_of_rain>
        </data>"""
        return Response(response=response, status=200, mimetype="application/xml")
    else:
        return Response("Format not recognized", status=400)

if __name__ == '__main__':
    app.run()
