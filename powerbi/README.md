# 🟨 Power BI File Upload Guide

## HCC Analytics BD

This folder is the approved location for Power BI project assets associated with the HCC Analytics BD dataset.

## Recommended file name

```text
HCC_Analytics_BD.pbix
```

For source-controlled development, a Power BI Project (`.pbip`) is preferred when available because its text-based project files are easier to review than a single binary `.pbix` file.

## Upload method

### File below GitHub's practical repository limit

1. Open the report in Power BI Desktop.
2. Refresh it using only the synthetic files from `data/`.
3. Remove credentials and unused connections.
4. Save the reviewed file as `HCC_Analytics_BD.pbix`.
5. Upload it into this `powerbi/` folder.

### Large PBIX file

Use **Git LFS** or attach the PBIX as a **GitHub Release asset** rather than placing a large binary in ordinary Git history.

## Mandatory security review before upload

- ✅ Confirm all data is synthetic or properly anonymised.
- ✅ Remove cached credentials, API keys, database passwords and local-user paths.
- ✅ Review **Data source settings** and clear permissions where appropriate.
- ✅ Remove unused queries, hidden tables and unnecessary columns.
- ✅ Check Power Query parameters and M code for secrets or private endpoints.
- ✅ Confirm no external custom visual or connector is untrusted.
- ✅ Review Row-Level Security roles and test them when included.
- ✅ Disable or remove automatic refresh settings that rely on private gateways.
- ✅ Scan the file with endpoint security before publishing.

## Repository status

The CSV model, DAX guide and data-model instructions are already available in `data/` and `bi/`. A native PBIX binary should be uploaded only after the manual security review above because this repository does not generate or validate PBIX internals automatically.

## Related files

- `bi/data_model_and_setup.md`
- `bi/power_bi_dax_measures.md`
- `data/data_dictionary.csv`
- `excel/Bangladesh_HR_Compensation_Compliance_Dashboards.xlsx`
