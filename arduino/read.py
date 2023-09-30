import serial,time,keyboard,os
ser = serial.Serial(port='COM3', baudrate=9600, bytesize=serial.EIGHTBITS)
while True:
    output = ser.readline().decode().rstrip()
    # print(output)
    if output =='4133':
        os.system('notepad')
