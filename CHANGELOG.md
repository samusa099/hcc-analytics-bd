# Changelog

All notable changes to HCC Analytics BD are documented here.

## [1.2.0] — 2026-07-24

### Added

- Secure Power BI upload guide and approved `powerbi/` location.
- `SECURITY.md` responsible-disclosure and data-protection policy.
- CODEOWNERS for security-sensitive and binary analytics assets.
- Dependabot configuration for Python and GitHub Actions.
- Automated Bandit and `pip-audit` security workflow.
- Pinned build dependency file.
- Release notes for Power BI upload readiness and security closure.

### Changed

- Build workflow is now read-only and validates reproducibility instead of pushing to `main`.
- GitHub Actions references are pinned to immutable commit SHAs.
- Python analytics dependencies are pinned to supported versions.
- Cleaned CSV output is spreadsheet-safe against formula-prefix injection.
- Pipeline input tables and paths are restricted to the configured allow-list.

### Security

- Closed automatic workflow write-permission risk.
- Closed spreadsheet/CSV formula-injection risk in cleaned exports.
- Added recurring dependency and static-code security checks.

## [1.1.0] — 2026-07-24

### Added

- Initial Bangladesh HR compensation and compliance analytics package.
- Excel dashboards, CSV data, Python/SQLite workflow and BI documentation.
