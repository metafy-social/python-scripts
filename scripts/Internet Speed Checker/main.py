import speedtest
import matplotlib.pyplot as plt
import pandas as pd


def run_speed_test():

    download_speeds = []
    upload_speeds = []
    ping_values = []

    # Run the speedtest while the user wants to continue running iterations
    while True:
        print('Internet Speed Checker')

        # Get the speed
        s = speedtest.Speedtest()
        s.get_best_server()
        s.download()
        s.upload()
        results_dict = s.results.dict()

        # Append speeds and ping
        download_speeds.append(results_dict['download'] / 1024 / 1024)
        upload_speeds.append(results_dict['upload'] / 1024 / 1024)
        ping_values.append(results_dict['ping'])

        # Print the results
        print(f"Iteration {len(download_speeds)}:")
        print(f"  Download Speed: {download_speeds[-1]:.2f} Mbit/s")
        print(f"  Upload Speed: {upload_speeds[-1]:.2f} Mbit/s")
        print(f"  Ping: {ping_values[-1]:.2f} ms")
        print(f"  ISP: {results_dict['client']['isp']}")

        # Ask the user whether they want to run another iteration
        user_input = input("Do you want to run another iteration? (yes/no): ").lower()
        if user_input != 'yes':
            break

    avg_download_speed = sum(download_speeds) / len(download_speeds)
    avg_upload_speed = sum(upload_speeds) / len(upload_speeds)
    avg_ping = sum(ping_values) / len(ping_values)

    max_download_iteration = download_speeds.index(max(download_speeds)) + 1
    max_upload_iteration = upload_speeds.index(max(upload_speeds)) + 1
    min_ping_iteration = ping_values.index(min(ping_values)) + 1

    # Storing results
    df = pd.DataFrame({
        'Iteration': [i for i in range(1, len(download_speeds) + 1)],
        'Download Speed': download_speeds,
        'Upload Speed': upload_speeds,
        'Ping': ping_values
    })

    print("\nSummary:")
    print(f"  Average Download Speed: {avg_download_speed:.2f} Mbit/s")
    print(f"  Average Upload Speed: {avg_upload_speed:.2f} Mbit/s")
    print(f"  Average Ping: {avg_ping:.2f} ms")
    print(f"  Iteration with Highest Download Speed: Iteration {max_download_iteration}")
    print(f"  Iteration with Highest Upload Speed: Iteration {max_upload_iteration}")
    print(f"  Iteration with Lowest Ping: Iteration {min_ping_iteration}")

    # Plot the results with integer x-axis labels
    plt.plot(df['Iteration'], df['Download Speed'], label='Download Speed')
    plt.plot(df['Iteration'], df['Upload Speed'], label='Upload Speed')
    plt.plot(df['Iteration'], df['Ping'], label='Ping')
    plt.xlabel('Iteration Number')
    plt.ylabel('Speed/Ping (Mbit/s)')
    plt.title('Internet Speed Test Results')
    plt.legend()
    plt.show()


if __name__ == "__main__":
    run_speed_test()