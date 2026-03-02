import re

NAV = """    <nav>
        <div class="nav-container">
            <a href="index.html" class="nav-brand">Nguyen Son</a>
            <div class="nav-links" id="navLinks">
                <a href="index.html">Home</a>
                <a href="publications.html">Publications</a>
                <a href="teaching.html">Teaching</a>
                <a href="talks.html">Talks</a>
                <a href="projects.html">Projects</a>
                <a href="blog.html">Blog</a>
                <a href="files/resume_sonnguyen.pdf" class="nav-cv" target="_blank">CV ↗</a>
            </div>
            <button class="mobile-menu-btn" id="menuBtn">
                <span></span>
                <span></span>
            </button>
        </div>
    </nav>"""

SIDEBAR = """        <aside class="sidebar reveal">
            <img src="img/avt2.jpg" alt="Nguyen Manh Son" class="profile-img">
            <div>
                <p class="sidebar-name">Nguyen Manh Son</p>
                <div class="sidebar-meta">
                    <p><strong>University of Science</strong></p>
                    <p>Vietnam National University</p>
                    <p>Undergraduate · GTA</p>
                    <p>Hanoi, Vietnam</p>
                </div>
                <span class="sidebar-badge">Young Scientist 2026</span>
                <p class="sidebar-section-label">Connect</p>
                <div class="social-links">
                    <a href="https://github.com/rssonnm" class="social-icon">
                        <span class="social-icon-dot"></span>
                        <span>GitHub / rssonnm</span>
                    </a>
                    <a href="https://x.com/sonmchems" class="social-icon">
                        <span class="social-icon-dot"></span>
                        <span>X / sonmchems</span>
                    </a>
                    <a href="https://scholar.google.com/citations?user=RpLurfYAAAAJ&hl=vi" class="social-icon">
                        <span class="social-icon-dot"></span>
                        <span>Google Scholar</span>
                    </a>
                </div>
            </div>
        </aside>"""

FONTS = '    <link href="https://fonts.googleapis.com/css2?family=Syne:wght@400;500;600;700;800&family=Inter:wght@300;400;500;600;700&family=DM+Serif+Display:ital@0;1&display=swap" rel="stylesheet">'

# --- teaching.html ---
teaching = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Teaching — Nguyen Manh Son</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
""" + FONTS + """
    <link rel="stylesheet" href="styles.css">
    <link rel="icon" type="image/x-icon" href="icon.ico">
</head>
<body>
    <canvas id="bg-canvas"></canvas>
""" + NAV + """
    <div class="container">
""" + SIDEBAR + """
        <main class="main-content">
            <section class="reveal">
                <h1>Teaching</h1>
                <div class="accent-line"></div>
                <p>I serve as both a Graduate and Undergraduate Teaching Assistant at the University of Science, VNU, focusing on the application of statistics and machine learning to chemical analysis.</p>

                <h2>Graduate Teaching Assistant</h2>
                <div class="teaching-list">
                    <div class="teaching-item">
                        <span class="teaching-code">CH35</span>
                        <span>Statistics and Applied Mathematics for Chemistry <em>(2025)</em></span>
                    </div>
                    <div class="teaching-item">
                        <span class="teaching-code">CH34</span>
                        <span>Chemometrics in Analytical Chemistry <em>(2024)</em></span>
                    </div>
                    <div class="teaching-item">
                        <span class="teaching-code">CH34</span>
                        <span>Statistics and Applied Mathematics for Chemistry <em>(2024)</em></span>
                    </div>
                    <div class="teaching-item">
                        <span class="teaching-code">CH33</span>
                        <span>Statistics and Applied Mathematics for Chemistry <em>(2023)</em></span>
                    </div>
                </div>

                <h2 style="margin-top:3rem;">Undergraduate Teaching Assistant</h2>
                <div class="teaching-list">
                    <div class="teaching-item">
                        <span class="teaching-code">CHE2116</span>
                        <span>Analytical Chemistry <em>(2025)</em></span>
                    </div>
                    <div class="teaching-item">
                        <span class="teaching-code">CHE2129</span>
                        <span>Advanced Analytical Chemistry <em>(2025)</em></span>
                    </div>
                    <div class="teaching-item">
                        <span class="teaching-code">CHE2129</span>
                        <span>Advanced Analytical Chemistry <em>(2024)</em></span>
                    </div>
                </div>
            </section>
        </main>
    </div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script src="scripts.js"></script>
