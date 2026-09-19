"""Laboratory."""

import glob
import os

import pandas as pd  # type: ignore

files = glob.glob("files/input/*.csv.zip")
marketing = pd.concat(
    [pd.read_csv(file, compression="zip") for file in files],
    ignore_index=True,
)

# Split into the three tables
client = marketing[
    [
        "client_id",
        "age",
        "job",
        "marital",
        "education",
        "credit_default",
        "mortgage",
    ]
]
campaign = marketing[
    [
        "client_id",
        "number_contacts",
        "month",
        "day",
        "contact_duration",
        "previous_campaign_contacts",
        "previous_outcome",
        "campaign_outcome",
    ]
]
economics = marketing[["client_id", "cons_price_idx", "euribor_three_months"]]

# Editing the client dataset
# Clean education column
client.loc[:, "education"] = client["education"].str.replace(".", "_")
client.loc[:, "education"] = client["education"].replace("unknown", pd.NA)

# Clean job column
client.loc[:, "job"] = client["job"].str.replace(".", "")
client.loc[:, "job"] = client["job"].str.replace("-", "_")

# Clean and convert client columns to bool data type
for col in ["credit_default", "mortgage"]:
    client.loc[:, col] = client[col].map(
        {
            "yes": 1,
            "no": 0,
            "unknown": 0,
        }
    )
    client.loc[:, col] = client[col].astype(int)

# Editing the campaign dataset
# Change campaign_outcome to binary values
campaign.loc[:, "campaign_outcome"] = (
    campaign["campaign_outcome"]
    .map(
        {
            "yes": 1,
            "no": 0,
        }
    )
    .astype(int)
)

# Convert previous_outcome to binary values
campaign.loc[:, "previous_outcome"] = campaign["previous_outcome"].map(
    {"success": 1, "failure": 0, "nonexistent": 0}
)

# Add year column
campaign = campaign.assign(year="2022")

# Convert day to string
campaign["day"] = campaign["day"].astype(str)

# Add last_contact_date column
campaign["last_contact_date"] = (
    campaign["year"] + "-" + campaign["month"] + "-" + campaign["day"]
)

# Convert to datetime
campaign["last_contact_date"] = pd.to_datetime(
    campaign["last_contact_date"], format="%Y-%b-%d"
)
# Drop unneccessary columns
campaign.drop(columns=["month", "day", "year"], inplace=True)

# delete the files and the directory if it exists
if os.path.exists("files/output"):
    for file in os.listdir("files/output"):
        os.remove(os.path.join("files/output", file))
    os.rmdir("files/output")
os.mkdir("files/output")


# Save tables to individual csv files
client.to_csv("files/output/client.csv", index=False)
campaign.to_csv("files/output/campaign.csv", index=False)
economics.to_csv("files/output/economics.csv", index=False)

print(campaign.head(20))
