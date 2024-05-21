import subprocess

def user_notification():
    try:
        # Run AppleScript command to play a system sound
        subprocess.run(
            ['osascript', '-e', 'display notification "Appointment Found, please fill in your data and book the appointment" sound name "Glass"'],
            check=True
        )
    except subprocess.CalledProcessError as e:
        print("Error:", e)

