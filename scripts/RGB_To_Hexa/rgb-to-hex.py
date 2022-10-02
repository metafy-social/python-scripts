def rgb_to_hex(rgb):
    return '%02x%02x%02x' % rgb


print("Enter the value of RGB color in (X,Y,Z) format:")
X = int(input("Enter value of X: "))
Y = int(input("Enter value of Y: "))
Z = int(input("Enter value of Z: "))
hex = rgb_to_hex((X, Y, Z))
print("The hexadecimal value is: {}" .format(hex))
