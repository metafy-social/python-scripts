def CMYKtoRGB(c, m, y, k) :
    c=float(c)/100.0
    m=float(m)/100.0
    y=float(y)/100.0
    k=float(k)/100.0
    r=round(255.0-((min(1.0, c*(1.0-k)+k))*255.0))
    g=round(255.0-((min(1.0, m*(1.0-k)+k))*255.0))
    b=round(255.0-((min(1.0, y*(1.0-k)+k))*255.0))
    return (r,g,b)

print("Welcome To CMYK to RGB Convertor || INPUT CMYK codes and rest leave it to the convertor\n")
c=int(input("C Value: "))
m=int(input("M Value: "))
y=int(input("Y Value: "))
k=int(input("K Value: "))

print("Processing...")
print("\nYour RGB values are", CMYKtoRGB(c,m,y,k))