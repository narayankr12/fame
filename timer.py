import time

def countdown_timer(seconds):
    print(f"⏱️ Countdown started for {seconds} seconds...\n")
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = f"{mins:02d}:{secs:02d}"
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1
    print("🚨 Time's up!")


try:
    duration = int(input("Enter countdown time in seconds: "))
    countdown_timer(duration)
except ValueError:
    print("❌ Please enter a valid number.")
