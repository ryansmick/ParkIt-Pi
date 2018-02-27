import RPi.GPIO as GPIO
import time

class DistanceSensor:
    def __init__(self, trig, echo, debug=False):
        self.trig = trig
        self.echo = echo
        self.debug = debug

        GPIO.setmode(GPIO.BCM)

        if self.debug:
            print("Distance measurement in progress...")
    
        GPIO.setup(self.trig,GPIO.OUT)
        GPIO.setup(self.echo,GPIO.IN)

        GPIO.output(self.trig, False)
        
        if self.debug:
            print("Waiting for sensor to settle...")

        time.sleep(2)

        if self.debug:
            print("Sensor ready!")

    # Read the distance given by the sensor
    # num_samples is the number of samples to average the distance over. Higher number gives more accuracy. Default is 1
    def read_distance(self, num_samples=1):

        if num_samples < 1:
            raise ValueError("num_samples must be greater than 1")

        total_distance = 0
        for i in range(num_samples):
            GPIO.setmode(GPIO.BCM)

            GPIO.setup(self.trig,GPIO.OUT)
            GPIO.setup(self.echo,GPIO.IN)

            GPIO.output(self.trig, True)
            time.sleep(0.00001)
            GPIO.output(self.trig, False)

            pulse_start = time.time()
            while GPIO.input(self.echo)==0:
                pulse_start = time.time()

            while GPIO.input(self.echo)==1:
                pulse_end = time.time()

            pulse_duration = pulse_end - pulse_start

            distance = pulse_duration * 17150
            total_distance += distance

        measured_distance = total_distance/num_samples

        if self.debug:
            print("Measured Distance: {} cm".format(measured_distance))

        return measured_distance

