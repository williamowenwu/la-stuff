import pandas as pd
import datetime as dt
from all_names import all_names,sections
from constants import old_attendance_sheet_id, sheet_id, answers

ans = input("Did you teach an additional section?\n")
ans = ans.title()

open("absent.txt", "w").close()

def create_dataframe():
    df = pd.read_csv(f'https://docs.google.com/spreadsheets/d/{old_attendance_sheet_id}/export?format=csv')

    df['Timestamp'] = pd.to_datetime(df['Timestamp'], format="%m/%d/%Y %H:%M:%S")

    df['First Name'] = df['First Name'].str.title()
    df['Last Name'] = df['Last Name'].str.title()

    df['First Name'] = df['First Name'].str.strip()
    df['Last Name'] = df['Last Name'].str.strip()
    return df

def get_this_weeks_friday():
    # offset if you want to grab previous weeks
    offset = dt.timedelta(days=21)
    today = dt.datetime.today()
    this_weeks_friday = today

    match today.isoweekday():
        case x if x < 5:
            diff_in_days = 5 - x
            this_weeks_friday = today + dt.timedelta(days=diff_in_days)
        case y if y > 5:
            diff_in_days = y - 5
            this_weeks_friday = today - dt.timedelta(days=diff_in_days)
    return this_weeks_friday


def main():
    df = create_dataframe()
    this_weeks_friday = get_this_weeks_friday()
    filt = df['Timestamp'].dt.date == this_weeks_friday.date()
    all_students_present = df.loc[filt, ["First Name", "Last Name", "Section Number"]]
    with open('absent.txt', 'a') as f:
        f.write(f"This week's friday: {this_weeks_friday.date()} \n \n")

    with open('absent.txt', 'a') as f:
        
        students_present = {}
        for section,sec_str in sections.items():
            if section == 3:
                if ans not in answers:
                    print("Just asking")
                    continue
            filter_ = df["Section Number"] == sec_str
            students_present[section] = all_students_present.loc[filter_, ["First Name", "Last Name"]]
            joined = all_names[section].merge(students_present[section],indicator=True,how='outer')
            diff = joined.loc[lambda x: x['_merge'] != 'both']
            with open('absent.txt', 'a') as f:
                f.write(f"SECTION: {section}\n\n")
                f.write(f"{str(diff)}\n\n")

if __name__ == "__main__":
    main()
