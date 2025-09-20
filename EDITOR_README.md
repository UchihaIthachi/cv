# Web-based LaTeX Editor

This is a web-based LaTeX editor for your CV project.

## How to run the application

1. **Install dependencies:**
   ```bash
   npm install
   ```

2. **Set up GitHub authentication:**
   - Go to your GitHub account settings -> Developer settings -> OAuth Apps.
   - Create a new OAuth App.
   - Set the "Homepage URL" to `http://localhost:3000`.
   - Set the "Authorization callback URL" to `http://localhost:3000/auth/github/callback`.
   - You will get a "Client ID" and a "Client Secret".
   - Create a `.env` file in the root of the project and add the following lines:
     ```
     GITHUB_CLIENT_ID=YOUR_CLIENT_ID
     GITHUB_CLIENT_SECRET=YOUR_CLIENT_SECRET
     AUTHORIZED_USER=UchihaIthachi
     ```
     Replace `YOUR_CLIENT_ID` and `YOUR_CLIENT_SECRET` with the values you obtained. You can also change the `AUTHORIZED_USER` to any GitHub username.
   - The application uses the `dotenv` package to load these environment variables, which is already included in the dependencies.

3. **Install LaTeX dependencies:**
   The application uses `xelatex` to compile the LaTeX project. You need to have a working TeX Live installation.
   On a Debian-based system (like Ubuntu), you can install the necessary packages with:
   ```bash
   sudo apt-get update
   sudo apt-get install -y texlive-xetex texlive-fonts-extra texlive-latex-extra
   ```

4. **Run the application:**
   ```bash
   npm start
   ```
   Or for development with automatic restart:
   ```bash
   npm run dev
   ```

5. **Open the editor:**
   Open your browser and go to `http://localhost:3000`. You will be redirected to the login page. Log in with your GitHub account.

## How it works

- The application is a Node.js/Express server.
- It provides a web interface with a code editor (CodeMirror) to edit the `.tex` files.
- It uses Passport.js with the `passport-github2` strategy for GitHub authentication.
- Editing is restricted to the GitHub user `UchihaIthachi`. Other users have read-only access.
- The "Compile" button runs `xelatex` on the server to generate the `main.pdf` file, which is then displayed in the browser.
