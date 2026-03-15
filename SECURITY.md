# Security Policy

## Data & Privacy

MedNote is designed with privacy as a core principle:

- **No backend server** — all data is processed and stored in your browser only
- **No analytics or tracking** — zero telemetry, no third-party tracking scripts
- **API keys stay local** — keys are stored in `localStorage` and sent only directly to Groq/Gemini APIs from your browser
- **Audio is not stored externally** — audio blobs are held in memory temporarily and never uploaded to any server other than the transcription API you choose

## API Key Security

Your Groq and Gemini API keys are:
- Stored only in `localStorage` on your device
- Never logged or transmitted to any MedNote-controlled server (there is none)
- Sent directly from your browser to the respective API endpoints (api.groq.com, generativelanguage.googleapis.com)

**Recommendation:** Use API keys with restricted permissions where possible, and rotate them periodically.

## Reporting a Vulnerability

If you discover a security issue, please open a [GitHub issue](../../issues) with the label `security`. For sensitive disclosures, describe the issue without including exploit details publicly, and we will follow up.
