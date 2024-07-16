import psutil
import time

def cpu(threshold):
    try:
        while True:
            cpu_usage = psutil.cpu_percent(interval=1) #getting cpu percentage from the psutil

            print(f"Monitoring CP+U usage ... {cpu_usage}%") #display

            if cpu_usage > threshold: 
                print(f"Alert! CPU usage exceeds threshold:{threshold}%.")

            time.sleep(2) #2 seconds interval

    except KeyboardInterrupt:
        print("\nMonitoring interrupted by user.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__": #using the __name__ and main to determine the percentage either from module or not
    threshold_percentage = 80

    cpu(threshold_percentage)
