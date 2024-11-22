# Twitter Friends Migration Script

## Overview
This Python script automates the migration of your Twitter friends (accounts you follow) from an old account to a new one. It uses the Tweepy library to interact with the Twitter API, managing Twitter's daily follow limits and handling errors effectively.

## Prerequisites
1. **Python Environment**
   - Install Python 3.x.
   - Install the project dependencies:
     ```bash
     pip install requirements.txt
     ```

2. **Twitter Developer Account**
   - Create a developer account at the [Twitter Developer Portal](https://developer.twitter.com).
   - Generate the following credentials for both your old and new accounts:
     - API Key
     - API Secret Key
     - Access Token
     - Access Token Secret

## Usage Instructions

### 1. Clone the Repository
Clone the repository to your local machine:
```bash
git clone https://github.com/oukookowa/twitter-friends-migration.git
cd twitter-friends-migration
```

### 2. Set Up API Credentials
Replace placeholder credentials in the script with your actual API keys and tokens for both accounts. For better security, use a .env file with the python-dotenv library.

Edit the script as follows:

```python
OLD_API_KEY = "your_old_account_api_key"
OLD_API_SECRET = "your_old_account_api_secret"
OLD_ACCESS_TOKEN = "your_old_account_access_token"
OLD_ACCESS_SECRET = "your_old_account_access_secret"

NEW_API_KEY = "your_new_account_api_key"
NEW_API_SECRET = "your_new_account_api_secret"
NEW_ACCESS_TOKEN = "your_new_account_access_token"
NEW_ACCESS_SECRET = "your_new_account_access_secret"
```

### 3. Test the Connection
Run the script to test authentication and connection:
```bash
python test_connection.py
```

### 4. Run the Script
Run the script to start migrating your friends list:

```bash
python xbot.py
```

## Script Execution

When the script is executed, it performs the following tasks:

- **Authenticates Both Accounts**: Logs into both the old and new Twitter accounts using the provided credentials.
- **Fetches Friends**: Retrieves a list of accounts followed by the old account.
- **Automates Following**: Automatically follows the retrieved accounts from the new account.
- **Respects Daily Follow Limit**: Adheres to Twitter's daily follow limit of 400 users per day, pausing and resuming as needed.
- **Error Handling**: Catches errors like rate limits, authentication failures, or protected accounts.
- **Displays Progress**: Outputs the progress directly in the terminal, showing details about the follow attempts.

## Features

### Current Functionality
- **Authentication**: Logs into both old and new Twitter accounts using provided credentials.
- **Fetch Friends**: Retrieves a list of accounts followed by the old account.
- **Follow on New Account**: Automates following these accounts from the new account.
- **Daily Follow Limit Management**: Automatically pauses if the 400-follow-per-day limit is reached and resumes the next day.
- **Error Handling**: Handles issues such as authentication failures, rate limits, and protected accounts gracefully.

### Adding Extra Features
Developers can enhance the script by implementing additional functionality:
- **Unfollow Old Account Followers**: Add functionality to unfollow all accounts from the old account once they've been migrated.
- **Environment Variables**: Replace hardcoded credentials with `.env` file management using libraries like `python-dotenv` for better security.
- **Exclude Certain Users**: Modify the script to exclude specific accounts, such as inactive users or bots.
- **GUI Interface**: Create a user-friendly graphical interface for non-technical users.
- **Logging**: Integrate logging to track successful and failed follow attempts in a log file.

## How to Contribute
Fork the Repository: Go to the GitHub Repository and click `Fork`.
Clone the Forked Repo:
```bash
git clone https://github.com/oukookowa/twitter-friends-migration.git
```
Make Changes: Add new features or improve the code.

Push Changes:
```bash
git add .
git commit -m "Added new feature"
git push origin main
```
Submit a Pull Request: Go to the original repository and click `New Pull Request`.

## Security Notes
Keep Credentials Secure: Use `.gitignore` to exclude sensitive files from version control.
Use Environment Variables: Store API keys and tokens in a `.env` file.
Compliance: Ensure the script adheres to `Twitter API Policies`.

## Conclusion
This script offers a scalable solution for migrating Twitter friends between accounts. With opportunities for customization and enhancements, it can cater to various user needs.

Feel free to contribute, experiment, and improve!

Happy Coding!
