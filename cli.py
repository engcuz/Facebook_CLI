from api import (
    post_status,
    view_profile,
    view_recent_posts,
    like_post,
    comment_on_post,
    delete_post,
    view_notifications,
    list_friends,
    send_friend_request,
    unfriend_user,
    send_direct_message,
)
 
 # get the token and saved to file
def get_access_token():
    try:
        with open('access_token.txt', 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        print("Access token file not found. Please generate the token first.")
        return None

ACCESS_TOKEN = get_access_token()

if not ACCESS_TOKEN:
    print("Exiting... Access token not available.")
    exit()

def display_menu():
    print("\nFacebook CLI Main Menu:")
    print("1. Post a status update")
    print("2. View profile details")
    print("3. View recent posts")
    print("4. Like a post")
    print("5. Comment on a post")
    print("6. Delete a post")
    print("7. View notifications")
    print("8. List friends")
    print("9. Send a friend request")
    print("10. Unfriend a user")
    print("11. Send a direct message")
    print("0. Exit")

def run_facebook_cli():
    global ACCESS_TOKEN
    while True:
        display_menu()
        choice = input("\nEnter the number of your choice: ").strip()

        if choice == "1":
            message = input("Enter your status message: ")
            response = post_status(ACCESS_TOKEN, message)
            print("Response:", response)

        elif choice == "2":
            response = view_profile(ACCESS_TOKEN)
            print("Profile Details:", response)

        elif choice == "3":
            response = view_recent_posts(ACCESS_TOKEN)
            # Check if data exists in the response
            if 'data' in response:
                print("\nRecent Posts:")
                for post in response['data']:
                 # Extract and display Post ID and Message
                     print(f"Post ID: {post['id']}, Message: {post.get('message', 'No message')}")
            else:
                print("No recent posts found.")


        elif choice == "4":
            post_id = input("Enter the Post ID to like: ")
            response = like_post(ACCESS_TOKEN, post_id)
            print("Response:", response)

        elif choice == "5":
            post_id = input("Enter the Post ID to comment on: ")
            comment = input("Enter your comment: ")
            response = comment_on_post(ACCESS_TOKEN, post_id, comment)
            print("Response:", response)

        elif choice == "6":
            post_id = input("Enter the Post ID to delete: ")
            response = delete_post(ACCESS_TOKEN, post_id)
            print("Response:", response)

        elif choice == "7":
            response = view_notifications(ACCESS_TOKEN)
            print("Notifications:", response)

        elif choice == "8":
            response = list_friends(ACCESS_TOKEN)
            print("Friends:", response)
            friends = response.get("data", [])
            if friends:
                for friend in friends:
                    print(f"Name: {friend.get('name')}, ID: {friend.get('id')}")
            else:
                print("No friends found or they have not authorized this app.")

        elif choice == "9":
            user_id = input("Enter the User ID to send a friend request: ")
            response = send_friend_request(ACCESS_TOKEN, user_id)
            print("Response:", response)

        elif choice == "10":
            user_id = input("Enter the User ID to unfriend: ")
            response = unfriend_user(ACCESS_TOKEN, user_id)
            print("Response:", response)

        elif choice == "11":
            user_id = input("Enter the User ID to message: ")
            message = input("Enter your message: ")
            response = send_direct_message(ACCESS_TOKEN, user_id, message)
            print("Response:", response)

        elif choice == "0":
            print("Exiting CLI.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    run_facebook_cli()
