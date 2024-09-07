# LinkedIn Automation Scripts

This project provides a set of Python scripts to automate various tasks on LinkedIn, including logging in, scraping group admins, following profiles, and sending connection requests. The scripts use Selenium WebDriver for browser automation and `requests` for internet connectivity checks.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Setup Instructions](#setup-instructions)
  - [1. Clone the Repository](#1-clone-the-repository)
  - [2. Create a Virtual Environment](#2-create-a-virtual-environment)
  - [3. Activate the Virtual Environment](#3-activate-the-virtual-environment)
  - [4. Install Dependencies](#4-install-dependencies)
  - [5. Configure the Scripts](#5-configure-the-scripts)
- [Running the Scripts](#running-the-scripts)
  - [1. Run the Main Script](#1-run-the-main-script)
  - [2. Individual Scripts](#2-individual-scripts)
- [Script Descriptions](#script-descriptions)
  - [`login.py`](#loginpy)
  - [`scrape.py`](#scrapepy)
  - [`follow.py`](#followpy)
  - [`connect.py`](#connectpy)
- [Important Notes](#important-notes)
- [Troubleshooting](#troubleshooting)
- [License](#license)

---

## Features

- **Automated Login**: Logs into LinkedIn using your credentials, handling cookies and potential two-factor authentication (2FA).
- **Scraping Group Admins**: Scrapes the profile URLs of admins from your LinkedIn groups.
- **Following Profiles**: Automates following the scraped profiles.
- **Sending Connection Requests**: Sends connection requests to the scraped profiles.
- **Internet Connectivity Checks**: Verifies internet connection before performing each major task.

## Prerequisites

- **Python 3.x**: Ensure you have Python 3 installed.
- **Google Chrome Browser**: The scripts use Chrome for automation.
- **ChromeDriver**: Download the ChromeDriver that matches your Chrome browser version from [here](https://chromedriver.chromium.org/downloads) and note its file path.
- **LinkedIn Account**: A valid LinkedIn account is required.
- **Selenium WebDriver**: Installed via `pip install selenium`.

## Setup Instructions

### 1. Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/javeria2108/linkedin-automation.git
cd linkedin-automation
```

### 2. Create a Virtual Environment

Create a new virtual environment to manage dependencies:

```bash
python -m venv env
```

### 3. Activate the Virtual Environment

Activate the virtual environment:

- **On Windows**:

  ```bash
  .\env\Scripts\activate
  ```

- **On macOS/Linux**:

  ```bash
  source env/bin/activate
  ```

### 4. Install Dependencies

Install the required Python packages using `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 5. Configure the Scripts

Before running the scripts, you need to configure them:

1. **Update ChromeDriver Path**:
   - In `login.py` (or the main script), update the path to your `chromedriver.exe`:
     ```python
     service = Service('path/to/your/chromedriver.exe')
     ```

2. **Set Your LinkedIn Credentials**:
   - In `login.py`, replace the placeholder email and password with your LinkedIn credentials:
     ```python
     email_field.send_keys('your_email@example.com')
     password_field.send_keys('your_password')
     ```

3. **Handle Two-Factor Authentication (If Enabled)**:
   - The script will prompt you to enter your 2FA code during login if required.

---

## Running the Scripts

### 1. Run the Main Script

You can create a main script to run all tasks sequentially with internet checks in between:

```python
# main.py
from login import login, setup_driver, wait_for_internet
from scrape import scrape_admins
from follow import follow_profiles
from connect import connect

if __name__ == "__main__":
    wait_for_internet()
    driver = setup_driver()
    login(driver)
    driver.quit()

    scrape_admins()
    follow_profiles()
    connect()
```

Run the main script:

```bash
python main.py
```

### 2. Individual Scripts

Alternatively, you can run each script individually:

- **Login**:
  ```bash
  python login.py
  ```
- **Scrape Admins**:
  ```bash
  python scrape.py
  ```
- **Follow Profiles**:
  ```bash
  python follow.py
  ```
- **Send Connection Requests**:
  ```bash
  python connect.py
  ```

---

## Script Descriptions

### `login.py`

Handles logging into LinkedIn, managing cookies for session persistence, and dealing with two-factor authentication.

- **Functions**:
  - `wait_for_internet()`: Checks for internet connectivity.
  - `setup_driver()`: Initializes the Selenium WebDriver.
  - `login(driver)`: Logs into LinkedIn using provided credentials.
  - `save_cookie(driver, path)`: Saves cookies to a file.
  - `load_cookie(driver, path)`: Loads cookies from a file.

### `scrape.py`

Scrapes the profile URLs of group admins from your LinkedIn groups.

- **Functions**:
  - `scrape_admins()`: Navigates to groups, loads all groups, and scrapes admin profiles.
  - Saves the scraped profile URLs to `admin_profiles.txt`.

### `follow.py`

Automates following the profiles listed in `admin_profiles.txt`.

- **Functions**:
  - `follow_profiles()`: Visits each profile URL and attempts to follow.

### `connect.py`

Sends connection requests to the profiles listed in `admin_profiles.txt`.

- **Functions**:
  - `connect()`: Visits each profile URL and sends a connection request.

---

## Important Notes

- **Use Responsibly**: Automating actions on LinkedIn may violate their Terms of Service. Use these scripts responsibly and at your own risk.
- **Delays and Randomization**: The scripts include random delays to mimic human behavior and reduce the risk of detection.
- **Two-Factor Authentication**: If you have 2FA enabled, be prepared to enter your code when prompted.
- **Profile Restrictions**: Depending on your LinkedIn account, you may have limitations on the number of profiles you can view or actions you can perform daily.
- **Chromedriver Version**: Ensure that the version of Chromedriver matches your installed version of Google Chrome.

---

## Troubleshooting

- **Chromedriver Errors**:
  - Ensure the `chromedriver.exe` path is correct.
  - Chromedriver version must match your Chrome browser version.

- **Login Issues**:
  - Double-check your LinkedIn credentials in `login.py`.
  - If experiencing 2FA issues, make sure the code input is correct.

- **Element Not Found Errors**:
  - LinkedIn may update their website structure. You may need to update the XPath or CSS selectors in the scripts.

- **Internet Connectivity**:
  - Ensure you have a stable internet connection. The scripts check for connectivity before proceeding.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

**Disclaimer**: This project is intended for educational purposes. Automating actions on websites may violate their Terms of Service. The author is not responsible for any misuse of this software.