# Automated Login and Tweet Posting Script

## Overview
This script automates the process of logging into a Twitter account (now referred to as X) and posting a tweet using Selenium and Python.

## Prerequisites
1. Python: Ensure you have Python 3.8 or higher installed.
2. Google Chrome: Install the latest version of Google Chrome.
3. ChromeDriver: Use the WebDriver Manager to automatically download the appropriate version of ChromeDriver.
4. Selenium Library: Install the Selenium Python library.

## Installation

1. Clone this repository or download the script file.
2. Install the required Python packages:
   ```bash
   pip install selenium webdriver-manager
   ```

## Configuration

Update the following variables in the script with your credentials:
- `email`: Your email address for the X (Twitter) account.
- `username`: Your username for the X (Twitter) account.
- `password`: Your password for the X (Twitter) account.

### Example:
```python
email = "your_email@example.com" # Change to your email
username = "your_username"       # Change to your username
password = "your_password"       # Change to your password
```

## Usage
1. Run the script:
   ```bash
   python script_name.py
   ```
   Replace `script_name.py` with the name of the Python script.

2. The script will perform the following steps:
   - Navigate to the X (Twitter) login page.
   - Log in using the provided credentials.
   - Post a predefined tweet.

## Customizing the Tweet
You can customize the tweet content by updating the `tweet` variable:

```python
tweet = "Your custom tweet content here!"
```

## Script Workflow
1. Open the X (Twitter) login page.
2. Input the email address and proceed.
3. Input the username and proceed.
4. Input the password and log in.
5. Wait for the tweet input field to load.
6. Enter the tweet and post it.
7. Close the browser.


