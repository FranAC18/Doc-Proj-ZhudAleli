# Distillation and QA plan — ZA-ALC-GEN-001 v1.3 DOCX

- Source Markdown: `F:\Tesis\App Tesis\documentacion\alcance\alcance_v1.3_2026-10-13.md`.
- Source DOCX template: `F:\Tesis\App Tesis\analisis\2026-10-13\alcances-modulos\Formato Corregido.docx`.
- Template SHA-256: `B7DE3D0CAC94D4ADF6506A7235F04C0D99E9CAC272914228CAAF87BEDCA011E0`.
- Template visual baseline: 4 A4 portrait pages; one section; margins 0.70 in left/right, 0.65 in top, 0.60 in bottom; first page differs; cover wordmark and repeated floral mark in header; page-number field retained.
- Slot map: cover logo and header image retained from original DOCX; cover title/version updated; page 2 starts control metadata and revision history; remaining source Markdown headings, paragraphs, lists, and tables are converted in order; repeating header and footer remain from template.
- Brand tokens: forest green `#4C5B4A` for primary headings/table headers; natural cream `#F0EAC8` for header text and alternating rows; burgundy `#642138` for secondary headings/metadata labels; terracotta `#AC6E40` for table borders; Georgia serif headings; Heebo Light body (font substitution allowed by local Word rendering).
- Source of truth/status: Markdown v1.3 content and all pending review states are preserved. The Word copy does not approve the scope or change Sprint 1.
- Output: `F:\Tesis\App Tesis\documentacion\alcance\alcance_v1.3_2026-10-13.docx`.
- Visual gate: export final DOCX with Microsoft Word to PDF; render every page to PNG; inspect each page for brand assets, clipping, table splits, header/footer, page numbers, and legibility; adjust and repeat if needed.
- Structural gate: extract final text and confirm all Markdown headings and table rows are represented; confirm embedded images and page-number field remain; `git diff --check` scoped to any tracked index/control updates.
- Final QA: 7 A4 pages visually inspected; all 6 source tables and 10 section headings match the Markdown; 2 brand images and the PAGE field are present; palette and pending-review status verified; no trailing whitespace in the index/control record.
- Final DOCX SHA-256: `DA04B57ABB1E8387AA75C458B1D233F870ECEA71280014A3C9B85E625C693FC6`.
