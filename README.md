# History Quiz — School Project

Simple browser quiz covering history questions from all continents (except Antarctica). Features:

- Continent selectors and difficulty levels (easy / medium / hard).
- Each question has 4 choices and exactly 1 correct answer.
- Results screen with score and breakdown by continent.

How to run locally

1. Serve the project directory over HTTP (browsers block `fetch()` on `file://`):

	 - Python 3 (PowerShell or CMD):

	 ```powershell
	 python -m http.server 8000
	 ```

	 Open: http://localhost:8000

	 - Node (one-time):

	 ```bash
	 npx http-server -p 8000
	 ```

	 - VS Code: install the Live Server extension and click *Go Live*.

Deployment (free static hosting)

- GitHub Pages
	1. Create a GitHub repository and push this project.
	2. Create a `main` branch (if needed), commit and push all files to GitHub.
	3. (Optional) Add the included GitHub Actions workflow to automatically deploy on push to `main`.
	4. On GitHub the site will be available at `https://<your-username>.github.io/<repo-name>/` within a minute of the first successful deploy.

Quick commands (replace values):

```powershell
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/<your-username>/<repo-name>.git
git push -u origin main
```

If you keep the workflow file (`.github/workflows/deploy.yml`) the site will deploy automatically after pushing to `main`.

Custom domain (optional)

 - To publish the site at your own domain (for example `play.historyquiz.example.com`):
	1. Add a DNS record at your domain registrar:
		- For subdomains (`play.example.com`) add a CNAME pointing to `<your-username>.github.io`.
		- For apex/root domains (example.com) use ALIAS/ANAME to point to `<your-username>.github.io`, or add the required A records from GitHub Pages documentation.
	2. Create a `CNAME` file in the repository root containing your domain (this repo includes a sample `CNAME` file).
	3. Push to `main`. GitHub Pages will serve the site at your custom domain after DNS and HTTPS provisioning complete.

Example: the included `CNAME` contains `play.historyquiz.example.com` as a placeholder — replace it with your domain before pushing.

Verify DNS (example with `nslookup`):

```powershell
nslookup -type=CNAME play.historyquiz.example.com
```

Note: DNS propagation and GitHub's HTTPS provisioning may take several minutes to a few hours the first time.

- Netlify
	1. Create a Netlify account and click *New site* → *Import from Git*.
	2. Connect your GitHub repo and deploy (build command: none, publish dir: `/`).

- Vercel
	1. Create a Vercel account and import your GitHub repo.
	2. Deploy using the defaults for a static site.

Notes

- The app fetches `data/questions.json` with a relative path (`data/questions.json`) — hosting as a static site will work without code changes.
- If you see an "Unable to load questions" alert when opening `index.html` directly, serve the folder as described above.
- For automatic deploys, connect your repo to Netlify or Vercel, or enable GitHub Pages from the repo settings.

Next steps I can implement for you

- Replace the `alert()` on fetch failure with a friendly in-page error banner and helpful buttons (e.g., "Run local server" instructions or "Open deployed site").
- Add a simple GitHub Actions workflow to auto-deploy to GitHub Pages.
