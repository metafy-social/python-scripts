# Internet Speed Checker

import speedtest
import time
import os


def main():

    # Clear the screen
    os.system('cls' if os.name == 'nt' else 'clear')

    # Print the title
    print('Internet Speed Checker')
    # Print the current time
    print(time.strftime('%H:%M:%S'))
    print("Connecting to server...")

    # Get the speed
    s = speedtest.Speedtest()
    s.get_best_server()
    s.download()
    s.upload()
    results_dict = s.results.dict()

    # Print the results
    print(f"Download: {results_dict['download'] / 1024 / 1024:.2f} Mbit/s")
    print(f"Upload: {results_dict['upload'] / 1024 / 1024:.2f} Mbit/s")
    print(f"Ping: {results_dict['ping']:.2f} ms")
    print(f"ISP: {results_dict['client']['isp']}")

    # Wait 5 seconds
    time.sleep(5)


if __name__ == "__main__":
    main()
