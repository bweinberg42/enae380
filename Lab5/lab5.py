import time
import easygopigo3 as easy


pig = easy.EasyGoPiGo3()
d_sensor = pig.init_distance_sensor()


def apply_phys_limit(d):
    """ 
    Moves the PiGo forward until the IR distance sensor detects an obstacle 
    within the distance (mm) specified.

    Parameters
    __________
    d : float
        the distance measured by our sensor


    Returns     
    -------
    float
        the last read distance of the obstacle

    """

    dist = d_sensor.read_mm()

    while (dist > d):
        pig.forward()
        dist = d_sensor.read_mm()

    pig.stop()
    return(dist)




def apply_time_limit(dt, speed):
    """ 
    Moves the PiGo forward for a specified time (sec) and motor-speed (dps).
    
    Parameters
    __________
    dt : float
        the duration (s) for which to move forward

    speed : int
        the speed (dps) at which to move forward
        
    """

    pig.set_speed(speed)

    pig.forward()

    time.sleep(dt)

    pig.stop()

    pass


