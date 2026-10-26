def time_string(hours,minutes,time_format):
    result = ''
    hours_str = str(hours)
    minutes_str = str(minutes)
    if len(minutes_str) < 2:
        minutes_str = '0' + minutes_str

    if time_format == '24':
        if len(hours_str) < 2:
            hours_str = '0' + hours_str

        result = hours_str + ':' + minutes_str

    elif time_format == '12':

        if hours == 0:
            result = '12:' + minutes_str + 'am'
        elif 1 <= hours <= 11:
            result = hours_str + ':' + minutes_str + 'am'
        elif hours == 12:
            result = hours_str + ':' + minutes_str + 'pm'
        elif 13 <= hours <= 23:
            hours_str = str(hours - 12)
            result = hours_str + ':' + minutes_str +'pm'
        

    return result
        
        

print(time_string(15,38,'24'))
print(time_string(8,3,'24'))
print(time_string(0,5,'24'))
print(time_string(11,15,'12'))
print(time_string(0,7,'12'))
print(time_string(7,30,'12'))
print(time_string(12,46,'12'))
print(time_string(13,10,'12'))
print(time_string(19,2,'12'))