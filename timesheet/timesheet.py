import datetime as dt
import pyperclip


def main():
    offset = dt.timedelta(days=7)
    today = dt.datetime.today() + offset

    day_of_week = today.isocalendar()[2]
    date = today - dt.timedelta(days=day_of_week)

    staff_meetings = [dt.date(2022,11,17), dt.date(2022,12,1)]

    all_days = [((date + dt.timedelta(days=i)).date()) for i in range(7)]

    with open('timesheet.txt','w') as f:
        for day in all_days:
            date_month_day = day.strftime("%A %-m/%-d")
            match day.strftime("%A"):
                case 'Tuesday':
                    f.write(f"{date_month_day}, 6 pm - 7pm - Preparation for study group\n")
                case 'Wednesday':
                    f.write(f"{date_month_day}, 5:40 pm - 7 pm - CS 112 Study Group\n")
                case 'Thursday':
                    if day in staff_meetings:
                        f.write(f"{date_month_day}, 9 pm - 10 pm - Staff Meeting\n")
                    f.write(f"{date_month_day}, 5 pm - 6pm - Preparation for Friday Recitations\n")
                case 'Friday':
                    f.write(
                        f"{date_month_day}, 12:25 pm - 1:20 pm - Data Structure Recitation\n"
                        f"{date_month_day}, 4:05 pm - 5 pm - Data Structure Recitation\n"
                        f"{date_month_day}, 5:55 pm - 6:50 pm pm - Data Structure Recitation"
                    )
    fo = open('timesheet.txt', 'r').read()
    pyperclip.copy(fo)

if __name__ == "__main__":
    main()
