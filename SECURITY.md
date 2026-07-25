<h1 align="center">🛡️ Security Policy</h1>

<p align="center">
  <strong>Responsible vulnerability reporting and safe handling of HR analytics assets</strong>
</p>

<p align="center">
  <img alt="Private Reporting" src="https://img.shields.io/badge/reporting-private-C92A2A?style=flat&logo=github">
  <img alt="Synthetic Data" src="https://img.shields.io/badge/data-synthetic%20only-6F42C1?style=flat">
  <img alt="Dependency Review" src="https://img.shields.io/badge/dependencies-monitored-025E8C?style=flat&logo=dependabot">
  <img alt="Security Checks" src="https://github.com/samusa099/hcc-analytics-bd/actions/workflows/security.yml/badge.svg">
</p>

<p align="center">
  <a href="#-supported-versions">Supported Versions</a> •
  <a href="#-reporting-a-vulnerability">Reporting</a> •
  <a href="#-security-scope">Scope</a> •
  <a href="#-response-process">Response</a> •
  <a href="#-data-protection-rules">Data Protection</a>
</p>

> [!CAUTION]
> Do not publish vulnerability details, credentials, real employee information or confidential files in a public issue, discussion or pull request.

---

## ✅ Supported Versions

| Version | Security support |
|---|---|
| `1.2.x` | ✅ Actively supported |
| `1.1.x` | ⚠️ Best-effort support |
| `1.0.x` and earlier | ❌ Not actively supported |
| Unreleased `main` branch | ✅ Reviewed through repository checks and pull requests |

Users should reproduce issues against the latest supported release or current default branch where practical.

---

## 📨 Reporting a Vulnerability

Use a private reporting route:

1. Open the repository's **Security** tab.
2. Select **Report a vulnerability** when GitHub Private Vulnerability Reporting is available.
3. When private reporting is unavailable, contact the repository owner through the contact options on the owner's GitHub profile.
4. Share only enough information publicly to establish a private communication channel.

### Include in the report

- affected file, workflow, dataset or binary asset;
- affected version, branch or commit SHA;
- clear reproduction steps;
- expected and observed behaviour;
- security or privacy impact;
- screenshots or proof of concept with sensitive values removed;
- suggested mitigation, when available;
- confirmation that no real employee or confidential organisational data was accessed or disclosed.

### Do not include publicly

- live credentials, tokens, secrets or connection strings;
- personal employee, applicant, payroll, tax, medical or banking information;
- weaponised exploit instructions that create unnecessary risk;
- confidential third-party data;
- unredacted local paths, email addresses or account identifiers.

---

## 🎯 Security Scope

This repository is a public learning and portfolio project containing synthetic HR data, Excel and Power BI assets, Python and SQL files, SQLite data and documentation. It does not operate a production payroll service, public authentication system or hosted employee database.

### In scope

| Area | Examples |
|---|---|
| **GitHub Actions** | Excessive permissions, unsafe script execution, unpinned actions or secret exposure. |
| **Python dependencies** | Known vulnerabilities, malicious packages or unsafe dependency handling. |
| **Data pipelines** | CSV formula injection, unsafe paths, insecure temporary files or uncontrolled exports. |
| **Binary analytics files** | Hidden macros, external connections, cached credentials or embedded sensitive content. |
| **Repository configuration** | Branch-protection gaps, exposed secrets or unsafe release practices. |
| **Privacy controls** | Accidental inclusion of real employee, applicant, payroll, tax, identity or bank information. |

### Generally out of scope

- social-engineering attacks against the maintainer;
- denial-of-service testing;
- automated scanning that creates excessive traffic;
- reports based only on missing optional headers for services the repository does not operate;
- vulnerabilities in third-party platforms without a repository-specific impact;
- speculative issues without a reproducible security consequence.

A report may still be reviewed when it falls outside the normal scope but demonstrates a credible risk to repository users.

---

## ⏱️ Response Process

| Stage | Target |
|---|---|
| **Acknowledgement** | Within 7 calendar days |
| **Initial triage** | Within 14 calendar days |
| **Severity and scope confirmation** | After reproduction and impact review |
| **Remediation plan** | Based on severity, exploitability and affected assets |
| **Disclosure coordination** | After a fix or reasonable mitigation is available |

Targets are goals rather than guaranteed service-level commitments. Complex reports or maintainer availability may affect timing.

### Triage priorities

| Priority | Typical impact |
|---|---|
| **Critical** | Exposed credentials, confirmed sensitive-data disclosure or compromise of repository publishing controls. |
| **High** | Practical code execution, dependency compromise or high-impact workflow permission abuse. |
| **Medium** | Exploitable data injection, unsafe external connection or meaningful integrity risk requiring user interaction. |
| **Low** | Limited-impact hardening issue, defence-in-depth gap or documentation weakness. |

---

## 🔄 Remediation and Disclosure

The maintainer may:

1. reproduce and validate the report;
2. limit access to affected assets when necessary;
3. prepare a fix, mitigation or documentation update;
4. run repository validation and security checks;
5. publish a release note or advisory when appropriate;
6. credit the reporter with permission.

Please allow a reasonable remediation period before public disclosure. Coordinated disclosure reduces risk to users who may have downloaded or adapted the project.

---

## 🔐 Data-Protection Rules

### Never commit

- real employee or applicant records;
- CVs, national identifiers, passports or photographs;
- payroll bank details, tax identifiers or financial account data;
- medical, disciplinary, investigation or performance records;
- credentials, API keys, tokens, cookies or connection strings;
- confidential policies, legal files or client information.

### Review before release

- [ ] `.pbix`, `.xlsx`, `.sqlite`, notebook and archive files have been inspected.
- [ ] External connections and refresh credentials have been removed.
- [ ] Hidden worksheets, macros, comments and embedded objects have been reviewed.
- [ ] Local file paths and usernames are not exposed.
- [ ] Screenshots contain no personal notifications or identifiable records.
- [ ] CSV exports neutralise unsafe spreadsheet-formula prefixes.
- [ ] All demonstration records are synthetic or properly authorised and anonymised.

> [!IMPORTANT]
> Anonymisation is not guaranteed merely by removing names. Combinations of department, role, salary, location, age or dates may still identify a real person.

---

## ⚙️ Implemented Repository Controls

- Pull-request workflow for protected-branch changes.
- Required asset-validation and security checks.
- Read-only permissions for routine GitHub Actions jobs.
- Pinned trusted GitHub Actions.
- Bandit static analysis for Python code.
- Dependency auditing with `pip-audit`.
- Dependabot monitoring for Python and GitHub Actions dependencies.
- CODEOWNERS coverage for security-sensitive and binary analytics assets.
- Formula-prefix neutralisation in cleaned CSV exports.

These controls reduce risk but do not replace review, secure local handling or organisational governance.

---

## 🤝 Good-Faith Research

Security research should:

- avoid privacy violations and data destruction;
- use the minimum testing necessary to demonstrate impact;
- avoid disrupting GitHub or third-party services;
- stop immediately if real confidential information is encountered;
- report findings privately and provide reasonable time for remediation.

This policy is not legal advice and does not authorise activity that violates applicable law, platform terms or third-party rights.

---

## 🏅 Disclosure Credit

Responsible reporters may be credited in release notes or an advisory with their permission. Anonymous reporting and anonymous acknowledgement requests will be respected where reasonably possible.

---

<p align="center">
  <strong>Report privately. Minimise exposure. Protect people and data first.</strong>
</p>
