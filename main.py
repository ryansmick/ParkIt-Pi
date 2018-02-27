import RPi.GPIO as GPIO
import time

# Return distance in cm
def get_distance_measure(trig, echo, num_samples):
    total_distance = 0
    for i in range(num_samples):
        GPIO.setmode(GPIO.BCM)

        GPIO.setup(trig,GPIO.OUT)
        GPIO.setup(echo,GPIO.IN)

        GPIO.output(trig, True)
        time.sleep(0.00001)
        GPIO.output(trig, False)

        pulse_start = time.time()
        while GPIO.input(echo)==0:
            pulse_start = time.time()

        while GPIO.input(echo)==1:
            pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start

        distance = pulse_duration * 17150
        total_distance += distance

    return total_distance/num_samples

def update_space_status(status):
    pass

if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    
    TRIG = 23 
    ECHO = 24
    prev_status = None

    print("Distance Measurement In Progress")

    GPIO.setup(TRIG,GPIO.OUT)
    GPIO.setup(ECHO,GPIO.IN)

    GPIO.output(TRIG, False)
    print("Waiting For Sensor To Settle")
    time.sleep(2)

    while True:
        distance = get_distance_measure(TRIG, ECHO, 100)

        # If car in parking space, update the status of the space
        is_occupied = False
        if distance < 100:
            is_occupied = True

        if is_occupied != prev_status:
            update_space_status(is_occupied)
            prev_status = is_occupied

        GPIO.cleanup()

