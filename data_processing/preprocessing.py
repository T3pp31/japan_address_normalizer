import datetime as dt

import pandas as pd

data = pd.read_csv("./data_processing/data/KEN_ALL.CSV", encoding="shift-jis")

data.drop(
    columns=[
        "CD1",
        "CD2",
        "都道府県カタカナ",
        "市区町村カタカナ",
        "字カタカナ",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
    ],
    inplace=True,
)
data["zip_code"] = data["zip_code"].apply(lambda x: str(x).zfill(7))

now = dt.datetime.now()
year = now.year
month = now.month
date = now.day


data.to_csv(
    f"data/preprocessed_{year}-{month}-{date}.csv",
    index=False,
    encoding="shift-jis",
)
