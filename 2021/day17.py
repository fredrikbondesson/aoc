"""
    The probe's x,y position starts at 0,0. 
    Then, it will follow some trajectory by moving in steps. 
    On each step, these changes occur in the following order:
    
    The probe's x position increases by its x velocity.
    The probe's y position increases by its y velocity.
    Due to drag, the probe's x velocity changes by 1 toward the value 0; 
    that is, it decreases by 1 if it is greater than 0, 
    increases by 1 if it is less than 0, 
    or does not change if it is already 0.
    Due to gravity, the probe's y velocity decreases by 1.
"""    

def get_max(x_pos, y_pos, x_velocity, y_velocity, target_x1, target_x2, target_y1, target_y2):
    max_y = -100
    while x_pos <= target_x2 and y_pos >= target_y2:
        if y_pos > max_y:
                max_y = y_pos
        x_pos, y_pos, x_velocity, y_velocity = calc_pos_and_velocity(x_pos, y_pos, x_velocity, y_velocity)        
        if x_pos >= target_x1 and x_pos <= target_x2 and y_pos <= target_y1 and y_pos >= target_y2:
            return max_y

    return -100


def calc_pos_and_velocity(x, y, x_velocity, y_velocity):
    x_pos = x + x_velocity
    y_pos = y + y_velocity
    if x_velocity == 0:
        x_velocity = 0
    elif x_velocity > 0:
        x_velocity -= 1
    else:
        x_velocity += 1
    
    y_velocity -= 1
    return x_pos, y_pos, x_velocity, y_velocity


def main():
    # Example data
    # target area: x=20..30, y=-10..-5
    target_x1 = 20
    target_x2 = 30
    target_y1 = -5
    target_y2 = -10
    x_pos = 0
    y_pos = 0

    x_vel = 6
    y_vel = 3
    max_y = get_max(x_pos, y_pos, x_vel, y_vel, target_x1, target_x2, target_y1, target_y2)
    assert max_y == 6, f'Expected 6, got {max_y}'

    x_vel = 6
    y_vel = 9
    max_y = get_max(x_pos, y_pos, x_vel, y_vel, target_x1, target_x2, target_y1, target_y2)
    assert max_y == 45, f'Expected 45, got {max_y}'

    # 17,-4 # Never reach target zone
    x_vel = 17
    y_vel = -4
    max_y = get_max(x_pos, y_pos, x_vel, y_vel, target_x1, target_x2, target_y1, target_y2)
    assert max_y == -100, f'Expected -100, got {max_y}'

    max_ys = []
    max_set = set()
    for x in range(0, 1000):
        for y in range(-100, 100):
            x_vel = x
            y_vel = y
            max_y = get_max(x_pos, y_pos, x_vel, y_vel, target_x1, target_x2, target_y1, target_y2)
            if max_y != -100:
                max_ys.append(max_y)
                max_set.add((x_vel, y_vel))

    # print(max_ys)
    print(max(max_ys))
    assert max(max_ys) == 45, f'Expected 45, got {max(max_ys)}'
    # print(max_set)
    print(len(max_set))
    assert len(max_set) == 112, f'Expected 112, got {len(max_set)}'    

    # target area: x=155..215, y=-132..-72
    print('INPUT DATA: target area: x=155..215, y=-132..-72')
    
    target_x1 = 155
    target_x2 = 215
    target_y1 = -72
    target_y2 = -132
    x_pos = 0
    y_pos = 0

    max_ys = []
    max_set = set()
    for x in range(0, 1000):
        for y in range(-500, 500):
            x_vel = x
            y_vel = y
            max_y = get_max(x_pos, y_pos, x_vel, y_vel, target_x1, target_x2, target_y1, target_y2)
            if max_y != -100:
                max_ys.append(max_y)
                max_set.add((x_vel, y_vel))

    # print(max_ys)
    print(max(max_ys))
    assert max(max_ys) == 8646, f'Expected 8646, got {max(max_ys)}'
    print(len(max_set))
    assert len(max_set) == 5945, f'Expected 5945, got {len(max_set)}'


if __name__ == '__main__':
    main()