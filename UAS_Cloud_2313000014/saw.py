import pandas as pd

def hitung_saw(df):

    benefit = ["ram", "ssd", "processor", "merek"]
    cost = ["harga"]

    normalisasi = df.copy()

    for col in benefit:
        normalisasi[col] = normalisasi[col] / normalisasi[col].max()

    for col in cost:
        normalisasi[col] = normalisasi[col].min() / normalisasi[col]

    bobot = {
        "harga": 0.30,
        "ram": 0.25,
        "ssd": 0.20,
        "processor": 0.15,
        "merek": 0.10
    }

    normalisasi["nilai"] = (
        normalisasi["harga"] * bobot["harga"] +
        normalisasi["ram"] * bobot["ram"] +
        normalisasi["ssd"] * bobot["ssd"] +
        normalisasi["processor"] * bobot["processor"] +
        normalisasi["merek"] * bobot["merek"]
    )

    ranking = normalisasi.sort_values(
        by="nilai",
        ascending=False
    )

    return ranking