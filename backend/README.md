# MedNote Backend

FastAPI + SQLite backend that adds cloud sync to MedNote.
Deploy to Render free tier in under 5 minutes.

---

## Run Locally

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

Once running, visit `http://localhost:8000/docs` for the interactive API docs.

Then in your HTML file, update one line:
```js
window.MEDNOTE_API_BASE = "http://localhost:8000";
```

---

## Deploy to Render (Free, ~5 min)

### Step 1 — Push to GitHub
```bash
git init
git add .
git commit -m "initial commit"
git remote add origin https://github.com/your-username/mednote.git
git push -u origin main
```

### Step 2 — Connect to Render
1. Go to [render.com](https://render.com) → **New** → **Web Service**
2. Connect your GitHub account → select the `mednote` repo
3. Fill in the settings:

| Field | Value |
|---|---|
| Name | `mednote-api` |
| Environment | `Python 3` |
| Build Command | `pip install -r requirements.txt` |
| Start Command | `uvicorn main:app --host 0.0.0.0 --port $PORT` |

4. Click **Advanced** → **Add Environment Variable**:
   - Key: `DB_PATH`  →  Value: `/tmp/mednote.db`

5. Click **Create Web Service**

### Step 3 — Paste the URL into your HTML
Once deployed, Render gives you a URL like `https://mednote-api.onrender.com`.

Open your HTML file, find the `<script>` tag near the top, and set:
```js
window.MEDNOTE_API_BASE = "https://mednote-api.onrender.com";
```

Open the HTML file locally — it will now sync with the backend automatically.

---

## ⚠️ Render Free Tier — Known Limitations

| Issue | What happens | How it's handled |
|---|---|---|
| **Cold start** | Server sleeps after 15 min of inactivity → first request takes ~30s | HTML pings `/ping` every 10 min while the tab is open — keeps server awake during your demo |
| **DB resets on redeploy** | `/tmp/mednote.db` is wiped when Render redeploys | Fine for a hackathon demo. For persistence across deploys, add a Render Disk (mount at `/data`, set `DB_PATH=/data/mednote.db`) |

---

## API Reference

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/health` | Health check |
| `GET` | `/ping` | Keep-alive (prevents cold start during demo) |
| `POST` | `/api/user` | Create or get a user |
| `POST` | `/api/sync` | Push all visits + reminders |
| `GET` | `/api/records/{userId}` | Pull all visits + reminders |
| `POST` | `/api/visit` | Save a single visit |
| `DELETE` | `/api/visit/{userId}/{visitId}` | Delete a visit |
| `POST` | `/api/reminder` | Save a single reminder |
| `DELETE` | `/api/reminder/{userId}/{reminderId}` | Delete a reminder |

---

## Architecture

```
Browser (local HTML file)
  │
  ├─ On load:          GET  /api/records/{userId}   → pull saved data
  ├─ On data change:   POST /api/sync               → auto-save (1.5s debounce)
  └─ Every 10 min:     GET  /ping                   → prevent cold start
  │
  ▼
FastAPI  (Render free tier)
  │
  ▼
SQLite  (/tmp/mednote.db)
  ├── users
  ├── visits
  └── reminders
```

Users are identified by a random `userId` generated on first visit and stored in `localStorage` — no login required. Suitable for a hackathon demo; add JWT auth for production.
