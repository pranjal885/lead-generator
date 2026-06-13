import pandas as pd

df = pd.read_csv("output/leads.csv")

print("\n===== JOB LEAD ANALYSIS =====\n")

print(f"Total Jobs Found: {len(df)}")

print("\nTop 10 Hiring Companies:")
print(df["Company"].value_counts().head(10))

print("\nTop 10 Locations:")
print(df["Location"].value_counts().head(10))

python_jobs = df[
    df["Job Title"].str.contains(
        "Python",
        case=False,
        na=False
    )
]

print(f"\nPython Related Jobs: {len(python_jobs)}")

df["Priority Score"] = df["Job Title"].apply(
    lambda x: 10 if "Python" in str(x) else 5
)

top_jobs = df.sort_values(
    "Priority Score",
    ascending=False
)

print("\nTop Recommended Jobs:")
print(
    top_jobs[
        ["Job Title", "Company", "Priority Score"]
    ].head(10)
)

recommended_jobs = df[
    df["Job Title"].str.contains(
        "Python|Developer|Engineer|Data",
        case=False,
        na=False
    )
]

recommended_jobs.to_csv(
    "output/recommended_jobs.csv",
    index=False
)

print(
    f"\nRecommended Jobs Saved: {len(recommended_jobs)}"
)

with open("output/summary_report.txt", "w") as file:

    file.write("JOB LEAD ANALYSIS REPORT\n")
    file.write("========================\n\n")

    file.write(f"Total Jobs Found: {len(df)}\n")
    file.write(f"Python Related Jobs: {len(python_jobs)}\n")
    file.write(
        f"Recommended Jobs: {len(recommended_jobs)}\n"
    )

print("\nSummary report generated.")