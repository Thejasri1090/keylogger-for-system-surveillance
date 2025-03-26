# Keylogger for System Surveillance

## Introduction

In modern IT infrastructure, data security and recovery play a critical role in ensuring that sensitive data is preserved, particularly in cases of system failure or unauthorized access. Keyloggers, which are tools designed to monitor and record keystrokes, are essential for computer forensics. These tools help track user actions, retrieve lost data, and assist in investigating cybercrimes.

A **Keylogger** is a surveillance application designed to monitor and log keystrokes typed on a system, which can be used for tracking users and retrieving important data during cybercrime investigations. The software records all keystrokes, including special keys, and sends the captured data to an administrator or forensic analyst.

## Features

- **Keystroke Logging**: Captures every keystroke typed by the user.
- **Email Reports**: Sends the collected keystrokes via email after a certain number of keystrokes or on a time interval.
- **Customizable Parameters**: Configure time interval, email credentials, and keystroke threshold.
- **Invisible Operation**: Runs in the background without being detected by the user.
- **Password Protection**: Secures the software from unauthorized access.

## Requirements

Before using the KeyLogger, you need to install the following Python libraries:

- `pynput`: For listening to keyboard events.
- `smtplib`: For sending emails via SMTP.

You can install the required libraries using pip:

```bash
pip install pynput

## How It Works

### 1. **Keystroke Logging**

- The keylogger listens for keystroke events using the `pynput` library.
- It records every key press, including special keys like `Space`, `Esc`, etc., and stores the pressed keys in a log.

### 2. **Email Reports**

- The keylogger will send the collected keystrokes to a designated email account once the number of keystrokes exceeds the predefined threshold (default is 100).
- The log is sent via SMTP (email service provider: Gmail).
- After sending the email, the log is cleared, and the keystroke counter resets.

### 3. **Customizable Time Interval**

- The program runs indefinitely and can send reports periodically based on a time interval (default is 30 seconds).
- You can modify the time interval and other settings in the code.

## Code Overview

### KeyLogger Class

#### `__init__(self, time_interval: int, email: str, password: str, keystroke_threshold: int = 20)`

- **time_interval**: The time interval (in seconds) to check and send logs.
- **email**: The email address to send the logs to.
- **password**: The email password (App password if using Gmail).
- **keystroke_threshold**: The number of keystrokes before sending an email report.

#### `append_to_log(self, string: str)`

- Appends a keystroke to the log and checks if the keystroke threshold is reached. If so, it triggers the `report_n_send()` method to send an email.

#### `on_press(self, key)`

- Handles key press events.
- Records the keystroke and adds it to the log. Special keys like `Space` and `Esc` are also handled.

#### `send_mail(self)`

- Sends the log to the configured email address using Gmail’s SMTP service.
- After sending, the log is cleared, and the keystroke counter is reset.

#### `report_n_send(self)`

- Checks if the keystroke threshold is reached.
- Sends the email report if the threshold is met.
- Schedules the next check based on the specified time interval.

#### `start(self)`

- Starts the keylogger and listens for keystrokes using the `pynput` library.
- Initiates periodic email reporting.

## Usage Instructions

### 1. **Download the script**.

### 2. **Install dependencies**:

Install `pynput` using the following command:

```bash
pip install pynput

### 3. **Edit the email credentials**:

Replace `your_email@gmail.com` and `your_password` with your actual email and password (use an app password if using Gmail).

### 4. **Run the script**:

```bash
python keylogger.py

The keylogger will start capturing keystrokes and sending them via email once the threshold is met.

## Important Notes

- **Email Credentials**: You must replace the email and password with your own credentials. If you're using Gmail, it's recommended to use an App Password for security reasons.
- **Security**: The script does not encrypt the captured keystrokes. This is for educational purposes, and storing sensitive information like passwords in plain text is unsafe.
- **Stopping the Keylogger**: The keylogger will stop when the `Esc` key is pressed.

## Ethical Considerations

It is essential to understand the ethical implications of using keyloggers:

- **Authorization**: Always obtain permission from the target before deploying a keylogger.
- **Privacy**: Keyloggers should not be used to invade the privacy of individuals without consent.

This project is intended for educational purposes and cybersecurity research. It should not be used for malicious or illegal activities.
