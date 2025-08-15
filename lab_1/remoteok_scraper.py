import requests
import pandas as pd

# RemoteOK public API endpoint
url = "https://remoteok.com/api"

# Send GET request
response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
data = response.json()

# The first element is metadata, skip it
jobs = data[1:]

# Extract required fields
job_list = []
for job in jobs:
    job_list.append({
        "Company Name": job.get("company"),
        "Job Role": job.get("position"),
        "Location": job.get("location"),
        "Features/Tags": ", ".join(job.get("tags", []))
    })

# Convert to DataFrame
df = pd.DataFrame(job_list)

# Save to CSV
df.to_csv("remoteok_jobs.csv", index=False)
print(f"Saved {len(df)} job listings to remoteok_jobs.csv")
