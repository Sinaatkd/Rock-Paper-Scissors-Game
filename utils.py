import numpy as np

def calculate_angle(first_point, mid_point, end_point):
    """calculate angle of between two points

    Args:
        first_point (array[x,y]): first point x, y
        mid_point (array[x,y]): mid point x, y
        end_point (array[x,y]): end point x, y

    Returns:
        int: calculated angle
    """
    first_point = np.array(first_point)
    mid_point = np.array(mid_point)
    end_point = np.array(end_point)

    radians = np.arctan2(end_point[1]-mid_point[1],
                         end_point[0]-mid_point[0]) - np.arctan2(first_point[1]-mid_point[1],
                                                                 first_point[0]-mid_point[0])
    angle = np.abs(radians*180.0/np.pi)

    if angle >180.0:
        angle = 360-angle
    return angle