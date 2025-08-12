from datetime import datetime

def log_alert(message):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open("dos_alerts.log", "a") as f:
        f.write(f"{timestamp} - {message}\n")
