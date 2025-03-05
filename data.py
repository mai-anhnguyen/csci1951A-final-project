import pandas as pd

appData= pd.read_csv("BusinessApps.csv")
realData = pd.read_csv("RealInterestRate.csv")
insuranceData = pd.read_csv("UnemployInsurance.csv")
unemployData = pd.read_csv("UnemployRate.csv")

merged = appData.merge(
    realData, on="observation_date").merge(
    insuranceData, on="observation_date").merge(
    unemployData, on="observation_date")

merged.columns = ["month", "business apps", "real interest rate (%)", "unemp. ins. ($ bil)", "unemp. rate (%)"]

merged.to_csv("merged_file.csv", index=False)

print(merged[1:])