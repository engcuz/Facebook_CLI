import requests

# post  status update on  authenticatd user
def post_status(access_token, message):
   
   
    # endpoint 
    url = "https://graph.facebook.com/me/feed"
    params = {"access_token": access_token, "message": message}
    # POST Request:
    response = requests.post(url, params=params)

    # return json resonse 
    return response.json()

    # retrieve the user profile details
def view_profile(access_token):
    
    url = "https://graph.facebook.com/me"
    params = {"access_token": access_token, "fields": "id,name"}
    response = requests.get(url, params=params)
    return response.json()

    #           view the recent posts on the user's feed
def view_recent_posts(access_token):
    
    url = "https://graph.facebook.com/me/feed"
    params = {"access_token": access_token}
    response = requests.get(url, params=params)
    return response.json()

    #        like a specific post by its ID
def like_post(access_token, post_id):
    
    url = f"https://graph.facebook.com/{post_id}/likes"
    params = {"access_token": access_token}
    response = requests.post(url, params=params)
    return response.json()

        # comment on  specific post by its ID
def comment_on_post(access_token, post_id, comment):
    
    url = f"https://graph.facebook.com/{post_id}/comments"
    params= {"access_token": access_token, "message": comment}
    response =requests.post(url, params=params)
    return response.json()

        # delete a specific post by its ID
def delete_post(access_token, post_id):
    
    url = f"https://graph.facebook.com/{post_id}"
    params = {"access_token": access_token}
    response = requests.delete(url, params=params)
    return response.json()

    # view the user's notifications
def view_notifications(access_token):
    
    url = "https://graph.facebook.com/me/notifications"
    params = {"access_token": access_token}
    response = requests.get(url, params=params)
    return response.json()

    # list the user's friends
def list_friends(access_token):
    
    url = "https://graph.facebook.com/me/friends"
    params = {"access_token": access_token, "fields": "name"}
    response = requests.get(url, params=params)
    return response.json()

    # send friend request to another user by user ID
def send_friend_request(access_token, user_id):
    
    url = f"https://graph.facebook.com/{user_id}/friends"
    params = {"access_token": access_token}
    response = requests.post(url, params=params)
    return response.json()

    # unfriend a user by their user ID
def unfriend_user(access_token, user_id):
    
    url = f"https://graph.facebook.com/me/friends/{user_id}"
    params = {"access_token": access_token}
    response = requests.delete(url, params=params)
    return response.json()

    # send DM to user by their user ID
def send_direct_message(access_token, user_id, message):
    
    url = f"https://graph.facebook.com/me/messages"
    params = {"access_token": access_token, "recipient": {"id": user_id}, "message": {"text": message}}
    response = requests.post(url, json=params)
    return response.json()
