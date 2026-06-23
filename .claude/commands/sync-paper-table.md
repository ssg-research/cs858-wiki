---
description: Regenerate the reading-list tables in wiki/README.md from the spreadsheet
---

Sync the paper table in `wiki/README.md` to the current spreadsheet.

## Steps

1. **Regenerate.** Run:

   ```bash
   uv run python3 scripts/build-paper-table.py
   ```

   Capture the full stdout. The output begins with `### Part 1:` and ends with
   the closing `</table>` of Part 2.

2. **Identify the replacement zone.** In `wiki/README.md`, the zone to replace
   is the block that starts at the line `### Part 1: Risks to trustworthiness in ML`
   and ends at the closing `</table>` tag (just before the `<sup>&dagger;</sup>`
   footnote line). Do not touch anything outside this zone.

3. **Diff.** Compare the captured output to the current content of that zone.
   If there are no differences, report "No changes — table already up to date"
   and stop.

4. **Inject.** If there are differences, replace the zone with the new output
   exactly as printed by the script. Show the user a summary of what changed
   (which rows or cells differ).

5. **Lint and verify.**

   ```bash
   npx --no-install markdownlint-cli2 "wiki/README.md"
   uv run python3 scripts/check-links.py
   ```

   Both must report zero errors. Fix any issues before continuing.

6. **Stop.** Do not commit. Report what changed and wait for the user to approve
   a commit.
