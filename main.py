from sensor import DistanceSensor

if __name__ == '__main__':
    TRIG = 23 
    ECHO = 24
    prev_status = None
    DEBUG = True

    sensor = DistanceSensor(TRIG, ECHO, DEBUG)

    while True:
        distance = sensor.read_distance(100)

        # If car in parking space, update the status of the space
        is_occupied = False
        if distance < 100:
            is_occupied = True

        if is_occupied != prev_status:
            if DEBUG:
                if is_occupied:
                    print("Space is OCCUPIED")
                else:
                    print("Space is NOT OCCUPIED")
            prev_status = is_occupied

