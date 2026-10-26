import converters

print('### Test converters')
print(f'Three meters is {converters.m_to_cm(3)}cm')
print(f'2m = {converters.m_to_cm(2)}cm')
print(f'532cm = {converters.cm_to_m(532)}m')
print(f'532cm = {converters.cm_to_inch(532)}inch')
print(f'6ft 9 inch = {converters.ft_in_to_cm(6,9)}cm')


