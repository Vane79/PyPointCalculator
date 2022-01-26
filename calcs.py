from datetime import date, timedelta
from selenium_fetch_stats import selenium


class Pointer:
    def __init__(self, p_total):
        self.p_total = p_total
        self.money_now, self.tier, self.diff = calculate_money(self.p_total)
        self.worked_days, self.month_workdays = days_worked()
        self.average_daily = self.p_total // self.worked_days
        self.point_prediction = self.average_daily * self.month_workdays
        self.money_prediction, self.tier_prediction, self.diff_prediction = calculate_money(self.point_prediction)
        if self.money_prediction < self.money_now:
            self.money_prediction = self.money_now
        self.tier_diff_by_end_of_month = self.diff_prediction // self.month_workdays
        self.workdays_left = self.month_workdays - self.worked_days


def days_worked():
    """
    :return:   amount of weekdays up to today, including today.
    """
    if date.today().month != 12:
        end_of_month = date(date.today().year, (date.today().month + 1), 1)
        end_of_month += timedelta(days=-1)
    else:
        end_of_month = date(date.today().year, date.today().month, 31)
    day_counter = date(date.today().year, date.today().month, 1)
    worked_days, month_workdays = 0, 0
    while day_counter <= end_of_month:  # let's count weekdays in the current month
        if day_counter.weekday() not in (5, 6):
            month_workdays += 1
            day_counter += timedelta(days=1)
        else:
            day_counter += timedelta(days=1)
        if day_counter == date.today():
            worked_days = month_workdays + 1
        if worked_days == 0:
            worked_days = 1
    return worked_days, month_workdays


def calculate_money(p_total):
    if p_total <= 2500:
        money_now, tier = p_total * 10, 10
        difference_with_next_tier = 2500 - p_total
    elif 2501 <= p_total <= 3000:
        money_now, tier = p_total * 11, 11
        difference_with_next_tier = 3000 - p_total
    elif 3001 <= p_total <= 3500:
        money_now, tier = p_total * 12, 12
        difference_with_next_tier = 3500 - p_total
    elif 3501 <= p_total <= 4000:
        money_now, tier = p_total * 13, 13
        difference_with_next_tier = 4000 - p_total
    else:
        money_now, tier = p_total * 14, 14
        difference_with_next_tier = 0
    return money_now, tier, difference_with_next_tier


def output_data(points):
    try:
        calculated = Pointer(points)
        print(f"""
    You've processed {calculated.p_total} total points. That was approx. {calculated.average_daily} points per weekday.
    You already earned {calculated.money_now} roubles, that's {calculated.tier} roubles per point.
    So, by my humble estimates, you'll get {calculated.money_prediction} roubles by the end of the current month, {calculated.tier_prediction} roubles per point.
    You'd have to process {calculated.tier_diff_by_end_of_month} more points per weekday for the next tier.
    By the way, there's only a bit of time left. Only {calculated.workdays_left} days, to be exact.
        """)
    except ValueError:
        print(f"There was an error in your input somewhere.")


if __name__ == '__main__':
    photos = input("How many photos? ")
    videos = input("how many videos? ")
    # photos, videos = selenium()
    total = int(photos) + (int(videos) * 2)
    output_data(total)
    pass
