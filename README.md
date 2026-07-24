# 🇧🇩 HCC Analytics BD

## HR Compensation & Compliance Analytics for Bangladesh

A ready-to-use **synthetic HR analytics dataset and dashboard pack** for Bangladesh-focused compensation, benefits, attendance, payroll and compliance analysis.

[![Security Checks](https://github.com/samusa099/hcc-analytics-bd/actions/workflows/security.yml/badge.svg)](https://github.com/samusa099/hcc-analytics-bd/actions/workflows/security.yml)
[![Build Validation](https://github.com/samusa099/hcc-analytics-bd/actions/workflows/build-project.yml/badge.svg)](https://github.com/samusa099/hcc-analytics-bd/actions/workflows/build-project.yml)
![Release](https://img.shields.io/badge/release-v1.2.0-7C3AED)
![Data](https://img.shields.io/badge/data-100%25%20synthetic-1E8E5A)

**Prepared by:** Musa  
**Version:** 1.2.0  
**Data:** 100% synthetic demo data

## 📦 Included

- 📊 Two interactive Excel dashboards
- 📁 BI-ready CSV datasets and data dictionary
- 🧮 HR KPI and payroll calculation fields
- ⚖️ Bangladesh labour and payroll compliance reference table
- 🐍 Python data-cleaning notebook and secured pipeline
- 🗄️ SQLite database with analytical views and SQL queries
- 📈 Power BI DAX and Looker Studio calculated-field guides
- 🟨 Secure Power BI file-upload guidance
- 🔐 Automated dependency and static-security checks
- 🖼️ Visual usage guide

## 🚀 Quick Start

1. Open `excel/Bangladesh_HR_Compensation_Compliance_Dashboards.xlsx`.
2. Review the `Start_Here` sheet.
3. Select a month from the dashboard dropdown.
4. Replace synthetic data with structured, authorised data when needed.
5. For Power BI or Looker Studio, import the CSV files from `data/`.
6. For Python and SQLite, use the files inside `python_sqlite/`.

## 📘 Documentation

- **[Complete Dataset Usage Guide](DATASET_USAGE_GUIDE.md)** — calculations, use cases and platform workflows
- **[Power BI Upload Guide](powerbi/README.md)** — PBIX location, large-file method and security checklist
- **[v1.2.0 Release Notes](RELEASE_NOTES.md)** — Power BI upload readiness and security changes
- **[Security Policy](SECURITY.md)** — responsible disclosure and data-protection rules
- **[Security Review & Closure](docs/SECURITY_REVIEW_2026-07-24.md)** — findings, remediation and residual controls

## 🗂 Main Folders

```text
excel/          Excel dashboards and analysis workbook
data/           Clean CSV tables and data dictionary
bi/             Power BI and Looker Studio setup files
powerbi/        Approved location and review guide for native Power BI files
python_sqlite/  Notebook, secured pipeline, SQLite database and SQL
guide/          Visual instructions and dashboard previews
scripts/        Reproducible project generator
```

## 🔐 Security Baseline

- Routine CI workflows use read-only repository permission.
- Official GitHub Actions are pinned to immutable commit SHAs.
- Bandit and `pip-audit` run through GitHub Actions.
- Dependabot monitors Python and GitHub Actions dependencies.
- Cleaned CSV exports neutralise spreadsheet-formula prefixes.
- CODEOWNERS covers workflows, scripts, data tooling and binary analytics assets.

Branch protection and secret-scanning settings should also be enabled from the repository's GitHub settings.

## ⚠️ Important

This is a **learning, portfolio and decision-support template**—not legal, payroll or tax advice. Before live organisational use, verify the latest sector wage gazette, Bangladesh labour requirements, EPZ applicability, NBR tax rules and internal company policies.

Never commit real employee records, credentials, bank details, tax identifiers or confidential payroll data.
