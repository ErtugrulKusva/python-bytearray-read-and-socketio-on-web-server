#!/usr/bin/env python
import serial
import time
import numpy
from threading import Thread
from flask import Flask, render_template, session, request
from flask_socketio import SocketIO, emit, join_room, leave_room, \
    close_room, rooms, disconnect
#async_mode = None
async_mode = "threading"
#app = Flask(__name__)
app = Flask(__name__, static_url_path="", static_folder="static")
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode=async_mode)
#socketio = SocketIO(app)
thread = None



def Highlowcalc(h,l):#High-Low byte calculator-floater |||Floatlara göre High Low byte veri hesaplayıcı fonksiyon
    hesap = ((int(h)* 256) + l) / 10
    return hesap
def Highlowcalc1(h,l):#High-Low byte calculator-integer |||Integerlara göre High Low byte veri hesaplayıcı fonksiyon 
    hesap = ((int(h)* 256) + l)
    return hesap

def background_thread():
  z1baudrate = 9600
  port1= 'COM5'  # set the correct port before run it if you are using raspberry pi / linux you should define like this--> '/dev/ttyS0'

  z1serial = serial.Serial(port=port1, baudrate=z1baudrate)
  z1serial.timeout = 0.05  # set read timeout
  # print z1serial  # debug serial.
  print(z1serial.is_open)  # True for opened
  
  if z1serial.is_open:
    while True:
        #socketio.sleep(2)
        temperature="222"#temperature default
        sizeofData = z1serial.inWaiting()
        if sizeofData:
            z1serial.flush()
            incomingData =[]
            out= z1serial.readline()#Serial reading
            incomingData = list(out)
            if(len(incomingData) == 20):            
              #print("size of array: ",len(incomingData))
              #print(incomingData)            
                        
              temperature = Highlowcalc(incomingData[0], incomingData[1])
              temperatureispositive = int(incomingData[2])
              if( temperatureispositive == 0):
                  temperature = temperature * (-1)                  
                 
              humidity = Highlowcalc(incomingData[5], incomingData[6])
              height = Highlowcalc(incomingData[3], incomingData[4])              
              pressure = Highlowcalc(incomingData[7], incomingData[8])
              speed =incomingData[9]
              gyroX= Highlowcalc(incomingData[10], incomingData[11])
              gyroXispositive = int(incomingData[12])
              if( gyroXispositive== 0):
                  gyroX = gyroX * (-1)                  
              
              gyroY= Highlowcalc(incomingData[13], incomingData[14])
              gyroYispositive = int(incomingData[15])
              if( gyroYispositive== 0):
                  gyroY = gyroY * (-1)                  
              
              gyroZ= Highlowcalc(incomingData[16], incomingData[17])
              gyroZispositive = int(incomingData[18])
              if( gyroZispositive== 0):
                  gyroZ = gyroZ * (-1)                  
               
                             
              if(incomingData[19] ==int (numpy.mean(incomingData))):#checkSum byte
                  print("Incoming datas have been verified")
                  #print(incomingData[0],"----",incomingData[1]," Sıcaklık(°C):", temperature , " humidity(%):",humidity, "height(m):", height)
                  socketio.sleep(0.2)
                  socketio.emit('seribas', {'temperature': str(temperature), 'humidity':str(humidity),'speed':str(speed), 'height': str(height),'pressure': str(pressure)}, namespace='/seriGonder') #sending data to socket
             #else:
            #print('no data')
        #time.sleep(0.05)
        socketio.sleep(0.05)
        
        #socketio.sleep(0.05)
  else:
    print('z1serial not open')

@app.route('/')
def index():
     global thread
     if thread is None:
        thread = Thread(target=background_thread)
        thread.start()
     #return render_template('esp8266.html', async_mode=socketio.async_mode)
     return render_template('index.html')


@socketio.on('connect', namespace='/connection_info')
def test_connect():
    # global thread
    # with thread_lock:
    #     if thread is None:
    #         thread = socketio.start_background_task(background_thread)
    emit('my_response', {'data': 'Connected', 'count': 0})


@socketio.on('disconnect', namespace='/connection_info')
def test_disconnect():
    print('Client disconnected', request.sid)


if __name__ == '__main__':
    socketio.run(app,host='0.0.0.0', port=3000, debug=True)