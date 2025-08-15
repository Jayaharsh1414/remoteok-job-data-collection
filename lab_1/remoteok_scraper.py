import requests
import pandas as pd

url = "https://remoteok.com/api"

response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
data = response.json()


jobs = data[1:]

job_list = []
for job in jobs:
    job_list.append({
        "Company Name": job.get("company"),
        "Job Role": job.get("position"),
        "Location": job.get("location"),
        "Features/Tags": ", ".join(job.get("tags", []))
    })


df = pd.DataFrame(job_list)

df.to_csv("remoteok_jobs.csv", index=False)
print(f"Saved {len(df)} job listings to remoteok_jobs.csv")
