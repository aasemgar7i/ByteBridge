# ByteBridge: GitHub Info Fetcher

A simple Flask web application that retrieves and displays information about a GitHub user based on their username. This application uses the GitHub API to fetch the number of public repositories and followers for the given user.

## Features

- Enter a GitHub username to retrieve user information.
- Display the number of public repositories and followers.
- Basic error handling for invalid usernames and API request failures.

## Requirements

- Python 3.x
- Flask
- Requests

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/aasemgar7i/ByteBridge.git
    cd ByteBrige
    ```

2. Create and activate a virtual environment (optional but recommended):

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```bash
    pip install flask requests
    ```

## Usage

1. Run the Flask application:

    ```bash
    python3 app.py
    ```

2. Open your web browser and go to use ip given with Flask Ex: `http://127.0.0.1:5011/`.

3. Enter a GitHub username and submit the form to retrieve and display the user's information.

## Project Structure
ByteBridge/
│
├── app.py
└── templates/
└── index.html

- `app.py`: The main Flask application file.
- `templates/index.html`: The HTML template for the web page.

## Example

### Input

Enter the GitHub username in the form:

Username: octocat

### Output

GitHub Info for octocat
Repositories: 8
Followers: 3456

## Error Handling

- If the username is not found, an error message will be displayed:

User not found.

- If there is an issue with the API request, a generic error message will be shown:

An error occurred. Please try again later.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or new features.

## Acknowledgements

- [Flask](https://flask.palletsprojects.com/)
- [GitHub API](https://docs.github.com/en/rest)

=====================================================
Created By. Aasem Ali.
==========================
