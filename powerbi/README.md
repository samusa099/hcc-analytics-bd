# 🟨 Power BI Project Guide

## HCC Analytics BD

This folder is the approved location for Power BI project assets built from the **Bangladesh HR Compensation & Compliance Analytics** dataset.

Use it to create management-ready dashboards for workforce, payroll, attendance, benefits, pay equity and compliance monitoring—without exposing real employee or company data.

> 📘 For the full use-case, page-design and implementation guide, read [`POWER_BI_USAGE_GUIDE.md`](POWER_BI_USAGE_GUIDE.md).

---

## 🚀 Best ways to use this Power BI project

| Use case | Best audience | Primary outcome |
|---|---|---|
| Executive HR overview | Management, HR Head | Headcount, payroll cost, attendance and compliance at a glance |
| Payroll cost control | HR Operations, Finance | Gross pay, net pay, overtime, deductions and monthly variance |
| Attendance monitoring | HR Operations, Line Managers | Absence, lateness, leave and working-hours exceptions |
| Compensation review | HR, Finance, Leadership | Grade, department, gender and location pay comparisons |
| Benefits coverage | HR, Rewards Team | PF, insurance, medical, transport and meal enrolment gaps |
| Compliance tracking | HR Compliance, Audit | Open exceptions, risk levels, owners, due dates and closure status |
| Portfolio and training | Learners, Analysts, Recruiters | Power Query, star schema, DAX, visual storytelling and HR analytics practice |

---

## 🧭 Where it can be used

- **HR monthly review meetings**
- **Management and board presentations**
- **Payroll and finance reconciliation**
- **Department manpower-cost analysis**
- **Internal audit and compliance follow-up**
- **Compensation and pay-equity studies**
- **HR analytics training, GitHub and portfolio projects**
- **Scenario-based interview or assessment demonstrations**

---

## ⚡ Quick start

1. Download or clone the repository.
2. Open **Power BI Desktop**.
3. Select **Get Data → Text/CSV** and import the required files from `data/`.
4. Use `employees` as the main employee dimension.
5. Create one-to-many relationships using `Employee_ID`.
6. Add a calendar table for payroll, attendance and compliance trend analysis.
7. Copy the recommended measures from [`../bi/power_bi_dax_measures.md`](../bi/power_bi_dax_measures.md).
8. Build pages using the blueprint in [`POWER_BI_USAGE_GUIDE.md`](POWER_BI_USAGE_GUIDE.md).
9. Refresh, validate totals and remove all credentials before sharing.

Recommended source model: [`../bi/data_model_and_setup.md`](../bi/data_model_and_setup.md)

---

## 🗂️ Recommended report pages

1. **Executive Overview** — headcount, payroll, attendance and compliance
2. **Workforce Profile** — department, grade, location, gender and employment type
3. **Payroll & Overtime** — gross pay, net pay, OT cost, deductions and variance
4. **Attendance & Leave** — attendance rate, absence, lateness, leave and working hours
5. **Benefits Coverage** — eligibility, enrolment and benefit gaps
6. **Pay Equity** — gender, grade and department compensation comparison
7. **Compliance & Risk** — exception status, risk level, owner, due date and closure tracking
8. **Employee Drill-through** — one synthetic employee’s consolidated record

---

## 📦 Recommended project format

For a normal Power BI Desktop file:

```text
HCC_Analytics_BD.pbix
```

For source-controlled development, prefer a Power BI Project when available:

```text
HCC_Analytics_BD.pbip
```

A `.pbip` project is easier to inspect, compare and review because more of its structure is stored as text rather than one large binary file.

---

## ⬆️ Upload method

### Standard-size PBIX

1. Refresh using only the synthetic files from `data/`.
2. Confirm all visuals and measures reconcile with the source files.
3. Remove credentials, local paths and unused connections.
4. Save the reviewed file as `HCC_Analytics_BD.pbix`.
5. Upload it into this `powerbi/` folder.

### Large PBIX

Use **Git LFS** or attach the PBIX as a **GitHub Release asset** rather than adding a large binary repeatedly to normal Git history.

---

## 🔐 Mandatory security review before upload

- ✅ Confirm all data is synthetic or properly anonymised.
- ✅ Remove cached credentials, API keys, database passwords and private endpoints.
- ✅ Replace personal local paths with parameters or documented relative paths.
- ✅ Review **Data source settings** and clear permissions where appropriate.
- ✅ Remove unused queries, hidden tables and unnecessary columns.
- ✅ Inspect Power Query parameters and M code for secrets.
- ✅ Confirm external custom visuals and connectors are trusted.
- ✅ Review and test Row-Level Security roles when included.
- ✅ Remove private gateway or automatic-refresh dependencies.
- ✅ Scan the file with endpoint security before publishing.

---

## ⚠️ Responsible-use boundary

This is a **synthetic learning and decision-support project**. It is not a substitute for legal, payroll, tax or compliance advice.

Before real organisational use, validate:

- current wage gazettes and sector rules;
- applicable Bangladesh labour requirements;
- tax-year and payroll rules;
- company policies and collective agreements;
- data privacy, access and retention requirements.

---

## 🔗 Related files

- [`POWER_BI_USAGE_GUIDE.md`](POWER_BI_USAGE_GUIDE.md)
- [`../bi/data_model_and_setup.md`](../bi/data_model_and_setup.md)
- [`../bi/power_bi_dax_measures.md`](../bi/power_bi_dax_measures.md)
- [`../data/data_dictionary.csv`](../data/data_dictionary.csv)
- [`../DATASET_USAGE_GUIDE.md`](../DATASET_USAGE_GUIDE.md)
- [`../excel/Bangladesh_HR_Compensation_Compliance_Dashboards.xlsx`](../excel/Bangladesh_HR_Compensation_Compliance_Dashboards.xlsx)

---

**Prepared by:** Musa  
**Project:** HCC Analytics BD  
**Data type:** Fully synthetic demo data
