from msilib.schema import Icon
import time
from plyer import notification

if __name__ == "__main__":
     while True:
        notification.notify(
             title = "idle Alert",
             message = "Research has linked sitting for long periods of time with a number of health concerns. They include obesity and a cluster of conditions — increased blood pressure, high blood sugar.",
             timeout=10

        )
        time.sleep(60*60)

