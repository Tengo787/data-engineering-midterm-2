import pandas as pd


input_file = "data.csv"
output_file = "processed_data.csv"


df = pd.read_csv(input_file)


filtered_df = df[df["price"] > 50]


grouped_df = filtered_df.groupby("category")["price"].mean().reset_index()


grouped_df.to_csv(output_file, index=False)

print(f"დამუშავებული მონაცემები შენახულია: {output_file}")
