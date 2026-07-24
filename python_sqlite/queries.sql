-- Bangladesh HR Compensation & Compliance Analytics

-- 1) Monthly payroll KPIs
SELECT * FROM vw_monthly_kpis ORDER BY Payroll_Month;

-- 2) Department payroll for June 2026
SELECT *
FROM vw_department_payroll
WHERE Payroll_Month = '2026-06-01'
ORDER BY Gross_Pay DESC;

-- 3) Highest compliance exception categories
SELECT Compliance_Area,
       COUNT(*) AS Checks,
       SUM(CASE WHEN Status='Non-Compliant' THEN 1 ELSE 0 END) AS Exceptions,
       ROUND(100.0 * SUM(CASE WHEN Status='Compliant' THEN 1 ELSE 0 END) / COUNT(*), 2) AS Compliance_Pct
FROM compliance_register
GROUP BY Compliance_Area
ORDER BY Exceptions DESC;

-- 4) Employees with high-risk exceptions
SELECT *
FROM vw_employee_risk_flags
WHERE High_Risk_Count > 0
ORDER BY High_Risk_Count DESC, Exception_Count DESC;

-- 5) Overtime exceptions
SELECT p.Employee_ID, e.Employee_Name, p.Payroll_Month, p.OT_Hours, p.OT_Rate, p.OT_Pay
FROM payroll_monthly p
JOIN employees e ON e.Employee_ID = p.Employee_ID
WHERE p.OT_Rate_Compliant = 'No'
ORDER BY p.Payroll_Month, p.OT_Hours DESC;

-- 6) Wage payment delays
SELECT Employee_ID, Payroll_Month, Due_Date, Pay_Date, Net_Pay
FROM payroll_monthly
WHERE Paid_On_Time = 'No'
ORDER BY Payroll_Month, Pay_Date;
