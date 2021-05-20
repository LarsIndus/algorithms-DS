# Get the angle between the hands of a clock.
# Function accepts times in both 12 and 24 hours format.

def get_angle(hours, minutes):
    ANGLE_PER_MINUTE = 360 / 60
    ANGLE_PER_HOUR = 360 / 12
    
    # convert to 12 hour format
    hours %= 12
    
    angle_minutes = ANGLE_PER_MINUTE * minutes
    angle_hours = ANGLE_PER_HOUR * (hours + minutes / 60)
    
    angle_diff = abs(angle_minutes - angle_hours)
    
    # always return the smaller possible angle
    if (angle_diff > 180):
        return 360 - angle_diff
    
    return angle_diff

# Testing --------------------------------------------------------------------
def main():
    hours = 15
    minutes = 15
    print(get_angle(hours, minutes))

if __name__ == '__main__':
    main()