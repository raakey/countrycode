from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/diag')
def get_travel_advisory():
    url = "https://www.travel-advisory.info/api"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            api_status_data = {"code": 200, "status": "ok", "details": "..."}
            return jsonify({"api_status": api_status_data})
        else:
            return jsonify({"error": f"Failed to fetch data. Status code: {response.status_code}"})
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/convert')
def get_iso_alpha2_codes():
    url = "https://www.travel-advisory.info/api"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        iso_alpha2_list = [country_data['iso_alpha2'] for country_data in data['data'].values()]
        return jsonify(iso_alpha2_list)
    else:
        return jsonify({"error": f"Failed to retrieve data. Status code: {response.status_code}"}), 500

@app.route('/health', methods=['GET'])
def health_check():
    try:
        response = requests.get('https://www.travel-advisory.info/api')
        if response.status_code == 200:
            return jsonify(status='OK', message='API is healthy')
        else:
            return jsonify(status='Error', message='API is not healthy')

    except Exception as e:
        return jsonify(status='Error', message=str(e))

if __name__ == '__main__':
    app.run(debug=True)
