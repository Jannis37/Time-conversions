def add_zeros(arg):
    val = str(arg)
    if len(val) == 1:
        val = f'0{val}'
    return val

def hour_to_minute(val):
    return float(val) * 60

def minute_to_hour(val):
    return float(val) / 60

def hour_to_second(val):
    return float(val) * 60 * 60

def second_to_hour(val):
    return float(val) / (60 * 60)

def minute_to_second(val):
    return float(val) * 60

def second_to_minute(val):
    return float(val) / 60

def min_to_HHMM(val):
    min = float(val)
    hours = add_zeros(int(min / 60))
    minutes = add_zeros(int(min % 60))
    return f'{hours}:{minutes}'

def sec_to_HHMM(val):
    secs = float(val)
    hours = add_zeros(int(secs / (60 * 60)))
    minutes = add_zeros(int((secs / 60) % 60))
    return f'{hours}:{minutes}'

def HHMM_to_min(val):
    hours, minutes = val.split(':')
    return hour_to_minute(hours) + float(minutes)

def HHMM_to_sec(val):
    hours, minutes = val.split(':')
    return hour_to_second(hours) + minute_to_second(minutes)
