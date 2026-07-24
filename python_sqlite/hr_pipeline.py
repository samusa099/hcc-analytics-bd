#!/usr/bin/env python3
"""
Bangladesh HR Compensation & Compliance Analytics
CSV cleaning + validation + SQLite loader.

Important:
- Demo decision-support project, not legal advice.
- Update the configured sector wage floor and tax logic before operational use.
"""
from pathlib import Path
import sqlite3
import pandas as pd

BASE = Path(__file__).resolve().parents[1]
DATA = BASE / "data"
DB = Path(__file__).resolve().parent / "hr_analytics.sqlite"
CLEAN = Path(__file__).resolve().parent / "cleaned"
CLEAN.mkdir(exist_ok=True)

FILES = {
    "employees": "employees.csv",
    "payroll_monthly": "payroll_monthly.csv",
    "attendance_leave_monthly": "attendance_leave_monthly.csv",
    "benefits_enrollment": "benefits_enrollment.csv",
    "leave_entitlement": "leave_entitlement.csv",
    "compliance_register": "compliance_register.csv",
    "law_reference": "law_reference.csv",
    "data_dictionary": "data_dictionary.csv",
}

DATE_FIELDS = {
    "employees": ["Join_Date", "Date_of_Birth", "Exit_Date"],
    "payroll_monthly": ["Payroll_Month", "Due_Date", "Pay_Date"],
    "attendance_leave_monthly": ["Month"],
    "compliance_register": ["Month", "Action_Due_Date"],
}

def clean_text(series):
    return series.astype("string").str.strip().replace({"": pd.NA, "nan": pd.NA})

def load_and_clean(table, filename):
    df = pd.read_csv(DATA / filename)
    df.columns = [c.strip().replace(" ", "_") for c in df.columns]
    for col in df.select_dtypes(include="object").columns:
        df[col] = clean_text(df[col])
    for col in DATE_FIELDS.get(table, []):
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors="coerce").dt.date
    df = df.drop_duplicates()
    return df

def validate(frames):
    issues = []
    emp = frames["employees"]
    pay = frames["payroll_monthly"]
    att = frames["attendance_leave_monthly"]

    if emp["Employee_ID"].duplicated().any():
        issues.append("Duplicate Employee_ID found.")
    missing_emp = set(pay["Employee_ID"].dropna()) - set(emp["Employee_ID"].dropna())
    if missing_emp:
        issues.append(f"Payroll has {len(missing_emp)} unknown Employee_ID values.")
    missing_att = set(att["Employee_ID"].dropna()) - set(emp["Employee_ID"].dropna())
    if missing_att:
        issues.append(f"Attendance has {len(missing_att)} unknown Employee_ID values.")
    if "Gross_Pay" in pay and (pd.to_numeric(pay["Gross_Pay"], errors="coerce") < 0).any():
        issues.append("Negative Gross_Pay found.")
    return issues

def main():
    frames = {table: load_and_clean(table, filename) for table, filename in FILES.items()}
    issues = validate(frames)

    with sqlite3.connect(DB) as con:
        for table, df in frames.items():
            df.to_sql(table, con, if_exists="replace", index=False)
            df.to_csv(CLEAN / f"{table}_cleaned.csv", index=False, encoding="utf-8-sig")

    print("Loaded tables:", ", ".join(frames))
    print("Validation issues:", issues if issues else "None")
    print("SQLite:", DB)
    print("Cleaned CSV folder:", CLEAN)

if __name__ == "__main__":
    main()
