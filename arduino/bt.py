import serial
import time
ser = serial.Serial(port='COM6', baudrate=9600, bytesize=serial.EIGHTBITS)


while True:
    # inputVal = input("Enter on or off :")
    # ser.write(bytes(inputVal, 'utf-8'))
    # time.sleep(0.05)
    output = ser.readline().decode().rstrip()
    print(output)