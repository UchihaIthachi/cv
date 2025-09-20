require('dotenv').config();
const express = require('express');
const app = express();
const port = 3000;
const glob =require('glob');
const fs = require('fs');
const { exec } = require('child_process');
const session = require('express-session');
const passport = require('passport');
const GitHubStrategy = require('passport-github2').Strategy;

app.use(session({ secret: 'keyboard cat', resave: false, saveUninitialized: false }));
app.use(passport.initialize());
app.use(passport.session());

passport.serializeUser(function(user, done) {
  done(null, user);
});

passport.deserializeUser(function(obj, done) {
  done(null, obj);
});

passport.use(new GitHubStrategy({
    clientID: process.env.GITHUB_CLIENT_ID,
    clientSecret: process.env.GITHUB_CLIENT_SECRET,
    callbackURL: "http://localhost:3000/auth/github/callback"
  },
  function(accessToken, refreshToken, profile, done) {
    return done(null, profile);
  }
));

app.get('/auth/github', passport.authenticate('github', { scope: [ 'user:email' ] }));

app.get('/auth/github/callback',
  passport.authenticate('github', { failureRedirect: '/login' }),
  function(req, res) {
    res.redirect('/');
  });

app.get('/logout', function(req, res){
  req.logout();
  res.redirect('/');
});


app.use(express.static(__dirname));
app.use(express.json());

function ensureAuthenticated(req, res, next) {
  if (req.isAuthenticated()) { return next(); }
  res.redirect('/login')
}

app.get('/', ensureAuthenticated, (req, res) => {
  res.sendFile(__dirname + '/public/index.html');
});

app.get('/login', (req, res) => {
  res.sendFile(__dirname + '/public/login.html');
});

app.get('/api/user', (req, res) => {
  if (req.isAuthenticated()) {
    res.json({
      username: req.user.username,
      authorized_user: process.env.AUTHORIZED_USER
    });
  } else {
    res.json({
      username: null,
      authorized_user: process.env.AUTHORIZED_USER
    });
  }
});

app.get('/api/files', ensureAuthenticated, (req, res) => {
  glob('**/*.tex', (err, files) => {
    if (err) {
      res.status(500).send('Error reading files');
      return;
    }
    res.json(files);
  });
});

app.get('/api/file', ensureAuthenticated, (req, res) => {
  const filepath = req.query.path;
  fs.readFile(filepath, 'utf8', (err, data) => {
    if (err) {
      res.status(500).send('Error reading file');
      return;
    }
    res.send(data);
  });
});

app.post('/api/file', ensureAuthenticated, (req, res) => {
  if (req.user.username !== process.env.AUTHORIZED_USER) {
    return res.status(403).send('Forbidden');
  }
  const { path, content } = req.body;
  fs.writeFile(path, content, 'utf8', (err) => {
    if (err) {
      res.status(500).send('Error writing file');
      return;
    }
    res.send('File saved');
  });
});

function parseLogError(logContent) {
  const lines = logContent.split('\n');
  const errorLineIndex = lines.findIndex(line => line.startsWith('!'));

  if (errorLineIndex === -1) {
    return null;
  }

  const errorMessage = lines[errorLineIndex].substring(2);
  const lineInfo = lines[errorLineIndex + 1];
  const lineNumberMatch = lineInfo.match(/l\.(\d+)/);
  const lineNumber = lineNumberMatch ? parseInt(lineNumberMatch[1], 10) : null;

  let filePath = 'main.tex'; // Default to main.tex
  for (let i = errorLineIndex - 1; i >= 0; i--) {
    const match = lines[i].match(/\(([^)]+\.tex)/);
    if (match) {
      filePath = match[1];
      break;
    }
  }

  return {
    message: errorMessage,
    line: lineNumber,
    file: filePath
  };
}

app.post('/api/compile', ensureAuthenticated, (req, res) => {
  if (req.user.username !== process.env.AUTHORIZED_USER) {
    return res.status(403).send('Forbidden');
  }
  exec('xelatex -interaction=nonstopmode main.tex', (err, stdout, stderr) => {
    if (err) {
      fs.readFile('main.log', 'utf8', (logErr, logData) => {
        if (logErr) {
          return res.status(500).send('Error compiling LaTeX and could not read log file.');
        }
        const errorDetails = parseLogError(logData);
        if (errorDetails) {
          return res.status(400).json({ error: errorDetails });
        } else {
          return res.status(500).send('Error compiling LaTeX. Check logs.');
        }
      });
      return;
    }
    exec('xelatex -interaction=nonstopmode main.tex', (err, stdout, stderr) => {
      if (err) {
        // Even the second run can fail, so we should probably parse the log here too.
        // For now, keeping it simple.
        res.status(500).send('Error on second LaTeX compilation pass.');
        return;
      }
      res.json({ success: true });
    });
  });
});

app.listen(port, () => {
  console.log(`Server listening at http://localhost:${port}`);
});
