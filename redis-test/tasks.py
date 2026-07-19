from celery_app import app
import time

@app.task
def send_email(email):
    print("Sending email...")

    time.sleep(5)

    return f"Email sent to {email}"