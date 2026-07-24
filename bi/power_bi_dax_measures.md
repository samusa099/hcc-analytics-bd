# Power BI DAX Measures

```DAX
Total Gross Payroll = SUM(payroll_monthly[Gross_Pay])

Total Net Payroll = SUM(payroll_monthly[Net_Pay])

Total OT Cost = SUM(payroll_monthly[OT_Pay])

Average Gross Pay = AVERAGE(payroll_monthly[Gross_Pay])

Paid On Time % =
DIVIDE(
    CALCULATE(COUNTROWS(payroll_monthly), payroll_monthly[Paid_On_Time] = "Yes"),
    COUNTROWS(payroll_monthly)
)

OT Rate Compliance % =
DIVIDE(
    CALCULATE(COUNTROWS(payroll_monthly), payroll_monthly[OT_Rate_Compliant] = "Yes"),
    COUNTROWS(payroll_monthly)
)

Compliance Score % =
DIVIDE(
    CALCULATE(COUNTROWS(compliance_register), compliance_register[Status] = "Compliant"),
    COUNTROWS(compliance_register)
)

Compliance Exceptions =
CALCULATE(COUNTROWS(compliance_register), compliance_register[Status] = "Non-Compliant")

Average Attendance % = AVERAGE(attendance_leave_monthly[Attendance_Rate])

Active Headcount =
CALCULATE(DISTINCTCOUNT(employees[Employee_ID]), employees[Active_Status] = "Active")

Female Average Gross =
CALCULATE(AVERAGE(payroll_monthly[Gross_Pay]), payroll_monthly[Gender] = "Female")

Male Average Gross =
CALCULATE(AVERAGE(payroll_monthly[Gross_Pay]), payroll_monthly[Gender] = "Male")

Pay Equity Ratio =
DIVIDE([Female Average Gross], [Male Average Gross])
```
