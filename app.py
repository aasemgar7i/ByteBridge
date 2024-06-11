from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    github_info = None
    error = None
    if request.method == 'POST':
        username = request.form['username']
        github_info, error = get_github_info(username)
    return render_template('index.html', github_info=github_info, error=error)


def get_github_info(username):
    url = f'https://api.github.com/users/{username}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            'username': username,
            'repositories': data['public_repos'],
            'followers': data['followers']
        }, None
    elif response.status_code == 404:
        return None, "User not found."
    else:
        return None, "An error occurred. Please try again later."


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5011)
