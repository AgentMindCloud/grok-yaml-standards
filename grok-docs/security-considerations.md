# grok-docs.yaml — Security Considerations

## 1. Never configure `update_on: ["push"]` for docs that publish to external sites

If a docs target is automatically pushed to a public site (GitHub Pages, Netlify) on every commit, a bad push can expose work-in-progress content, partially merged features, or accidentally included sensitive information. Use `update_on: ["pr_merged"]` or `["release"]` for any docs with a public publish step, and add a manual review checkpoint in the pipeline.

## 2. Audit `source_files` globs to exclude credential files and private directories

When `source_files` includes broad patterns like `"**/*"`, Grok analyses every file in the repository to generate documentation — including `.env` files, key files, and internal configuration. Grok will not intentionally include secrets in output, but exposure risk increases with scope. Be explicit: list only the directories and file types that should inform the docs (e.g. `["src/**/*.ts", "README.md"]`).

## 3. Review `include_code_samples: true` output for hardcoded values before publishing

When code samples are generated from your source, they reflect what is actually in your code. If any source file contains a hardcoded API key, a development endpoint URL, or an internal hostname, those values may appear verbatim in generated documentation. Review auto-generated code samples before each publish, particularly after config changes.

## 4. Validate `target` paths to prevent unintended file overwrites

The `target` field accepts any path relative to the repository root. A misconfigured target like `../../.env` or `../Makefile` could overwrite files outside the documentation tree. Validate that `target` paths are within expected directories (e.g. `docs/`, `README.md`) and never point to executable scripts, CI configuration, or other sensitive files.

## 5. Treat automatically generated changelogs as a data-disclosure risk

If a `changelog` section is included in a docs target, Grok may summarise commit history and PR titles in the output. Commit messages and PR titles sometimes contain internal ticket numbers, employee names, or partial details of security fixes. Review the generated changelog before publishing, and consider using squash merges with sanitised commit messages on repositories where this is a concern.
