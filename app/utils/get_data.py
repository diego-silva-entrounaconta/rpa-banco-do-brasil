from datetime import date, timedelta


def get_date_yesterday():
    date_now = date.today()
    date_yesterday = date_now - timedelta(days=1)
    date_yesterday_formatted = date_yesterday.strftime("%d/%m/%Y")

    return date_yesterday_formatted
