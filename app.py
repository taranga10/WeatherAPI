from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/weather', methods=['GET'])
def get_weather():
    """
    Fetches weather data from OpenWeatherMap for a specific city
    and returns the data in JSON format.
    """
    api_key = 'bd5e378503939ddaee76f12ad7a97608'  # Replace with your actual OpenWeatherMap API key
    city = 'Bengaluru'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(url)
    data = response.json()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
