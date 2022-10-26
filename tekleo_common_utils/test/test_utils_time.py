from tekleo_common_utils.utils_time import UtilsTime

utils_time = UtilsTime()

print('Testing current time at different zones:')
current = utils_time.get_timestamp_ms_now()
print('Current timestamp:      ', current)
print('Current time at local:  ', utils_time.format_timestamp_ms(current, timezone=utils_time.get_timezone_local()))
print('Current time at UTC:    ', utils_time.format_timestamp_ms(current, timezone=utils_time.get_timezone_utc()))
print('Current time at PST:    ', utils_time.format_timestamp_ms(current, timezone=utils_time.get_timezone_pst()))
print('--------------------------------------------------------------------------------------------\n')

print('Testing time parsing')
current_str_utc = utils_time.format_timestamp_ms(current, timezone=utils_time.get_timezone_utc())
print('String at UTC:', current_str_utc)
current_1 = utils_time.parse_timestamp_ms(current_str_utc)
print('Timezone parsed at UTC:', current_1)
print('String restored at UTC:', utils_time.format_timestamp_ms(current_1, timezone=utils_time.get_timezone_utc()))
current_2 = utils_time.parse_timestamp_ms(current_str_utc)
print('Timezone parsed at local:', current_2)
print('String restored at local:',utils_time.format_timestamp_ms(current_2, timezone=utils_time.get_timezone_local()))
print('--------------------------------------------------------------------------------------------\n')


print('Testing day start/end')
day_start = utils_time.get_day_start_timestamp_ms(2022, 1, 1, timezone=utils_time.get_timezone_local())
print('Day start:', utils_time.format_timestamp_ms(day_start, timezone=utils_time.get_timezone_local()))
day_end = utils_time.get_day_end_timestamp_ms(2022, 1, 1, timezone=utils_time.get_timezone_local())
print('Day end:', utils_time.format_timestamp_ms(day_end, timezone=utils_time.get_timezone_local()))
day_start_2, day_end_2 = utils_time.get_day_start_end_timestamps_ms(2022, 1, 1, timezone=utils_time.get_timezone_local())
print('Day start 2:', utils_time.format_timestamp_ms(day_start_2, timezone=utils_time.get_timezone_local()))
print('Day end 2:', utils_time.format_timestamp_ms(day_end_2, timezone=utils_time.get_timezone_local()))
print('--------------------------------------------------------------------------------------------\n')

print('Testing month start/end')
month_start = utils_time.get_month_start_timestamp_ms(2022, 1, timezone=utils_time.get_timezone_local())
print('Month start:', utils_time.format_timestamp_ms(month_start, timezone=utils_time.get_timezone_local()))
month_end = utils_time.get_month_end_timestamp_ms(2022, 1, timezone=utils_time.get_timezone_local())
print('Month end:', utils_time.format_timestamp_ms(month_end, timezone=utils_time.get_timezone_local()))
month_start_2, month_end_2 = utils_time.get_month_start_end_timestamps_ms(2022, 1, timezone=utils_time.get_timezone_local())
print('Month start 2:', utils_time.format_timestamp_ms(month_start_2, timezone=utils_time.get_timezone_local()))
print('Month end 2:', utils_time.format_timestamp_ms(month_end_2, timezone=utils_time.get_timezone_local()))
print('--------------------------------------------------------------------------------------------\n')

print('Testing day start/end')
day_start_local, day_end_local = utils_time.get_day_start_end_timestamps_ms(2022, 10, 5, timezone=utils_time.get_timezone_local())
print("Day start/end (local)  :  ", day_start_local, "/", day_end_local)
day_start_utc, day_end_utc = utils_time.get_day_start_end_timestamps_ms(2022, 10, 5, timezone=utils_time.get_timezone_utc())
print("Day start/end (UTC)    :  ", day_start_utc, "/", day_end_utc)
assert day_start_local != day_start_utc
assert day_end_local != day_end_utc
print('--------------------------------------------------------------------------------------------\n')