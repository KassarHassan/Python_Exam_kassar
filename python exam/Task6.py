# task6
import wbdata
import pandas as pd
import datetime

# 1
country_code = "SUR"                         # Suriname
indicator    = {"SP.POP.TOTL": "population"}  # total population

# 2
df = wbdata.get_dataframe(
    indicator,
    country=country_code
)

# 3
df.index = pd.to_datetime(df.index, format="%Y")

# 4) Filter the DataFrame between Jan 1 2010 and Dec 31 2020
start = datetime.datetime(2010, 1, 1)
end   = datetime.datetime(2020, 12, 31)
df    = df.loc[(df.index >= start) & (df.index <= end)]

# 5
df = df.reset_index().rename(columns={"index": "date"})

for _, row in df.iterrows():
    year = row["date"].year
    pop  = int(row["population"])
    print(f"Suriname, {year}: {pop:,}")
