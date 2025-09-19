
# AI Discharge Copilot 🚑

This is a **Streamlit-based AI tool** to assist hospital staff in managing and prioritizing patient discharges efficiently using simple heuristics, rules, and a knowledge base.

---

## 🔍 Project Overview

In hospitals, **delayed discharges** and inefficient **bed allocation** often create bottlenecks, increase patient waiting time, and burden staff. This project builds a **minimal viable prototype (MVP)** that can:

- 📥 Load and visualize patient records (1000+ entries)
- ✅ Check discharge readiness via rule-based logic
- 🛏️ Match patients with available beds
- 📚 Retrieve helpful context from a knowledge base
- 📊 Offer a clean dashboard UI for decisions

---

## 📁 Folder Structure

```
AI_Discharge_Copilot_Final/
├── app/
│   ├── app.py                 ← Streamlit main app
│   ├── utils.py               ← Logic for rules, loading, AI functions
├── data/
│   ├── patients.xlsx          ← 📊 1000 mock patients with 20+ fields
│   ├── beds.xlsx              ← 🛏️ (Optional) Bed info file
│   └── knowledge.txt          ← 📚 Reference material
├── README.md                  ← 📄 This file
├── requirements.txt           ← 🧪 Libraries to install
```

---

## ⚙️ How It Works

### Step 1: Upload Patient & Bed Data
- Loads the patient Excel file (`patients.xlsx`)
- Each row = 1 patient with demographic, medical & readiness data

### Step 2: Discharge Readiness Rules
- Runs a **simple rules engine** to check:
  - Stable vitals
  - Treatment complete
  - Doctor signed off
  - Family informed

### Step 3: Bed Allocation (Optional)
- If `beds.xlsx` is present, uses availability logic to assign

### Step 4: Contextual Retrieval (Optional)
- Uses text embeddings to retrieve guidance from `knowledge.txt`

### Step 5: Dashboard View
- Displays data tables and discharge-ready patients

---

## 🚀 Deployment Guide

1. ✅ Upload the entire zip (`AI_Discharge_Copilot_Final_ReadyToDeploy.zip`) to [Streamlit Cloud](https://share.streamlit.io/)
2. 🗂️ Unzip and ensure file structure is intact
3. ▶️ Set `app/app.py` as the entry point
4. 📄 Add secrets or environment configs if needed

---

## 🔧 Tech Stack

- Python 🐍 (Pandas, Numpy)
- Streamlit 🌐 (Dashboard + Hosting)
- OpenAI (Optional for embeddings)
- FAISS (Optional for semantic search)
- Excel / CSV data for patients and beds

---

## 🧠 Future Enhancements

- ✅ Doctor login + secure edit permissions
- ⏳ Predict length of stay
- 📱 WhatsApp / SMS alerts to families
- 📅 Discharge calendar view

---

## 📬 Questions?

Ping `@YourTeam` or reach out at [your-email@example.com](mailto:your-email@example.com)

