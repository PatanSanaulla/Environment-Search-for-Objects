import numpy as np
import cv2 as cv2

try:
    import vrep
    import sys
    from threading import Thread
    import time
    from time import sleep

except:
    print ('--------------------------------------------------------------')
    print ('"vrep.py" could not be imported. This means very probably that')
    print ('either "vrep.py" or the remoteApi library could not be found.')
    print ('Make sure both are in the same folder as this file,')
    print ('or appropriately adjust the file "vrep.py"')
    print ('--------------------------------------------------------------')
    print ('')

print ('Program started to execute in V-Rep')
vrep.simxFinish(-1) # just in case, close all opened connections
clientID = vrep.simxStart('127.0.0.1',19997,True,True,5000,5) # Connect to V-REP

if clientID != -1:
    print('Connection Established to remote API server')

    # Now send some data to V-REP in a non-blocking fashion:
    vrep.simxAddStatusbarMessage(clientID, 'Hello V-REP from Python!', vrep.simx_opmode_oneshot)  # This message should be printed on your CopelliaSim in the bottm

    returnCode, vsHandle = vrep.simxGetObjectHandle(clientID, 'Vision_sensor', vrep.simx_opmode_oneshot_wait)
    print(vsHandle)
    i = 0
    while True:
        #[err,res,img]=vrep.simxGetVisionSensorImage(clientID,vsHandle,0,vrep.simx_opmode_buffer)
        #if (err == vrep.simx_return_ok):
         #   imageAcquisitionTime = vrep.simxGetLastCmdTime(clientID)

        #[ret, detState, auxPackets] = vrep.simxReadVisionSensor(clientID,vsHandle,vrep.simx_opmode_buffer)

        res, resolution, image = vrep.simxGetVisionSensorImage(clientID, vsHandle, 0, vrep.simx_opmode_streaming)
        while (vrep.simxGetConnectionId(clientID) != -1):
            res, resolution, image = vrep.simxGetVisionSensorImage(clientID, vsHandle, 0, vrep.simx_opmode_buffer)
            if res == vrep.simx_return_ok:
                #res = vrep.simxSetVisionSensorImage(clientID, v1, image, 0, vrep.simx_opmode_oneshot)
                print("image OK!!!")
                img = np.array(image, dtype=np.uint8)
                img.resize([resolution[1], resolution[0], 3])
                img = cv2.rotate(img, cv2.ROTATE_180)
                cv2.imshow('image', img)
                imageName = 'image'+str(i)+'.jpg'
                cv2.imwrite(imageName,img)
                i = i+1
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            elif res == vrep.simx_return_novalue_flag:
                print("no image yet")
                pass
            else:
                print(res)

        sleep(1)
        print ("______________________________________________")

    # Before closing the connection to V-REP, make sure that the last command sent out had time to arrive. You can guarantee this with (for example):
    vrep.simxGetPingTime(clientID)

    # Now close the connection to V-REP:
    vrep.simxFinish(clientID)
else:
    print ('Failed connecting to remote API server')
    sys.exit("Connection failed")
print ('Program ended')


