import tweepy
import time
from datetime import datetime
from decouple import config

# Main Execution ---
def main():
    # Get the list of people you're following from the old account
    old_following = get_old_account_following()
    
    if old_following:
        # Follow them on the new account
        follow_accounts(old_following)
    else:
        print("No users to follow from the old account.")

# --- API Credentials for both old and new accounts ---
# Replace with your actual credentials
OLD_API_KEY = config("OLD_API_KEY")
OLD_API_SECRET = config("OLD_API_SECRET")
OLD_ACCESS_TOKEN = config("OLD_ACCESS_TOKEN")
OLD_ACCESS_SECRET = config("OLD_ACCESS_SECRET")

NEW_API_KEY = config("NEW_API_KEY")
NEW_API_SECRET = config("NEW_API_SECRET")
NEW_ACCESS_TOKEN = config("NEW_ACCESS_TOKEN")
NEW_ACCESS_SECRET = config("NEW_ACCESS_SECRET")

# --- Authentication for both old and new Twitter accounts ---
def authenticate(api_key, api_secret, access_token, access_secret):
    auth = tweepy.OAuthHandler(api_key, api_secret)
    auth.set_access_token(access_token, access_secret)
    return tweepy.API(auth, wait_on_rate_limit=True)

# --- Authenticate Old and New Accounts ---
old_api = authenticate(OLD_API_KEY, OLD_API_SECRET, OLD_ACCESS_TOKEN, OLD_ACCESS_SECRET)
new_api = authenticate(NEW_API_KEY, NEW_API_SECRET, NEW_ACCESS_TOKEN, NEW_ACCESS_SECRET)

# --- Global Variables ---
follow_count = 0
last_reset_time = datetime.now().date()  # Track the last reset time

# --- Function to fetch the list of friends from the old account ---
def get_old_account_following():
    """Fetches the list of users followed by the old account."""
    friends = []
    try:
        # Get the list of friends (people you follow) from the old account
        for friend in tweepy.Cursor(old_api.get_friends).items():
            friends.append(friend.screen_name)
        print(f"Fetched {len(friends)} accounts from the old account.")
        return friends
    except tweepy.errors.TweepyException as e:  # Updated error class
        print(f"Error fetching followers: {e}")
        return []

# --- Function to follow the users from the old account to the new account ---
def follow_accounts(account_to_follow):
    global follow_count, last_reset_time

    # Check if a new day has started, reset follow count if so
    if datetime.now().date() != last_reset_time:
        follow_count = 0
        last_reset_time = datetime.now().date()

    # Loop through each user to follow
    for username in account_to_follow:
        # Check if we've reached the follow limit for the day
        if follow_count >= 400:
            print("Follow limit reached for today. Pausing for the next 24 hours...")
            time.sleep(60 * 60 * 24)  # Wait 24 hours before resuming
            follow_count = 0  # Reset follow count after a day
            last_reset_time = datetime.now().date()

        try:
            # Follow the user
            new_api.create_friendship(screen_name=username)
            print(f"Followed: {username}")
            follow_count += 1
            time.sleep(1)  # Pause for 1 second between follows to avoid rate limits
        except tweepy.errors.TweepyException as e:  # Updated error class
            print(f"Error following {username}: {e}")
            continue

if __name__ == "__main__":
    main()