<h1 align="center">🚀 Contributing to HCC Analytics BD</h1>

<p align="center">
  <strong>Focused contributions that improve HR analytics quality, usability and responsible data practice</strong>
</p>

<p align="center">
  <img alt="Contributions Welcome" src="https://img.shields.io/badge/contributions-welcome-2E8B57?style=flat">
  <img alt="Pull Request Required" src="https://img.shields.io/badge/workflow-pull%20request-2F81F7?style=flat&logo=github">
  <img alt="Synthetic Data Only" src="https://img.shields.io/badge/data-synthetic%20only-6F42C1?style=flat">
  <img alt="Checks Required" src="https://img.shields.io/badge/checks-required-CB7A00?style=flat&logo=githubactions">
</p>

<p align="center">
  <a href="#-before-you-start">Before You Start</a> •
  <a href="#-suitable-contributions">Suitable Contributions</a> •
  <a href="#-contribution-workflow">Workflow</a> •
  <a href="#-quality-standards">Quality Standards</a> •
  <a href="#-pull-request-checklist">PR Checklist</a>
</p>

> [!IMPORTANT]
> This is a public portfolio and learning repository. Contributions must use synthetic data and must not expose real employee, applicant, payroll, medical, banking, tax or confidential organisational information.

---

## 👋 Before You Start

Thank you for considering a contribution to **HCC Analytics BD**.

Before opening a pull request:

1. Read the project [`README.md`](README.md).
2. Review the [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md).
3. Check the [`SECURITY.md`](SECURITY.md) before reporting vulnerabilities or sensitive data exposure.
4. Search existing issues and pull requests to avoid duplicate work.
5. Keep the proposed change focused and explain its analytical value.

For a substantial redesign, new dataset, new workflow or breaking structural change, open a discussion or issue before investing significant effort.

---

## ✨ Suitable Contributions

| Area | Examples |
|---|---|
| **Data quality** | Correct inconsistent fields, relationships, types, validation rules or documentation. |
| **HR analytics** | Add reusable compensation, payroll, attendance, leave, benefits or compliance analysis. |
| **Excel** | Improve formulas, dashboard usability, validation, accessibility or instructions. |
| **Power BI** | Add documented DAX, model guidance, page blueprints or secure file-handling practices. |
| **Python and SQL** | Improve cleaning, tests, queries, views, reproducibility or error handling. |
| **Documentation** | Clarify setup, calculations, assumptions, limitations, navigation or examples. |
| **Accessibility** | Improve contrast, labels, alternative text, chart interpretation or readable structure. |
| **Security** | Strengthen dependency controls, permissions, data sanitisation or release validation. |

### Contributions that will not be accepted

- real personal or organisational records;
- credentials, tokens, keys or connection strings;
- unlicensed third-party data, images or code;
- unexplained binary-file changes;
- generated content that has not been reviewed for accuracy;
- misleading, discriminatory or legally unsupported HR conclusions;
- unrelated mass-formatting or repository-wide changes without a clear purpose.

---

## 🔄 Contribution Workflow

### 1. Fork and create a focused branch

Use a short descriptive branch name:

```text
feat/payroll-variance-view
fix/attendance-validation
docs/power-bi-refresh-guide
security/dependency-hardening
```

Recommended prefixes:

| Prefix | Use |
|---|---|
| `feat/` | New analytical capability or project feature |
| `fix/` | Bug, calculation, data or documentation correction |
| `docs/` | Documentation-only improvement |
| `security/` | Security or data-protection improvement |
| `refactor/` | Internal restructuring without intended output change |
| `test/` | Validation or automated test improvement |

### 2. Make one coherent change

- Avoid mixing unrelated modifications.
- Preserve the existing folder structure unless restructuring is the purpose of the pull request.
- Document new assumptions, fields, relationships and formulas.
- Keep generated files reproducible where practical.
- Do not silently alter KPI definitions or historical outputs.

### 3. Validate the work

