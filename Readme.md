# M365 Whisperer – Your Sarcastic Microsoft 365 Admin Chatbot 🤖

**M365 Whisperer** is a Gemini-powered Streamlit chatbot that acts as a **sarcastic, overworked IT admin**.
It specializes in **Microsoft 365 administration**, **device certification**, **MFA**, and **identity management**, helping IT professionals troubleshoot and automate tasks with a touch of humor.

---

## 🚀 Features

* Handles **Microsoft 365 tasks**:

  * Mailbox creation, deletion, and modification
  * Email forwarding control
  * MFA enable/disable
* Manages **device security**:

  * HENNGE One device certification registration & revocation
* Integrates with **enterprise tools**:

  * Active Directory / Entra ID
  * FortiClient VPN
  * Jump servers
  * Sync servers
* **Conversation memory** keeps context across multiple turns
* **Funny & sarcastic persona** makes IT support less boring
* **Loader spinner** while processing requests

---

## 🛠️ Tech Stack

* [Streamlit](https://streamlit.io) – Web UI
* [Google Gemini API](https://developers.generativeai.google/) – AI engine
* Python 3.11+
* [python-dotenv](https://pypi.org/project/python-dotenv/) – For local API key management

---

## 📁 Project Structure

```
m365_whisperer/
│
├── app.py                # Streamlit entry point
├── requirements.txt      # Python dependencies
├── .gitignore
└── README.md
```

---

## ⚡ Installation

1. Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/m365_whisperer.git
cd m365_whisperer
```

2. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Create a `.env` file:

```env
GEMINI_API_KEY=your_real_api_key_here
```

---

## 🏃 Run Locally

```bash
streamlit run app.py
```

---


## 📄 License

License – free to use and modify.
