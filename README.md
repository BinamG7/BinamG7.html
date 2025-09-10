<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Guragain Binam — Student Portfolio</title>
  <meta name="description" content="Student portfolio and landing page of Guragain Binam." />

  <!-- Google Font -->
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">

  <style>
    :root{--bg:#0f1724;--card:#0b1220;--accent:#3b82f6;--muted:#9aa4b2;--glass:rgba(255,255,255,0.04)}
    *{box-sizing:border-box}
    body{margin:0;font-family:'Inter',ui-sans-serif,system-ui,-apple-system,"Segoe UI",Roboto,'Helvetica Neue',Arial;color:#e6eef6;background:linear-gradient(180deg,#071025 0%, #071725 60%);-webkit-font-smoothing:antialiased}
    .container{max-width:980px;margin:36px auto;padding:28px}
    header{display:flex;align-items:center;gap:18px}
    .avatar{width:88px;height:88px;border-radius:16px;overflow:hidden;display:flex;align-items:center;justify-content:center;background:linear-gradient(135deg,#334155,#0ea5e9);border:2px solid var(--accent)}
    .avatar img{width:100%;height:100%;object-fit:cover;}
    h1{margin:0;font-size:26px}
    h2{font-size:20px;border-left:4px solid var(--accent);padding-left:10px;margin-bottom:10px}
    p.lead{margin:6px 0 0;color:var(--muted)}
    .card{background:var(--card);border-radius:14px;padding:20px;margin-top:20px;box-shadow:0 6px 18px rgba(2,6,23,0.6);transition: transform 0.3s ease, box-shadow 0.3s ease}
    .card:hover{transform: translateY(-4px); box-shadow: 0 10px 20px rgba(59,130,246,0.3);}
    .grid{display:grid;grid-template-columns:1fr 320px;gap:20px}@media(max-width:880px){.grid{grid-template-columns:1fr}}
    .section{margin-bottom:18px}
    .projects{display:grid;grid-template-columns:repeat(2,1fr);gap:14px}@media(max-width:640px){.projects{grid-template-columns:1fr}}
    .project{background:linear-gradient(135deg, rgba(11,18,32,0.8), rgba(11,18,32,0.95));padding:12px;border-radius:10px;transition: transform 0.3s ease, box-shadow 0.3s ease}
    .project:hover{transform: translateY(-4px); box-shadow: 0 10px 20px rgba(59,130,246,0.3);}
    .project h3{margin:0 0 6px;font-size:16px}
    .project p{margin:0;color:var(--muted);font-size:13px}
    .skills{display:flex;flex-wrap:wrap;gap:10px}
    .skill{background:rgba(255,255,255,0.03);padding:8px 12px;border-radius:999px;font-size:13px;color:var(--muted)}
    .experience{margin-top:18px}
    .exp-item{background:linear-gradient(135deg, rgba(11,18,32,0.8), rgba(11,18,32,0.95));padding:12px;border-radius:10px;margin-bottom:12px;transition: transform 0.3s ease, box-shadow 0.3s ease}
    .exp-item:hover{transform: translateY(-4px); box-shadow:0 10px 20px rgba(59,130,246,0.3);}
    .exp-item h3{margin:0;font-size:16px}
    .exp-item p{margin:4px 0 0;color:var(--muted);font-size:13px}
    aside .contact{display:flex;flex-direction:column;gap:10px}
    .btn{display:inline-block;padding:10px 14px;border-radius:10px;text-decoration:none;font-weight:600}
    .btn-primary{background:linear-gradient(90deg,var(--accent),#60a5fa);color:white;transition:all 0.3s ease}
    .btn-primary:hover{transform: translateY(-2px); box-shadow:0 6px 12px rgba(59,130,246,0.3);}
    .btn-ghost{background:transparent;border:1px solid rgba(255,255,255,0.06);color:var(--muted);transition:all 0.3s ease}
    .btn-ghost:hover{color:#60a5fa; border-color:#60a5fa; background:rgba(96,165,250,0.1);}
    footer{margin-top:28px;text-align:center;color:var(--muted);font-size:13px}
    .top-links{display:flex;gap:10px;flex-wrap:wrap}
    .meta{display:flex;gap:10px;color:var(--muted);font-size:13px;align-items:center}
    pre{background:#071226;color:#bcd8ff;padding:12px;border-radius:8px;overflow:auto}
  </style>
</head>
<body>
  <div class="container">
    <header>
      <div class="avatar" aria-hidden>
        <img src="binam_photo.jpg" alt="Guragain Binam">
      </div>
      <div>
        <h1>Guragain Binam — Student in Integrated Business Management</h1>
        <p class="lead">I am a student at Donga University, majoring in Integrated Business Management. Currently, I am in my second semester and actively building projects, practicing Python and Microsoft Office tools, and documenting what I learn here.</p>
        <div class="meta" style="margin-top:8px">
          <span>📍 Nepal</span><span>•</span>
          <span>📧 <a href="mailto:binamguragain788@gmail.com" style="color:inherit;text-decoration:underline">binamguragain788@gmail.com</a></span><span>•</span>
          <span>📱 010 2356 7789</span><span>•</span>
          <span>🆔 Student ID: 2518325</span>
        </div>
      </div>
    </header>

    <main class="card grid" role="main">
      <section>
        <div class="section">
          <h2 style="margin-top:0">About me</h2>
          <p>I am Guragain Binam, a second semester student of Integrated Business Management at Donga University. I enjoy coding in Python, creating small websites, and preparing school projects. This page is a short personal landing page to show my work and contact information.</p>
        </div>

        <div class="section">
          <h2>Projects & coursework</h2>
          <div class="projects">
            <article class="project">
              <h3>Project — Simple Python Calculator</h3>
              <p>Small console program that practices arithmetic operators and variables. (Chapter 03 exercises)</p>
              <p style="margin-top:8px"><a class="btn btn-ghost" href="https://github.com/BinamG7/simple-python-calculator" target="_blank">View code</a></p>
            </article>
            <article class="project">
              <h3>Portfolio Site (this page)</h3>
              <p>Single-file HTML portfolio hosted on GitHub Pages. Use it as a starting template and replace the placeholders.</p>
              <p style="margin-top:8px"><a class="btn btn-ghost" href="https://github.com/BinamG7/student-portfolio" target="_blank">Open live</a></p>
            </article>
            <article class="project">
              <h3>MS Office Practice Sheets</h3>
              <p>Word and Excel practice exercises — formatting, formulas and charts.</p>
            </article>
            <article class="project">
              <h3>Language: Korean Speaking Test</h3>
              <p>Audio practice and PDFs to help memorize Korean scripts.</p>
            </article>
          </div>
        </div>

        <div class="section">
          <h2>Skills</h2>
          <div class="skills">
            <div class="skill">Python (basics)</div>
            <div class="skill">HTML & CSS</div>
            <div class="skill">Git & GitHub</div>
            <div class="skill">MS Word / Excel / PowerPoint</div>
            <div class="skill">Korean (learning)</div>
          </div>
        </div>

        <div class="section experience">
          <h2>Experience</h2>
          <div class="exp-item">
            <h3>Basics of Computer Training</h3>
            <p>Completed a foundational training program covering essential computer skills, software usage, and digital literacy.</p>
          </div>
          <div class="exp-item">
            <h3>Business Management Internship</h3>
            <p>6-month internship experience in the field of Business Management, applying theoretical knowledge to real workplace practices and projects.</p>
          </div>
        </div>
      </section>

      <aside>
        <div class="card contact">
          <h3 style="margin-top:0">Contact & Links</h3>
          <div class="top-links">
            <a class="btn btn-primary" href="https://github.com/BinamG7" target="_blank" rel="noopener">GitHub</a>
          </div>
          <div style="margin-top:12px">
            <strong>Quick copy for GitHub Pages:</strong>
            <pre>Save this file as <code>index.html</code> and push to your repo root. Enable Pages in repo Settings &gt; Pages &gt; Branch: main &gt; / (root).</pre>
          </div>
          <div style="margin-top:8px">
            <strong>Contact:</strong>
            <address style="font-style:normal;color:var(--muted);margin-top:6px">binamguragain788@gmail.com<br/>📱 010 2356 7789<br/>🆔 Student ID: 2518325</address>
          </div>
        </div>
      </aside>
    </main>

    <footer>
      <div>© <span id="year"></span> Guragain Binam — Built with ❤️ • Hosted on GitHub Pages</div>
    </footer>
  </div>

  <script>
    document.getElementById('year').textContent = new Date().getFullYear();
  </script>
</body>
</html>
