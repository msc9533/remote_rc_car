import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)

def stop():
    GPIO.output(12, GPIO.LOW)
    GPIO.output(5, GPIO.LOW)
    GPIO.output(6, GPIO.LOW)
    GPIO.output(13, GPIO.LOW)
    time.sleep(1)

def backward():
    GPIO.output(12, GPIO.LOW)
    GPIO.output(5, GPIO.HIGH)
    
    GPIO.output(6, GPIO.HIGH)
    GPIO.output(13, GPIO.LOW)
    
    time.sleep(1)

    stop()
def forward():
    GPIO.output(12, GPIO.HIGH)
    GPIO.output(5, GPIO.LOW)
    
    GPIO.output(6, GPIO.LOW)
    GPIO.output(13, GPIO.HIGH)
    time.sleep(1)
    stop()
    
def left():
    GPIO.output(12, GPIO.LOW)
    GPIO.output(5, GPIO.HIGH)
    
    GPIO.output(6, GPIO.LOW)
    GPIO.output(13, GPIO.HIGH)
    time.sleep(1)
    stop()
    
def right():
    GPIO.output(12, GPIO.HIGH)
    GPIO.output(5, GPIO.LOW)
    
    GPIO.output(6, GPIO.HIGH)
    GPIO.output(13, GPIO.LOW)
    time.sleep(1)
    stop()

if __name__ == "__main__":
    stop()
    time.sleep(3)
    forward()
    time.sleep(3)
    backward()
    time.sleep(3)
    right()
    time.sleep(3)
    left()
    time.sleep(3)
    stop()
    GPIO.cleanup()
