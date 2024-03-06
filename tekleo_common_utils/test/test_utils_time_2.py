from tekleo_common_utils.utils_time import UtilsTime

utils_time = UtilsTime()


class TestUtilsTime2:
    def test_1(self):
        print(utils_time.parse_timestamp_ms("20.01.2024 00:00:01 (+0000)"))

    def test_parse_timestamp_ms_rfc3339(self):
        d1 = "2006-06-15T00:00:00"
        d2 = "2006-08-23T12:15:23-07:00"
        d3 = "2022-12-23T09:33:35.97+00:00"
        d4 = "2022-09-20T15:44:10.893+00:00"
        d5 = "2022-09-20T15:44:10.893123+00:00"
        d6 = "2018-04-23T13:37:12.723Z"
        d7 = "2018-04-23T13:37:12.71"
        print(utils_time.parse_timestamp_ms_rfc3339(d1))
        print(utils_time.parse_timestamp_ms_rfc3339(d2))
        print(utils_time.parse_timestamp_ms_rfc3339(d3))
        print(utils_time.parse_timestamp_ms_rfc3339(d4))
        print(utils_time.parse_timestamp_ms_rfc3339(d5))
        print(utils_time.parse_timestamp_ms_rfc3339(d6))
        print(utils_time.parse_timestamp_ms_rfc3339(d7))

    def test_format_timestamp_ms_rfc3339(self):
        print(utils_time.format_timestamp_ms_rfc3339(1524479832000))
        print(utils_time.format_timestamp_ms_rfc3339(1524479832000, utils_time.get_timezone_pst()))
