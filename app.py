from flask import Flask, render_template, request
import requests

# Initialize the Flask application
app = Flask(__name__)


# Define the route for the homepage
@app.route('/', methods=['GET', 'POST'])
def index():
    github_info = None
    error = None

    # If the form is submitted
    if request.method == 'POST':
        username = request.form['username']  # Get the username from the form
        github_info, error = get_github_info(username)  # Fetch GitHub info

    # Render the template with the GitHub info and error message (if any)
    return render_template('index.html', github_info=github_info, error=error)


def get_github_info(username):
    """
    Fetches GitHub user information using the GitHub API.

    :param username: GitHub username
    :return: A dictionary containing the username, number of repositories, and number of followers,
             or an error message if the user is not found or an API error occurs.
    """
    url = f'https://api.github.com/users/{username}'  # GitHub API URL for user information
    response = requests.get(url)  # Make the API request

    # If the request is successful
    if response.status_code == 200:
        data = response.json()  # Parse the JSON response
        return {
            'username': username,
            'repositories': data['public_repos'],
            'followers': data['followers']
        }, None  # Return the user info with no error

    # If the user is not found
    elif response.status_code == 404:
        return None, "User not found."

    # For any other API error
    else:
        return None, "An error occurred. Please try again later."


# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5011)
