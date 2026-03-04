# Azure VM FastAPI Deployment (Mini Project Notes)

## 1️⃣ Fix SSH Key Permission Issue (Windows)

Problem:

```
WARNING: UNPROTECTED PRIVATE KEY FILE!
Permissions are too open.
```

Reason:
Windows gives extra users access to the .pem file. SSH requires private key to be readable only by the owner.

Fix Commands:

```powershell
icacls .\vm-fastapi-test-app_key.pem /inheritance:r
icacls .\vm-fastapi-test-app_key.pem /grant:r "$($env:USERNAME):(R)"
```

---

## 2️⃣ Create Azure VM

* Used Free Tier
* Selected Ubuntu image
* Region: Central India
* Generated SSH key pair
* Downloaded `.pem` file

---

## 3️⃣ Connect to VM Using SSH

Command:

```powershell
ssh -i key.pem azureuser@<public-ip>
```

Disconnect from VM:

```bash
exit
```

or press `CTRL + D`

---

## 4️⃣ Update Ubuntu Packages

Update package list:

```bash
sudo apt update
```

Explanation:
`apt` = Advanced Package Tool (Ubuntu package manager)

Upgrade installed software:

```bash
sudo apt upgrade -y
```

---

## 5️⃣ Install Python

```bash
sudo apt install python3 -y
sudo apt install python3-pip -y
```

Optional (make `python` command work):

```bash
sudo apt install python-is-python3 -y
```

Verify:

```bash
python --version
pip --version
```

---

## 6️⃣ Install Nginx

```bash
sudo apt install nginx -y
```

Check status:

```bash
sudo systemctl status nginx
```

Important Nginx Commands:

```bash
sudo systemctl start nginx
sudo systemctl stop nginx
sudo systemctl restart nginx
sudo systemctl status nginx
sudo systemctl enable nginx
```

Test in browser:

```
http://<public-ip>
```

---

## 7️⃣ Clone Repository Inside VM

Create folder and move into it:

```bash
mkdir codes
cd codes
```

Clone repo:

```bash
git clone <repo-url>
cd <repo-folder>
```

---

## 8️⃣ Virtual Environment Setup (Linux Way)

Important:
Do NOT use Windows venv (`Scripts/activate`).
Linux uses `bin/activate`.

Create venv:

```bash
python -m venv testApp
```

Activate:

```bash
source testApp/bin/activate
```

Verify:

```bash
which python
```

---

## 9️⃣ Install Application Dependencies

If `requirements.txt` exists:

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install fastapi uvicorn gunicorn
```

---

## 🔟 Run FastAPI Application (Development Test)

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

Access in browser:

```
http://<public-ip>:8000
```

Common Issue:
Port 8000 blocked in Azure → Need inbound rule for port 8000.

---

## 1️⃣1️⃣ Production Setup (Gunicorn + Nginx)

Run with Gunicorn:

```bash
gunicorn -k uvicorn.workers.UvicornWorker main:app --bind 127.0.0.1:8000
```

Edit Nginx config:

```bash
sudo nano /etc/nginx/sites-available/default
```

Inside `location /` block:

```
proxy_pass http://127.0.0.1:8000;
proxy_set_header Host $host;
proxy_set_header X-Real-IP $remote_addr;
```

Restart Nginx:

```bash
sudo systemctl restart nginx
```

Now access:

```
http://<public-ip>
```

---

# ✅ Architecture Built

Browser
↓
Nginx (Port 80)
↓
Gunicorn (127.0.0.1:8000)
↓
FastAPI App

---

# 🚨 Problems Encountered

1. SSH key permission error (fixed using icacls)
2. Windows virtual environment pushed to GitHub (OS mismatch)
3. Port 8000 not accessible (Azure NSG rule missing)
4. Binding to 127.0.0.1 instead of 0.0.0.0 during testing

---

# 🎯 Outcome

* Successfully created Azure VM
* Connected using SSH key authentication
* Installed Python and Nginx
* Cloned FastAPI project
* Configured virtual environment correctly (Linux)
* Ran app with Uvicorn (dev)
* Prepared production structure using Gunicorn + Nginx
