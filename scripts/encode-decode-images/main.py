import argparse
import base64


def encode(filepath):
    image = open(filepath, 'rb')
    img_encoded = base64.b64encode(image.read())
    dest = open('encoded.txt', 'wb')
    dest.write(img_encoded)

def decode(dest_path):
    img_encoded = open('encoded.txt', 'rb')
    img_decoded = base64.b64decode(img_encoded.read()) 
    dest = open(dest_path, 'wb')
    dest.write(img_decoded)


parser = argparse.ArgumentParser()
parser.add_argument("-e", "--encode", required=False, help="Encode image.")
parser.add_argument("-d", "--decode", required=False, help="Decode image.")
args = vars(parser.parse_args())

if args["encode"]:
    encode(args["encode"])
else:
    decode(args["decode"])