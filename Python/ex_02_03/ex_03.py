xh = input("Enter hours: ")
xr = input("Enter rate: ")
xsal = float(xh) * float(xr)
if xsal < 50:
    print("Pay of", xsal,"is less" )
else:
    print("Pay of", xsal,"is ok")