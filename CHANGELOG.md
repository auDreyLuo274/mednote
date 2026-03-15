# Changelog

All notable changes to MedNote are documented here.

---

## [v1.2.0] — 2025

### Added
- Custom SVG heart-notebook logo replacing placeholder icon
- "Hello, [Name]" greeting moved to header position for cleaner layout

### Fixed
- White screen crash caused by undefined `tr` variable references in `T_EXTRA` translation object
- AI-extracted reminder items now output in the user's selected language (previously always English)
- Notification modal buttons ("Add item", "Confirm & save", "Skip") now use translation keys
- "Reminder" type badge in calendar now uses translated string
- Visit card title "New Recording" now respects selected language
- Timestamps on visit cards now use locale-appropriate formatting

---

## [v1.1.0] — 2025

### Added
- 10-language support: EN, 中文, FR, DE, 日本語, 한국어, ES, हिंदी, Tiếng Việt, العربية
- AI chat assistant powered by Groq Llama 3.3 / Gemini
- Calendar export to Google Calendar, Apple Calendar (.ics), and Outlook
- Document upload (PDF + images) with Gemini-powered extraction
- Elder mode with larger fonts and simplified navigation
- Dark / light theme toggle
- Live speech-to-text via Web Speech API
- Groq Whisper audio transcription

### Changed
- Dual layout: `RecallMD_web.html` (desktop sidebar) and `RecallMD_v12.html` (mobile tab bar)

---

## [v1.0.0] — 2025

### Initial Release
- Record doctor visits with live transcription
- AI-powered visit summaries (Findings, Medications, Watch-for, Next Steps)
- Medication and appointment extraction into reminder schedule
- Provisional item review and confirmation flow
- LocalStorage persistence — no backend required
