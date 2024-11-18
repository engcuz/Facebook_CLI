# Facebook CLI

## Description
The Facebook CLI project is a command-line application that interacts with the Facebook Graph API. It allow users to perform various Facebook actions, such as posting a status update, viewing profile details, and managing friends, directly from the terminal.

## Features
- Post status updates.
- View profile details.
- Retrieve and display recent posts.
- Like and comment on posts.
- Delete posts.
- View notifications.
- List friends.
- Send friend requests.
- Unfriend users.
- Send direct messages.

## Prerequisites
- Python 3.8 or later installed.
- Facebook Developer App created with the following permissions:
  - `email`
  - `public_profile`
  - `user_posts`
  - `user_friends`
- **ngrok** installed for local HTTPS URL redirection.

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/engcuz/Facebook_CLI.git
   cd Facebook_CLI
2. Create a Virtual Environment.
  For macOS/Linux:
    python3 -m venv venv
    source venv/bin/activate
  For Windows:
    python -m venv venv
    venv\Scripts\activate
3.Install Dependencies Install the required Python libraries using pip.
  pip install -r requirements.txt
4.run run server script.
  python server.py
5.run the ngrok, to get the redirect url
  ngrok http 5001

6.open up a Facebook developer account, then add credentials in auth.py
    client_id: Your Facebook app ID.
    client_secret: Your Facebook app secret.
    redirect_uri: Your ngrok callback URL
7.Run the CLI.
  python cli.py