</body>
</html>"""

with open('teaching.html', 'w') as f:
    f.write(teaching)
print("teaching.html done")

# --- talks.html ---
talks = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Talks — Nguyen Manh Son</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
""" + FONTS + """
    <link rel="stylesheet" href="styles.css">
    <link rel="icon" type="image/x-icon" href="icon.ico">
</head>
<body>
    <canvas id="bg-canvas"></canvas>
""" + NAV + """
    <div class="container">
""" + SIDEBAR + """
        <main class="main-content">
            <section class="reveal">
                <h1>Talks &amp; Outreach</h1>
                <div class="accent-line"></div>
                <h3>2025</h3>
                <div class="talk-card">
                    <div class="pub-title">Molecular Modeling for Drug Discovery</div>
                    <div class="pub-authors" style="margin-top:0.4rem;">Traphaco JSC, 2025</div>
                </div>
                <div class="talk-card">
                    <div class="pub-title">Artificial Intelligence for Drug Discovery</div>
                    <div class="pub-authors" style="margin-top:0.4rem;">Traphaco JSC, 2025</div>
                </div>
                <div class="talk-card">
                    <div class="pub-title">Application of Explainable AI in Personalized Nutrition</div>
                    <div class="pub-authors" style="margin-top:0.4rem;">International Conference on Chemical and Microbiological Risk Assessment for Food Safety, 2025</div>
                </div>

                <h2 style="margin-top:3rem;">Outreach</h2>
                <ul class="awards-list">
                    <li><span class="award-icon">🧪</span><span><b>HUS Chemistry Club</b> — Member of the Board of Directors, VNU Hanoi University of Science</span></li>
                    <li><span class="award-icon">🐾</span><span><b>The Dilittles Project</b> — Animal Rescue Project</span></li>
                    <li><span class="award-icon">🌐</span><span><b>International Language Club</b></span></li>
                </ul>
            </section>
        </main>
    </div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script src="scripts.js"></script>
</body>
</html>"""

with open('talks.html', 'w') as f:
    f.write(talks)
print("talks.html done")

# --- projects.html ---
projects = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Projects — Nguyen Manh Son</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
""" + FONTS + """
    <link rel="stylesheet" href="styles.css">
    <link rel="icon" type="image/x-icon" href="icon.ico">
</head>
<body>
    <canvas id="bg-canvas"></canvas>
""" + NAV + """
    <div class="container">
""" + SIDEBAR + """
        <main class="main-content">
            <section class="reveal">
                <h1>Research Projects</h1>
                <div class="accent-line"></div>
                <p>A selection of research projects spanning quantum machine learning, computational chemistry, and AI-driven food science.</p>

                <h3>Active</h3>
                <div class="project-card">
                    <div class="pub-title">Quantum Graph Flow Matching (QGFM)</div>
                    <div class="pub-authors" style="margin-top:0.4rem;margin-bottom:0.75rem;">
                        Developing quantum-enhanced generative models for molecular design using variational quantum circuits and continuous normalizing flows on graph structures.
                    </div>
                    <div class="skills-grid">
                        <span class="skill-tag">Quantum ML</span>
                        <span class="skill-tag">Graph ML</span>
                        <span class="skill-tag">Flow Matching</span>
                        <span class="skill-tag">JAX</span>
                    </div>
                </div>

                <div class="project-card">
                    <div class="pub-title">AI for Herbal Medicine Quality Control</div>
                    <div class="pub-authors" style="margin-top:0.4rem;margin-bottom:0.75rem;">
                        Multi-omics integration and spectral fingerprinting (FTIR, HPLC, UV-Vis) with machine learning for authentication and quality grading of traditional Vietnamese herbal medicines.
                    </div>
                    <div class="skills-grid">
                        <span class="skill-tag">Chemometrics</span>
                        <span class="skill-tag">Deep Learning</span>
                        <span class="skill-tag">Python</span>
                    </div>
                </div>

                <h3>Past</h3>
                <div class="project-card">
                    <div class="pub-title">Metabolomics Study of Peliosanthes micrantha</div>
                    <div class="pub-authors" style="margin-top:0.4rem;margin-bottom:0.75rem;">
                        UHPLC-QTOF-MS based metabolomics, cytotoxicity against HT29 cells (colon cancer cell line) and molecular docking for rhizome extracts. Conducted at VAST BioChemistry Lab.
                    </div>
                    <div class="skills-grid">
                        <span class="skill-tag">Metabolomics</span>
                        <span class="skill-tag">Molecular Docking</span>
                        <span class="skill-tag">VAST</span>
                    </div>
                </div>

                <div class="project-card">
                    <div class="pub-title">Deep Learning for Vietnamese Orange Quality</div>
                    <div class="pub-authors" style="margin-top:0.4rem;margin-bottom:0.75rem;">
                        Non-destructive prediction of citrus sweetness using computer vision and deep neural networks. Achieved real-time inference for farm-to-fork supply chain applications.
                    </div>
                    <div class="skills-grid">
                        <span class="skill-tag">Computer Vision</span>
                        <span class="skill-tag">PyTorch</span>
                        <span class="skill-tag">IoT</span>
                    </div>
                </div>
            </section>
        </main>
    </div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script src="scripts.js"></script>
</body>
</html>"""

with open('projects.html', 'w') as f:
    f.write(projects)
print("projects.html done")

