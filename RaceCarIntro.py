def update():
    global counter
    if is_down(A):
        rc.drive.set_speed_angle(0.5, counter)
    elif is_down(B):
        if counter % 60 == 1:
            rc.drive.set_speed_angle(0.5, -1)
        else:
            rc.drive.set_speed_angle(0.5, 0)
    elif is_down(X):
        if counter % 180 == 60:
            rc.drive.set_speed_angle(0.5, -4/3)
        elif counter % 180 == 90:
            rc.drive.set_speed_angle(0.5, -4/3)
        elif counter %180 == 150:
            rc.drive.set_speed_angle(0.5, -4/3)
        elif counter % 180 == 0:
            rc.drive.set_speed_angle(0.5, -4/3)
        else:
            rc.drive.set_speed_angle(0.5, 0)
    elif is_down(Y):
        if counter % 120 < 60:
            rc.drive.set_speed_angle(1, 0)
        else:
            rc.drive.set_speed_angle(-1, 0)
    else:
        rc.drive.stop()
    counter += rc.get_delta_time()   
