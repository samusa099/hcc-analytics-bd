# Security Policy

## Supported version

| Version | Supported |
|---|---|
| `1.2.x` | ✅ |
| `1.1.x` and earlier | Best-effort only |

## Reporting a vulnerability

Please **do not publish sensitive vulnerability details in a public issue**.

Use GitHub's **Private vulnerability reporting** feature from the repository's **Security** tab when it is enabled. If private reporting is unavailable, contact the repository owner through the GitHub profile and provide only enough information to establish a private reporting channel.

A useful report should include:

- affected file or workflow;
- affected version or commit;
- reproducible steps;
- expected security impact;
- proposed mitigation, when available;
- confirmation that no real employee data was accessed or disclosed.

## Response targets

- Initial acknowledgement: within 7 days
- Triage decision: within 14 days
- Remediation target: based on severity and reproducibility

## Repository security boundaries

This project contains synthetic HR data, local Python scripts, Excel assets, SQLite data and BI documentation. It does not operate a public web service, authentication system or production payroll service.

The following remain security-sensitive:

- GitHub Actions and repository write permissions;
- Python and transitive dependencies;
- spreadsheet/CSV formula injection when external data is imported;
- macros, external connections or embedded content in uploaded Excel/Power BI files;
- accidental upload of real employee, salary, tax or identity data.

## Data-protection rules

- Do not commit real employee records, credentials, tokens, tax identifiers or payroll bank information.
- Review `.pbix`, `.xlsx`, `.sqlite`, notebook and archive files before release.
- Remove external connections, cached credentials, macros and hidden sensitive data.
- Use synthetic or properly anonymised data only.

## Disclosure credit

Responsible reporters may be credited in release notes with their permission.
