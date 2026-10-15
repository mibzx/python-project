# GitHub Upload Guide (Beginner)

## 1. Prepare the folder
Keep `README_FIRST.md`, `GITHUB_GUIDE.md`, and all six project folders together. Run each project before uploading and add screenshots you personally captured.

## 2. Create a repository
1. Sign in to GitHub.
2. Choose **New repository**.
3. Name it `mca-python-projects`.
4. Add a short description such as `MCA Python programming assignment projects`.
5. Choose Public only if your instructor permits public sharing; otherwise use Private.
6. Create the repository.

## 3. Upload using the website
For a small assignment, you can use **Add file → Upload files** and drag in project files. For larger uploads, use Git on your computer.

## 4. Upload using Git (optional)
Open a terminal in the main project folder and run:
```bash
git init
git add .
git commit -m "Add six MCA Python projects"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/mca-python-projects.git
git push -u origin main
```
Replace `YOUR-USERNAME` with your own GitHub username and use the repository URL shown by GitHub. If Git asks you to authenticate, follow GitHub's current sign-in instructions; do not paste a password or token into project files.

## 5. Before submission
- [ ] Run each standard-library project.
- [ ] Install requirements and run Customer Segmentation.
- [ ] Take screenshots of menus, sample operations, and generated charts.
- [ ] Personalise each report with your details and actual test observations.
- [ ] Check that no personal/private files or credentials are included.
- [ ] Confirm the repository opens and each README explains how to run the project.
- [ ] Be ready to explain the code and demonstrate it live.

## Common Windows commands
Check Python:
```powershell
py --version
```
Run a project:
```powershell
py main.py
```
Install ML dependencies:
```powershell
py -m pip install -r requirements.txt
```
