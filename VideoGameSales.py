import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


print("hello world")

df=pd.read_csv("VideoGamesSales.csv")

# print(df.shape) #The orginal shape and data
# print(df[df.duplicated()]) #This shows the duplicated rows
# df = df.drop_duplicates() #This drops the duplicated rows
# print(df.shape) #Shows the new shape.

# df.info()
df["Region"]=df["Region"].fillna("North")
print("\n\n")
# df.info()


# for i, value in enumerate(df["NA_Sales"]):
#     if "$" in value:
#         print(type(value))
#         print(df["NA_Sales"][i])
#         # i = i[1:]

df["NA_Sales"] = df["NA_Sales"].replace("[$]", " ", regex=True)

df["NA_Sales"] = pd.to_numeric(df["NA_Sales"], errors="coerce")
# print(df.head(5))
Average_Sales = df["NA_Sales"].mean()

# print(f"{Average_Sales:.2f}")
# print(df.columns)

df["Country"] = df["Country"].replace({"[USA]" : "United States"})