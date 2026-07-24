# HCC Analytics BD — Release Notes

## v1.2.0 — Security & Power BI Upload Readiness

**Release date:** 24 July 2026  
**Prepared by:** Musa

### 🟨 Power BI file upload

- Added the official `powerbi/` location and secure PBIX upload checklist.
- Documented the recommended file name: `HCC_Analytics_BD.pbix`.
- Added guidance for Git LFS or GitHub Release assets when the PBIX file is too large for normal Git history.
- Added mandatory checks for cached credentials, private endpoints, Power Query parameters, custom visuals, gateways, hidden data and Row-Level Security.
- Confirmed that the current CSV model, data dictionary and DAX guidance remain ready for building the Power BI report.

> A native PBIX binary is not generated or internally inspected by this repository. Upload it only after completing the manual review in `powerbi/README.md`.

### 🔐 Security hardening

- Removed automatic repository-writing behaviour from the routine build workflow.
- Reduced GitHub Actions permissions to read-only for validation and security checks.
- Pinned `actions/checkout` and `actions/setup-python` to immutable commit SHAs.
- Pinned build and analytics dependencies to reviewed versions.
- Added weekly Bandit static analysis and `pip-audit` dependency scanning.
- Added Dependabot for Python and GitHub Actions updates.
- Added CODEOWNERS for security-sensitive files and binary analytics assets.
- Added a responsible vulnerability-disclosure policy.
- Added spreadsheet-formula neutralisation for cleaned CSV exports.
- Added allow-list and resolved-path validation for pipeline source files.

### ✅ Security review result

The repository is a local analytics project and exposes no web server, login system or public API. The review identified two material hardening opportunities:

1. a GitHub Actions workflow had broad write permission and automatically pushed generated files;
2. cleaned external text could be reopened in spreadsheet software without formula-prefix neutralisation.

Both items were remediated in this release. No confirmed exploitable remote-code-execution, credential-exposure, SQL-injection or authentication vulnerability was found in the reviewed Python paths.

### ⚠️ Residual controls

- Enable branch protection/rulesets for `main` in GitHub settings.
- Require pull-request review and CODEOWNER approval for protected paths.
- Enable private vulnerability reporting and secret scanning where available.
- Review all future `.pbix`, `.xlsx`, `.sqlite`, notebook and archive binaries before release.
- Never upload real employee, salary, tax, bank or identity data.

### 📦 Upgrade

```bash
git pull origin main
pip install -r python_sqlite/requirements.txt
```

### Tag

```text
v1.2.0
```
