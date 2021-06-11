import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

M1_DIR = 13
M1_PWM = 19
M2_DIR = 26
M2_PWM = 16
servoPin = 12

SERVO_MAX_DUTY    = 12
SERVO_MIN_DUTY    = 3

SLEEP_TERM = 0.5

GPIO.setup(M1_DIR, GPIO.OUT)
GPIO.setup(M1_PWM, GPIO.OUT)
GPIO.setup(M2_DIR, GPIO.OUT)
GPIO.setup(M2_PWM, GPIO.OUT)

def setServoPos(degree):
    GPIO.setup(servoPin, GPIO.OUT)

    servo = GPIO.PWM(servoPin, 50)
    servo.start(0)
    time.sleep(SLEEP_TERM)
    if degree > 180:
        degree = 180
    duty = SERVO_MIN_DUTY+(degree*(SERVO_MAX_DUTY-SERVO_MIN_DUTY)/180.0)
    servo.ChangeDutyCycle(duty)
    time.sleep(SLEEP_TERM)
    GPIO.cleanup(servoPin)

def stop():
    GPIO.output(M1_DIR, GPIO.LOW)
    GPIO.output(M1_PWM, GPIO.LOW)
    GPIO.output(M2_DIR, GPIO.LOW)
    GPIO.output(M2_PWM, GPIO.LOW)
    time.sleep(SLEEP_TERM)

def left():
    GPIO.output(M1_DIR, GPIO.HIGH)
    GPIO.output(M1_PWM, GPIO.LOW)
    GPIO.output(M2_DIR, GPIO.HIGH)
    GPIO.output(M2_PWM, GPIO.LOW)
    time.sleep(SLEEP_TERM)
    stop()

def right():
    GPIO.output(M1_DIR, GPIO.LOW)
    GPIO.output(M1_PWM, GPIO.HIGH)
    GPIO.output(M2_DIR, GPIO.LOW)
    GPIO.output(M2_PWM, GPIO.HIGH)
    time.sleep(SLEEP_TERM)
    stop()
    
def backward():
    GPIO.output(M1_DIR, GPIO.HIGH)
    GPIO.output(M1_PWM, GPIO.LOW)
    GPIO.output(M2_DIR, GPIO.LOW)
    GPIO.output(M2_PWM, GPIO.HIGH)
    time.sleep(SLEEP_TERM)
    stop()
    
def forward():
    GPIO.output(M1_DIR, GPIO.LOW)
    GPIO.output(M1_PWM, GPIO.HIGH)
    GPIO.output(M2_DIR, GPIO.HIGH)
    GPIO.output(M2_PWM, GPIO.LOW)
    time.sleep(SLEEP_TERM)
    stop()

if __name__ == "__main__":
    print("st")
    stop()
    print("fw")
    forward()
    print("b")
    backward()
    print("r")
    right()
    print("l")
    left()
    stop()
    for i in range(0,180,10):
        setServoPos(i)
    setServoPos(0)
    GPIO.cleanup()
