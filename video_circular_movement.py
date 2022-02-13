from robomaster import robot
import time
from robomaster import camera

if __name__ == '__main__':

    ep_robot = robot.Robot()
    ep_robot.initialize(conn_type="ap")

    ep_chassis = ep_robot.chassis

    '''
    x = speed in x direction( meter/second) [-3.5,3.5]
    y = speed in y direction( meter/second) [-3.5,3.5]
    z = rotation about z axis ( degree/second)[-600,600]
    '''
    ep_camera = ep_robot.camera

    print("Camera streaming started...")
    ep_camera.start_video_stream(display=True, resolution=camera.STREAM_360P)    
    
    ep_chassis.drive_speed(x=0.4,y=0,z=20)
    time.sleep(15)
    ep_chassis.drive_speed(x=0,y=0,z=0)
    
    ep_camera.stop_video_stream()
    print("Stopped video streaming...")
    
    ep_robot.close()