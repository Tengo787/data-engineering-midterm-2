import pandas as pd


df1 = pd.read_csv("data.csv")
df2 = pd.read_csv("data2.csv")


df1_filtered = df1[df1["value"] > 50]
df1_grouped = df1_filtered.groupby("category").agg({"value": "sum"}).reset_index()


df2["transformed_value"] = df2["amount"] * 1.2
df2_result = df2[["name", "transformed_value"]]


df1_grouped.to_csv("output.csv", index=False)
df2_result.to_csv("output2.csv", index=False)

print("Processing complete. Output saved to output.csv and output2.csv.")
