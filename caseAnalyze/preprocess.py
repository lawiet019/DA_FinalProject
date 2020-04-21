import pandas as pd
csv_data = pd.read_csv("./data/DXYRumors.csv")
rumors_list = csv_data["title"]
