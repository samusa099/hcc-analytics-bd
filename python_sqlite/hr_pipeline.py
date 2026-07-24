#!/usr/bin/env python3
"""
Bangladesh HR Compensation & Compliance Analytics
CSV cleaning + validation + SQLite loader.

Important:
- Demo decision-support project, not legal advice.
- Update the configured sector wage floor and tax logic before operational use.
- Cleaned CSV exports neutralize spreadsheet-formula prefixes to reduce CSV injection risk.
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

SPREADSHEET_FORMULA_PREFIXES = ("=", "+", "-", "@")


def clean_text(series: pd.Series) -> pd.Series:
    """Trim text and normalize blank-like values."""
    return series.astype("string").str.strip().replace({"": pd.NA, "nan": pd.NA})


def neutralize_spreadsheet_formulas(value):
    """Prefix formula-like text so Excel/Sheets treats it as literal text.

    This is applied only to cleaned CSV exports. SQLite retains the cleaned value
    without the protective apostrophe so analytical queries are unaffected.
    """
    if pd.isna(value) or not isinstance(value, str):
        return value
    stripped = value.lstrip()
    if stripped.startswith(SPREADSHEET_FORMULA_PREFIXES):
        return "'" + value
    return value


def spreadsheet_safe_copy(df: pd.DataFrame) -> pd.DataFrame:
    """Return a copy suitable for opening as CSV in spreadsheet software."""
    safe = df.copy()
    for column in safe.select_dtypes(include=["object", "string"]).columns:
        safe[column] = safe[column].map(neutralize_spreadsheet_formulas)
    return safe


def load_and_clean(table: str, filename: str) -> pd.DataFrame:
    """Load a configured local CSV and apply deterministic cleaning."""
    if table not in FILES or FILES[table] != filename:
        raise ValueError(f"Unapproved table or filename: {table!r}, {filename!r}")

    source = (DATA / filename).resolve()
    if source.parent != DATA.resolve():
        raise ValueError(f"Source path escapes the data directory: {source}")

    df = pd.read_csv(source)
    df.columns = [column.strip().replace(" ", "_") for column in df.columns]
    for column in df.select_dtypes(include="object").columns:
        df[column] = clean_text(df[column])
    for column in DATE_FIELDS.get(table, []):
        if column in df.columns:
            df[column] = pd.to_datetime(df[column], errors="coerce").dt.date
    return df.drop_duplicates()


def validate(frames: dict[str, pd.DataFrame]) -> list[str]:
    """Run referential-integrity and basic payroll-quality checks."""
    issues: list[str] = []
    employee = frames["employees"]
    payroll = frames["payroll_monthly"]
    attendance = frames["attendance_leave_monthly"]

    if employee["Employee_ID"].duplicated().any():
        issues.append("Duplicate Employee_ID found.")

    missing_payroll_employees = set(payroll["Employee_ID"].dropna()) - set(employee["Employee_ID"].dropna())
    if missing_payroll_employees:
        issues.append(f"Payroll has {len(missing_payroll_employees)} unknown Employee_ID values.")

    missing_attendance_employees = set(attendance["Employee_ID"].dropna()) - set(employee["Employee_ID"].dropna())
    if missing_attendance_employees:
        issues.append(f"Attendance has {len(missing_attendance_employees)} unknown Employee_ID values.")

    if "Gross_Pay" in payroll and (pd.to_numeric(payroll["Gross_Pay"], errors="coerce") < 0).any():
        issues.append("Negative Gross_Pay found.")

    return issues


def main() -> None:
    frames = {table: load_and_clean(table, filename) for table, filename in FILES.items()}
    issues = validate(frames)

    with sqlite3.connect(DB) as connection:
        for table, dataframe in frames.items():
            dataframe.to_sql(table, connection, if_exists="replace", index=False)
            safe_export = spreadsheet_safe_copy(dataframe)
            safe_export.to_csv(CLEAN / f"{table}_cleaned.csv", index=False, encoding="utf-8-sig")

    print("Loaded tables:", ", ".join(frames))
    print("Validation issues:", issues if issues else "None")
    print("SQLite:", DB)
    print("Spreadsheet-safe cleaned CSV folder:", CLEAN)


if __name__ == "__main__":
    main()
