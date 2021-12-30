def to_seconds_conversor(time_unit, time):
    if time_unit == 1:
        return time
    elif time_unit == 2:
        time *= 60
    else:
        time *= 3600
    return time
