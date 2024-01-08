import holidays
from datetime import date, timedelta


def is_weekend(date_to_check):
    # Check if it is Saturday (5) or Sunday (6)
    return date_to_check.weekday() in [5, 6]


def is_holiday(date_to_check):
    # Check if it is a holiday
    br_holidays = holidays.Brazil()

    return date_to_check in br_holidays


def get_date_yesterday():
    # Search the date of the previous day
    date_now = date.today()

    for date_to_subtract in range(2, 7):
        date_yesterday = date_now - timedelta(days=date_to_subtract)

        if not is_holiday(date_yesterday) and not is_weekend(date_yesterday):
            date_yesterday_formatted = date_yesterday.strftime("%d/%m/%Y")
            return date_yesterday_formatted

    return None
