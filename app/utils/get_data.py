from datetime import date, timedelta
import holidays


def is_weekend(date_to_check):
    # Verifica se é sábado (5) ou domingo (6)
    return date_to_check.weekday() in [5, 6]


def is_holiday(date_to_check):
    # Verifica se é feriado
    br_holidays = holidays.Brazil()

    return date_to_check in br_holidays


def get_date_yesterday():
    # Busca a data do dia anterior
    date_now = date.today()

    for date_to_subtract in range(2, 7):
        date_yesterday = date_now - timedelta(days=date_to_subtract)

        if not is_holiday(date_yesterday) and not is_weekend(date_yesterday):
            date_yesterday_formatted = date_yesterday.strftime("%d/%m/%Y")
            return date_yesterday_formatted

    return None
