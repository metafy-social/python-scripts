import sys
import webbrowser

if len(sys.argv) > 1:
    map_string = ' '.join(sys.argv[1:])
    webbrowser.open('https://www.google.com/maps/place/' + map_string)

else:
    print("Pass the string as command line argument.")


