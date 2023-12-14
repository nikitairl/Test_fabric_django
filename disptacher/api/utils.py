from datetime import datetime

import pytz

from disptacher.settings import TIME_ZONE


APP_TIMEZONE = pytz.timezone(TIME_ZONE)


def delta_calc(date, client_timezone):
    """
    Function to calculate time difference between two timezones
    """
    input_datetime = datetime.fromisoformat(str(date))
    client_timezone = pytz.timezone(client_timezone)

    now = datetime.now()
    client_timezone = client_timezone.localize(now)
    app_time = APP_TIMEZONE.localize(now)
    time_diff = app_time - client_timezone
    input_datetime = input_datetime + time_diff
    return input_datetime
