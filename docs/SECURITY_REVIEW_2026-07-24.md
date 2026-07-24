# Security Review — HCC Analytics BD

**Review date:** 24 July 2026  
**Repository:** `samusa099/hcc-analytics-bd`  
**Reviewer:** Repository-maintenance review requested by Musa  
**Status:** **Closed — remediations committed**

## Scope reviewed

- `scripts/build_project.py`
- `python_sqlite/hr_pipeline.py`
- Python dependency declarations
- GitHub Actions workflows
- generated CSV, Excel, SQLite and notebook handling
- release and Power BI binary-upload process

## Architecture and attack surface

This repository is a local analytics and portfolio project. It does not expose a web server, API endpoint, authentication system, payment processor or production payroll service.

Primary security boundaries are therefore:

1. repository and GitHub Actions write permissions;
2. third-party Python and GitHub Actions dependencies;
3. ingestion and export of user-supplied HR text data;
4. upload of binary BI, spreadsheet, database and notebook assets;
5. accidental publication of real employee or credential data.

## Findings and closure

### SEC-001 — Routine build workflow could write directly to `main`

**Previous condition:** The build workflow used `contents: write` and automatically committed generated files after pushes to selected paths.

**Risk:** A compromised dependency, action reference or generator change could modify repository content using the workflow token.

**Remediation:**

- changed the workflow to read-only `contents: read`;
- removed automated commit and push behaviour;
- added reproducibility validation instead;
- disabled persisted checkout credentials;
- pinned official actions to immutable commit SHAs;
- added timeout and concurrency controls.

**Disposition:** Closed.

### SEC-002 — Spreadsheet formula injection in cleaned CSV exports

**Previous condition:** Imported text was written to cleaned CSV files without neutralising values beginning with `=`, `+`, `-` or `@`.

**Risk:** A malicious external HR value could be interpreted as a spreadsheet formula when opened in Excel or Google Sheets.

**Remediation:**

- added formula-prefix neutralisation for spreadsheet-facing cleaned CSV output;
- preserved unsuffixed cleaned values inside SQLite for analytical use;
- added configured table allow-list and resolved-path validation.

**Disposition:** Closed.

### SEC-003 — Mutable and broadly specified dependencies

**Previous condition:** Runtime dependencies used broad minimum versions, and build dependencies were installed without version pins.

**Risk:** Non-reproducible builds and increased dependency supply-chain exposure.

**Remediation:**

- pinned build and analytics dependencies;
- added weekly Dependabot updates;
- added `pip-audit` dependency scanning;
- added Bandit static analysis.

**Disposition:** Closed with ongoing monitoring.

## Negative findings

No confirmed exploitable instance was identified in the reviewed Python paths for:

- command or shell injection;
- unsafe deserialisation;
- authentication or authorisation bypass;
- exposed hard-coded credential or token;
- remotely controlled SQL injection;
- path traversal from an external request;
- remote code execution.

The SQLite schema-generation identifiers are sourced from internal configured table structures rather than an external request. Data values are inserted with parameterised statements or pandas APIs.

## Power BI and binary-file control

Binary `.pbix`, `.xlsx`, `.sqlite`, notebook and archive files cannot be fully assessed through text review. Before upload:

- use only synthetic/anonymised records;
- remove cached credentials and private connection information;
- inspect Power Query parameters and custom visuals;
- clear unnecessary data-source permissions;
- use Git LFS or a release asset for large PBIX files;
- scan the binary using endpoint security.

See `powerbi/README.md`.

## Repository protections added

- `SECURITY.md`
- `.github/CODEOWNERS`
- `.github/dependabot.yml`
- `.github/workflows/security.yml`
- pinned GitHub Actions references
- read-only build validation workflow

## Manual GitHub settings still recommended

The available repository connector did not expose branch-ruleset administration. The repository owner should enable these settings manually for `main`:

- require a pull request before merging;
- require at least one approval;
- require CODEOWNER review;
- require passing build and security checks;
- block force pushes and branch deletion;
- require conversation resolution;
- enable secret scanning, push protection and private vulnerability reporting where available.

## Closure statement

The tracked workflow-token and spreadsheet-formula risks have been remediated. The security-hardening case may be closed as completed, subject to recurring CI scans and the manual GitHub settings listed above.
