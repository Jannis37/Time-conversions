# Tests
from time_conversions import hour_to_minute, min_to_HHMM, minute_to_hour, minute_to_second, second_to_minute, second_to_hour, hour_to_second, sec_to_HHMM

def print_separation():
    print('')
    print('---------------------------------------')
    print('')

tests = True
if tests:
    print('Hour to minute:')
    print(f'1h: {hour_to_minute(1)} minutes')
    print(f'1.5h: {hour_to_minute(1.5)} minutes')
    print(f'(As string) 1.5h: {hour_to_minute("1.5")} minutes')

    print_separation()

    print('Minute to hour:')
    print(f'60 min: {minute_to_hour(60)} hours')
    print(f'90 min: {minute_to_hour(90)} hours')
    print(f'(As string) 90 min: {minute_to_hour("90")}')

    print_separation()

    print('Hour to second:')
    print(f'1h: {hour_to_second(1)} seconds')
    print(f'1.5h: {hour_to_second(1.5)} seconds')
    print(f'(As string) 1.5h: {hour_to_second("1.5")} seconds')

    print_separation()

    print('Second to hour:')
    print(f'60s: {second_to_hour(60)} hours')
    print(f'90s: {second_to_hour(90)} hours')
    print(f'(As string) 90s: {second_to_hour("90")} hours')

    print_separation()

    print('Minute to second:')
    print(f'1 min: {minute_to_second(1)} seconds')
    print(f'1.5 min: {minute_to_second(1.5)} seconds')
    print(f'(As string) 1.5 min: {minute_to_second("1.5")} seconds')

    print_separation()

    print('Second to minute:')
    print(f'60s: {second_to_minute(60)} minutes')
    print(f'90s: {second_to_minute(90)} minutes')
    print(f'(As string) 90s: {second_to_minute("90")} minutes')

    print_separation()

    print('Minute to HH:MM')
    print(f'60 min: {min_to_HHMM(60)}')
    print(f'90 min: {min_to_HHMM(90)}')
    print(f'(As string) 90 min: {min_to_HHMM("90")}')

    print_separation()

    print('Seconds to HH:MM')
    print(f'60 min: {sec_to_HHMM(minute_to_second(60))}')
    print(f'90 min: {sec_to_HHMM(minute_to_second(90))}')
    print(f'(As string) 90 min: {sec_to_HHMM(minute_to_second("90"))}')