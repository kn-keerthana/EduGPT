# 📋 Exact Commands Cheat Sheet

## Setting Up Git & GitHub (Do this once)

### Step 1: Install Git (if not installed)
Download from: https://git-scm.com/downloads
After installing, open a terminal and verify:
```
git --version
```

### Step 2: Configure Git with your name/email (once ever)
```
git config --global user.name "Your Name"
git config --global user.email "your-email@gmail.com"
```

---

## Pushing Your Project to GitHub

### Step 3: Go into your project folder
```
cd path/to/EduGPT_clean
```
(Replace "path/to" with wherever you saved this folder)

### Step 4: Initialize Git
```
git init
```

### Step 5: Add all files
```
git add .
```

### Step 6: Make your first commit
```
git commit -m "Initial commit: EduGPT with Groq + LLaMA 3.3"
```

### Step 7: Create repo on GitHub
1. Go to https://github.com
2. Click the "+" button (top right) → "New repository"
3. Name it: `EduGPT`
4. Set to Public
5. Do NOT check "Add a README" (we already have one)
6. Click "Create repository"
7. Copy the URL shown (looks like: https://github.com/kn-keerthana/EduGPT.git)

### Step 8: Connect and push
```
git remote add origin https://github.com/kn-keerthana/EduGPT.git
git branch -M main
git push -u origin main
```

---

## Deploying to Hugging Face Spaces (Free Hosting)

### Step 1: Create a Hugging Face account
Go to: https://huggingface.co/join

### Step 2: Create a new Space
1. Go to: https://huggingface.co/new-space
2. Space name: `EduGPT`
3. SDK: Select "Gradio"
4. Visibility: Public
5. Click "Create Space"

### Step 3: Add your Groq API key as a secret
1. In your Space, click "Settings" tab
2. Scroll to "Repository secrets"
3. Click "New secret"
4. Name: `GROQ_API_KEY`
5. Value: your actual Groq API key
6. Click "Add secret"

### Step 4: Push your code to the Space
```
git remote add space https://huggingface.co/spaces/kn-keerthana/EduGPT
git push space main
```

Your app will be live at: https://huggingface.co/spaces/kn-keerthana/EduGPT

---

## Common Commands Reference

| What you want to do | Command |
|---------------------|---------|
| See what's changed | `git status` |
| Save new changes | `git add . && git commit -m "Update: description"` |
| Push to GitHub | `git push` |
| Pull latest from GitHub | `git pull` |
