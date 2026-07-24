# Looker Studio Calculated Fields

Use these as calculated fields after importing the CSVs.

```text
Paid On Time Flag
CASE WHEN Paid_On_Time = "Yes" THEN 1 ELSE 0 END

OT Compliance Flag
CASE WHEN OT_Rate_Compliant = "Yes" THEN 1 ELSE 0 END

Compliance Flag
CASE WHEN Status = "Compliant" THEN 1 ELSE 0 END

Compliance Exception Flag
CASE WHEN Status = "Non-Compliant" THEN 1 ELSE 0 END

Pay Equity Group
CASE
  WHEN Gender = "Female" THEN "Female"
  WHEN Gender = "Male" THEN "Male"
  ELSE "Other/Unspecified"
END
```

Recommended scorecards:
- SUM(Gross_Pay)
- SUM(Net_Pay)
- SUM(OT_Pay)
- AVG(Attendance_Rate)
- AVG(Paid On Time Flag)
- AVG(Compliance Flag)
- SUM(Compliance Exception Flag)

Format percentage flags as **Percent**.
