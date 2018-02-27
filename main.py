from sensor import DistanceSensor
from database_operations import Parse
import databaseconfig

if __name__ == '__main__':
    TRIG = 23
    ECHO = 24
    prev_status = None
    DEBUG = True

    sensor = DistanceSensor(TRIG, ECHO, DEBUG)
    database = Parse(databaseconfig.APPLICATION_ID, databaseconfig.REST_API_KEY, databaseconfig.PARSE_SERVER)

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
            database.update("parking_space", databaseconfig.object_id, {"is_occupied": is_occupied})
            prev_status = is_occupied
