# Write your code here :-)
from adafruit_httpserver import Request, Response
import busio, board

uart = busio.UART(board.TX, board.RX, baudrate=9600)

def setTime(request: Request):
    print("setTime request received")
    data = request.form_data
    dataToSend = [
        0,  # ID for setting time
        int(data["year"]),
        int(data["month"]),
        int(data["day"]),
        int(data["weekDay"]),
        int(data["hour"]),
        int(data["minute"]),
        int(data["second"]),
        99   # ID for command termination
    ]
    uart.write(bytes(dataToSend))
    return Response(request, body="Time Set Successfully", content_type="text/plain")

def getTime(request: Request):
    print("getTime")
    return Response(request, body="The time is: ", content_type="text/plain")


def setAlarm(request: Request):
    print("setAlarm")
    return Response(request, body="Alarm Set Successfully", content_type="text/plain")

def getAlarm(request: Request):
    print("getAlarm")
    return Response(request, body="The alarms are: ", content_type="text/plain")

def removeAlarm(request: Request):
    print("removeAlarm")
    return Response(request, body="Successfully Removed Alarm", content_type="text/plain")

