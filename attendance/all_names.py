import pandas as pd
from constants import all_names_sheet_id

df = pd.read_csv(f'https://docs.google.com/spreadsheets/d/{all_names_sheet_id}/export?format=csv')

sect_1_str = "Section 1 (12:25pm - 1:20pm)"
sect_5_str = "Section 5 (4:05 pm- 5pm)"
sect_16_str = "Section 16 (5:55pm - 6:50pm)"
sect_3_str = "Section 3 (12:25pm - 1:20pm)"

df['First Name'] = df['First Name'].str.title()
df['Last Name'] = df['Last Name'].str.title()

sections = {
    1: sect_1_str,
    3: sect_3_str,
    5: sect_5_str,
    16: sect_16_str
}

all_names = {}
for section,sec_str in sections.items():
    sec_filter = df["Section Number"] == sec_str
    all_names[section] = df.loc[sec_filter, ["First Name", "Last Name"]]


def main():
    print(all_names[16])

if __name__ == "__main__":
    main()