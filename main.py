from flask import Flask, jsonify, render_template
import requests


def data_from_api():
    if response.status_code == 200:
        data = response.json
        return data
    else:
        return jsonify({"error": "Failed to fetch data from API"}), 500


api_url = 'https://api.npoint.io/4e69431118e2881acf61'
response = requests.get(api_url)
all_posts = data_from_api()
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', posts=all_posts)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)
