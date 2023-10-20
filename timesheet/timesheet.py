import datetime as dt
import pyperclip

def main():
    offset = dt.timedelta(days=7) # to play around with time
    today = dt.datetime.today() 

    day_of_week = today.isocalendar()[2]
    date = today - dt.timedelta(days=day_of_week)

    staff_meetings = [dt.date(2023, 10, 4), dt.date(2023, 10, 18), dt.date(2023, 11, 1), dt.date(2023, 11, 15), dt.date(2023, 12, 6)]

    all_days = [((date + dt.timedelta(days=i)).date()) for i in range(7)]

    # Define the schedule using a dictionary
    schedule = {
        'Monday': [
            "10am - 11am, Prepare for Study Group",
            "3:50pm - 5:10pm, CS111 Study Group"
        ],
        'Wednesday': [
            "10am - 11am, Staff Meeting" if any(day in staff_meetings for day in all_days) else None,
            "11am - 12am, Prepare for Study Group",
            "12:10pm - 1:30pm, CS111 Study Group",
        ],
    }
    
    print("Hours with students: 3")
    print(f"Hours in staff meeting: {1 if any(day in staff_meetings for day in all_days) else 0}")
    print("Hours preparing: 2")

    with open('timesheet.txt', 'w') as f:
        for day in all_days:
            date_month_day = day.strftime("%A %-m/%-d")
            activities = schedule.get(day.strftime("%A"), [])
            for activity in activities:
                if activity:
                    f.write(f"{date_month_day}, {activity}\n")

    fo = open('timesheet.txt', 'r').read()
    pyperclip.copy(fo)

if __name__ == "__main__":
    main()