Run the checks relevant to your change.

| Change type | Minimum validation |
|---|---|
| Markdown/documentation | Verify links, headings, tables, images and rendered formatting. |
| CSV/data dictionary | Check schema, types, duplicate keys, missing values and formula-injection risk. |
| Python | Compile sources, run applicable tests and review security/static-analysis results. |
| SQL/SQLite | Validate schema, joins, totals, views and repeatability. |
| Excel/Power BI | Reconcile totals, inspect external connections and verify no sensitive cached data. |
| GitHub Actions | Use least privilege, pin trusted actions and test the workflow safely. |

### 4. Commit clearly

Use concise, action-oriented commit messages:

```text
docs: clarify payroll KPI definitions
fix: prevent unsafe CSV formula prefixes
feat: add department overtime analysis
security: pin workflow action versions
```

### 5. Open a pull request

The pull request should explain:

- the problem or opportunity;
- what changed;
- why the change is useful;
- how it was validated;
- any limitation, risk or follow-up item;
- screenshots or previews for visible dashboard or documentation changes.

---

## 📐 Quality Standards

| Standard | Requirement |
|---|---|
| **Accuracy** | Calculations and claims must be traceable to documented fields and assumptions. |
| **Reproducibility** | Another contributor should be able to follow the documented workflow. |
| **Clarity** | Names, labels, instructions and visuals should be understandable without hidden context. |
| **Data safety** | Use synthetic data and remove credentials, personal data and external connections. |
| **Scope control** | Keep changes focused and avoid unnecessary generated or temporary files. |
| **Compatibility** | Preserve existing paths and interfaces unless the change deliberately replaces them. |
| **Accessibility** | Use readable contrast, meaningful labels and alternative text where applicable. |
| **Documentation** | Update related guides when behaviour, calculations or structure changes. |

---

## 🧪 Data and Binary-File Policy

### Synthetic data requirement

All contributed records must remain synthetic. Contributions containing real personal, medical, payroll, applicant, banking, tax, identity or confidential organisational data will be rejected.

### CSV and spreadsheet safety

- Neutralise values beginning with spreadsheet-formula prefixes when exporting untrusted text.
- Check hidden sheets, named ranges, comments, macros and external links.
- Remove local paths, cached credentials and data-source authentication.
- Confirm that screenshots do not expose personal notifications, usernames or file paths.

### Power BI and database files

- Review `.pbix`, `.xlsx`, `.sqlite`, notebook and archive files before submission.
- Explain why a binary change is required.
- Include supporting source files or reproducible steps when possible.
- Avoid committing redundant exports, backups or temporary copies.

---

## ✅ Pull Request Checklist

Before requesting review, confirm:

- [ ] The change has one clear purpose.
- [ ] No real or confidential data is included.
- [ ] No credentials, tokens or connection strings are present.
- [ ] Calculations and assumptions are documented.
- [ ] Relevant totals and relationships have been validated.
- [ ] Documentation and navigation links are updated.
- [ ] Visual changes include a screenshot or preview where useful.
- [ ] Required GitHub Actions checks pass.
- [ ] The pull request explains limitations and follow-up work.
- [ ] The change follows the Code of Conduct.

---

## 🔍 Review and Merge

Maintainers may request changes for correctness, security, scope, reproducibility, accessibility or documentation quality.

A pull request is normally ready to merge when:

- required checks pass;
- material review comments are resolved;
- the branch is current enough to merge safely;
- the change does not introduce sensitive data or unsupported claims;
- the final diff contains only necessary files.

Maintainers may squash, rebase or merge according to repository settings and the nature of the contribution.

---

## 🛡️ Security Issues

Do not open a public issue for a vulnerability, leaked credential or sensitive-data exposure. Follow the private reporting process in [`SECURITY.md`](SECURITY.md).

---

<p align="center">
  <strong>Small, validated and well-documented contributions create the strongest analytics project.</strong>
</p>
