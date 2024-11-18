from flask import Flask, request, redirect
from auth import get_facebook_auth_url, get_token

# Initialize Flask application
app = Flask(__name__)

# Define the home route, which redirects the user to Facebook's OAuth login
@app.route('/')
def index():
    auth_url, _ = get_facebook_auth_url()
    return redirect(auth_url)  # Redirect to Facebook OAuth URL

# Define the callback route where Facebook redirects after authorization
@app.route('/callback')
def callback():
    code = request.args.get('code')
    token = get_token(code)
    access_token = token['access_token']
    
    # Overwrite the access token in the file
    with open('access_token.txt', 'w') as file:
        file.write(access_token)
    
    # Redirect to a confirmation page
    return redirect('/success')

# Confirmation page after saving the access token
@app.route('/success')
def success():
    return """
    <html>
        <body>
            <h1>Access Token Saved!</h1>
            <p>Your access token has been saved successfully.</p>
            <p>You can now return to the CLI and continue using the app.</p>
        </body>
    </html>
    """

if __name__ == '__main__':
    # Run the Flask app on host "0.0.0.0" to accept connections on all IPs and port 5001
    app.run(host="0.0.0.0", port=5001, debug=True)
