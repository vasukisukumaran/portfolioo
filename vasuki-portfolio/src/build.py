"""Render the complete, progressively enhanced portfolio with no build dependencies."""

import os
from datetime import date
from html import escape
from pathlib import Path

from content import EDUCATION, EXPERTISE, PROJECTS, STUDIES, TRAINING
from graphics import icon, photo_overlay

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT if (ROOT / "site.css").is_file() else ROOT / "dist"
ASSETS = OUT / "assets"
ORIGIN = os.environ.get("PORTFOLIO_ORIGIN", "").rstrip("/")
YEAR = date.today().year
NAV = ["Home", "About", "Projects", "Expertise", "Experience", "Contact"]
EMAIL = "vasukisukumaran@gmail.com"
PHONE = "+91 9944741852"
GITHUB = "https://github.com/vasukisukumaran"
LINKEDIN = "https://linkedin.com/in/vasuki-a-s-3389b7339"


def head(title, description, prefix="", route="", home=False):
    canonical = f'<link rel="canonical" href="{escape(ORIGIN + "/" + route)}">' if ORIGIN else ""
    hero_preload = '<link rel="preload" as="image" href="assets/hero-sculpture.webp" fetchpriority="high">' if home else ""
    return f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="#2c2b30">
  <title>{escape(title)}</title>
  <meta name="description" content="{escape(description, quote=True)}">
  <meta property="og:type" content="website">
  <meta property="og:title" content="{escape(title, quote=True)}">
  <meta property="og:description" content="{escape(description, quote=True)}">
  {canonical}
  <link rel="icon" href="{prefix}assets/monogram.svg" type="image/svg+xml">
  <link rel="preload" href="{prefix}assets/inter.woff2" as="font" type="font/woff2" crossorigin>
  {hero_preload}
  <link rel="stylesheet" href="{prefix}site.css">
  <script src="{prefix}site.js" defer></script>
</head>'''


def brand(href):
    return f'<a class="wordmark" href="{href}" aria-label="Vasuki A.S. home">V.A.S<span>.</span></a>'


def header(prefix="", detail=False):
    base = f"{prefix}index.html" if detail else ""
    active = "projects" if detail else "home"
    items = []
    for label in NAV:
        target = label.lower()
        current = ' aria-current="location"' if target == active else ""
        items.append(f'<a href="{base}#{target}" data-section="{target}"{current}>{label}</a>')
    return f'''
<a class="skip-link" href="#main">Skip to content</a>
<header class="site-header">
  <div class="wrap header-inner">
    {brand(base + "#home")}
    <nav class="main-nav" id="main-nav" aria-label="Main navigation">{"".join(items)}</nav>
    <a class="availability" href="{base}#contact" aria-label="Available for opportunities. Contact Vasuki"><span aria-hidden="true"></span>Available</a>
    <button type="button" class="menu-toggle" aria-controls="main-nav" aria-expanded="false" aria-label="Open navigation">
      <span class="menu-symbol" aria-hidden="true"><i></i><i></i></span><span class="menu-label">Menu</span>
    </button>
  </div>
</header>'''


def kicker(label):
    return f'<p class="kicker">{escape(label)}</p>'


def footer(prefix=""):
    home = f"{prefix}index.html#home" if prefix else "#home"
    return f'''
<footer class="site-footer dark">
  <div class="wrap footer-inner">{brand(home)}
    <p>Designed with intention. Built with curiosity.</p>
    <small>© {YEAR} Vasuki A.S.</small>
    <a href="{home}" class="back-top" aria-label="Back to home">{icon("up")}</a>
  </div>
</footer>'''


def hero():
    return f'''
<section class="hero dark" id="home" data-nav="home" aria-labelledby="hero-title">
  <div class="hero-stage">
    <div class="hero-art" aria-hidden="true">
      <img class="hero-art-img" src="assets/hero-sculpture.webp" width="1440" height="1229" alt="" fetchpriority="high">
    </div>
    <div class="wrap hero-inner">
      <div class="hero-copy">
        <p class="eyebrow hero-byline"><b>Vasuki A.S.</b><span class="slash">/</span><span>AI &amp; Software Engineering</span></p>
        <h1 id="hero-title" class="display hero-title"><span>Intelligence</span><span>meets</span><span>engineering<span class="accent">.</span></span></h1>
        <p class="hero-deck">Exploring the intersection of artificial intelligence, software engineering, and meaningful digital experiences.</p>
        <div class="actions"><a class="button primary" href="#projects">Explore projects {icon("arrow")}</a><a class="button ghost" href="#about">About me</a></div>
      </div>
    </div>
    <div class="wrap hero-foot">
      <div class="section-counter" aria-label="Section 1 of 6"><b>01</b><span>/</span><span>06</span><i aria-hidden="true"></i></div>
      <a href="#about" class="scroll-cue">Scroll {icon("down")}</a>
    </div>
  </div>
</section>'''


def about():
    return f'''
<section class="section paper about-section" id="about" data-nav="about" aria-labelledby="about-title">
  <div class="wrap">
    <div class="about-grid">
      <div class="about-copy">
        {kicker("About")}
        <h2 class="display section-title" id="about-title" data-reveal>Curious by<br>nature. Built<br>to explore.</h2>
        <div class="bio">
          <p>I’m Vasuki, a third-year engineering student at PSNA College of Engineering and Technology, specializing in artificial intelligence and machine learning.</p>
          <p>I like taking an everyday problem and building something people can use. That interest draws me to full-stack development, intelligent systems, and the details that make software feel intuitive.</p>
        </div>
      </div>
      <figure class="architecture" aria-label="Architectural study in concrete and coral">
        <div class="architecture-sun"></div>
        <img src="assets/about-architecture.svg" class="architecture-image" alt="An angular, cantilevered concrete building against a coral sun." width="800" height="680" loading="lazy" decoding="async">
        <span class="architectural-rule" aria-hidden="true"></span>
      </figure>
    </div>
    <dl class="bio-facts">
      <div><dt>Location</dt><dd>Madurai, India</dd></div>
      <div><dt>Education</dt><dd>B.E. Artificial Intelligence and Machine Learning</dd></div>
      <div><dt>Institution</dt><dd>PSNA College of Engineering and Technology</dd></div>
      <div><dt>Current status</dt><dd>Third year</dd></div>
    </dl>
  </div>
</section>'''


def tags(technologies):
    return '<ul class="tech-list" aria-label="Technologies">' + "".join(f"<li>{escape(name)}</li>" for name in technologies) + "</ul>"


def plate(project, number, prefix="", eager=False):
    key = project["plate"]
    photo = key in {"farm", "city", "parking"}
    if photo:
        filename = f"{key}.webp" if (ASSETS / f"{key}.webp").is_file() else f"scene-{key}.svg"
    else:
        filename = f"project-{key}.svg"
    overlay = photo_overlay(key) if photo else ""
    priority = 'fetchpriority="high"' if eager else 'loading="lazy" decoding="async"'
    return f'''
<figure class="project-plate plate-{key}">
  <div class="plate-art">
    <img class="scene-image" src="{prefix}assets/{filename}" alt="{escape(project["alt"], quote=True)}" width="800" height="500" {priority}>
    {overlay}
  </div>
  <span class="plate-index" aria-hidden="true">{number:02}</span>
  <figcaption><span class="plate-mark" aria-hidden="true"></span>Concept illustration<span class="plate-divider">/</span>{escape(project["caption"])}</figcaption>
</figure>'''


def project_row(project, number):
    href = f'projects/{project["slug"]}.html'
    return f'''
<article class="project-row" id="work-{project["slug"]}" aria-labelledby="title-{project["slug"]}">
  {plate(project, number)}
  <div class="project-copy">
    <p class="eyebrow project-category"><span class="sr-only">Project {number}. </span>{escape(project["category"])}</p>
    <h3 id="title-{project["slug"]}"><a href="{href}">{escape(project["title"])}</a></h3>
    <p class="project-subtitle">{escape(project["subtitle"])}</p>
    <p class="project-summary">{escape(project["summary"])}</p>
    {tags(project["stack"])}
    <a class="text-link" href="{href}" aria-label="Read the {escape(project["title"])} project brief">Read project brief {icon("north-east")}</a>
  </div>
</article>'''


def projects():
    return f'''
<section id="projects" data-nav="projects" aria-labelledby="work-title">
  <div class="work-intro dark">
    <div class="wrap">{kicker("Projects")}
      <div class="section-heading"><h2 class="display section-title" id="work-title" data-reveal>Selected work.<br>Thoughtfully built.</h2>
        <p>Five projects exploring software engineering, intelligent systems, and practical problem-solving.</p>
      </div>
    </div>
  </div>
  <div class="project-ledger paper"><div class="wrap">{"".join(project_row(p, i) for i, p in enumerate(PROJECTS, 1))}</div></div>
</section>'''


def expertise():
    grid = "".join(
        f'<div class="skill">{icon(symbol)}<h3>{escape(label)}</h3><p>{escape(skills)}</p></div>'
        for symbol, label, skills in EXPERTISE
    )
    return f'''
<section class="section expertise dark" id="expertise" data-nav="expertise" aria-labelledby="expertise-title">
  <div class="wrap">
    {kicker("Expertise")}
    <div class="section-heading"><h2 class="display section-title" id="expertise-title" data-reveal>The tools.<br>The thinking.<br>The execution.</h2>
    <p>From writing a first line of Python to connecting a Spring Boot application to a database, these are the skills I work with.</p></div>
    <div class="skills-grid">{grid}</div>
  </div>
</section>'''


def background():
    edu = "".join(f'<li><span class="timeline-year">{escape(year)}</span><div><h4>{escape(title)}</h4><p>{escape(school)}</p><span class="grade">{escape(grade)}</span></div></li>' for year, title, school, grade in EDUCATION)
    train = "".join(f'<li><span class="timeline-year">{escape(year)}</span><ul class="courses">' + "".join(f'<li>{escape(course)}</li>' for course in courses) + '</ul></li>' for year, courses in TRAINING)
    return f'''
<section class="section experience paper" id="experience" data-nav="experience" aria-labelledby="experience-title">
  <div class="wrap">
    {kicker("Experience")}
    <div class="internship-row">
      <h2 class="display section-title" id="experience-title" data-reveal>Where learning<br>becomes practice.</h2>
      <div class="internship"><span class="icon-disc">{icon("briefcase")}</span><div>
        <p class="eyebrow">Internship</p><h3>Python Chatbot Development Internship</h3><p class="org">Livewire <span>·</span> Madurai, India</p>
        <p>Completed an internship focused on chatbot development using Python.</p>
      </div></div>
    </div>
    <div class="academic-grid">
      <section aria-labelledby="education-title">
        {kicker("Education")}<h3 class="display subheading" id="education-title">The foundation.</h3>
        <ol class="timeline">{edu}</ol>
        <p class="languages"><b>Languages</b> Tamil and English, spoken and written.</p>
      </section>
      <section aria-labelledby="training-title">
        {kicker("Certifications & training")}<h3 class="display subheading" id="training-title">Continuously expanding<br>the horizon.</h3>
        <ol class="timeline training-list">{train}</ol>
      </section>
    </div>
  </div>
</section>'''


def exploration():
    figures = []
    for n, (slug, name, caption) in enumerate(STUDIES):
        figures.append(f'''
      <figure class="study">
        <a class="study-open" href="assets/study-{slug}.svg" data-study="{n}" aria-label="Enlarge the {escape(name)} study" aria-haspopup="dialog">
          <img src="assets/study-{slug}.svg" alt="{escape(caption, quote=True)}" width="800" height="500" loading="lazy" decoding="async">
          <span class="study-expand">{icon("expand")}</span>
        </a>
        <figcaption>{escape(name)}</figcaption><p class="sr-only study-description">{escape(caption)}</p>
      </figure>''')
    return f'''
<section class="section exploration dark" aria-labelledby="explore-title" data-nav="experience">
  <div class="wrap">{kicker("Visual explorations")}
    <div class="section-heading"><h2 class="display section-title" id="explore-title" data-reveal>Beyond the<br>defined.</h2>
    <p>Three visual studies in volume, repetition, and light. A space to play with the forms that run through this portfolio.</p></div>
    <div class="studies">{"".join(figures)}</div>
  </div>
</section>
<dialog class="study-dialog" id="study-dialog" aria-labelledby="study-dialog-title">
  <div class="dialog-bar"><p class="eyebrow">Visual exploration</p><button class="dialog-close" type="button" aria-label="Close enlarged study">{icon("close")}</button></div>
  <img class="dialog-image" src="assets/study-volume.svg" alt="" width="800" height="500" loading="lazy">
  <div class="dialog-copy"><div><h2 id="study-dialog-title"></h2><p class="dialog-description"></p></div>
    <div class="dialog-controls"><button type="button" class="prev-study" aria-label="Previous study">{icon("back")}</button><button type="button" class="next-study" aria-label="Next study">{icon("arrow")}</button></div>
  </div>
</dialog>'''


def philosophy():
    return '''
<section class="philosophy paper" data-nav="experience" aria-label="Personal philosophy">
  <div class="wrap quote-grid">
    <blockquote><span class="quote-mark" aria-hidden="true">“</span><p>Good technology<br>solves problems.<br><em>Great design<br>makes it matter.</em></p></blockquote>
    <p class="reflection">I learn by building something, trying it, and finding the part that could work better. That habit keeps me curious about emerging technologies and the people who will use them.</p>
  </div>
</section>'''


def contact():
    def line(symbol, label, url=None, external=False):
        attrs = ' target="_blank" rel="noopener noreferrer"' if external else ""
        tag = f'<a href="{escape(url, quote=True)}"{attrs}>' if url else '<span class="location">'
        end = "</a>" if url else "</span>"
        ext = icon("north-east", "row-arrow") if external else ""
        return f'<li>{tag}{icon(symbol)}<span>{escape(label)}</span>{ext}{end}</li>'
    contacts = [
        line("mail", EMAIL, "mailto:" + EMAIL), line("phone", PHONE, "tel:+919944741852"),
        line("pin", "Madurai, India"), line("linkedin", "LinkedIn", LINKEDIN, True),
        line("github", "GitHub", GITHUB, True),
    ]
    return f'''
<section class="section contact dark" id="contact" data-nav="contact" aria-labelledby="contact-title">
  <div class="contact-rings" aria-hidden="true"></div><div class="wrap">
    {kicker("Contact")}
    <div class="contact-grid">
      <h2 class="display section-title" id="contact-title" data-reveal>Have an idea?<br>Let’s create<br>something<span class="accent">.</span></h2>
      <div class="contact-details"><p>Interested in technology, collaboration, and meaningful ideas. Let’s connect.</p>
        <ul class="contact-list">{"".join(contacts)}</ul>
        <a class="button primary" href="mailto:{EMAIL}">Get in touch {icon("north-east")}</a>
      </div>
    </div>
  </div>
</section>'''


def home_page():
    return (
        head("Vasuki A.S. — AI & Software Engineering", "Explore Vasuki A.S.’s portfolio of AI, machine learning and full-stack development projects, technical skills, and education in Madurai, India.", home=True)
        + '<body>' + header() + '<main id="main">' + hero() + about() + projects() + expertise()
        + background() + exploration() + philosophy() + contact() + '</main>' + footer() + '</body></html>'
    )


def project_page(project, index):
    number = index + 1
    following = PROJECTS[number % len(PROJECTS)]
    steps = "".join(f'<li><h3>{escape(title)}</h3><p>{escape(description)}</p></li>' for title, description in project["workflow"])
    return (
        head(project["full_title"] + " — Vasuki A.S.", project["summary"], "../", f'projects/{project["slug"]}.html')
        + '<body class="case-page">' + header("../", detail=True) + f'''
<main id="main">
  <section class="case-hero dark" aria-labelledby="case-title"><div class="wrap">
    <a class="text-link back-link" href="../index.html#work-{project["slug"]}">{icon("back")} Selected work</a>
    <p class="eyebrow case-kicker">Project {number:02} / {len(PROJECTS):02}<span></span>{escape(project["category"])}</p>
    <h1 class="display case-title" id="case-title">{escape(project["title"])}</h1>
    <p class="case-subtitle">{escape(project["full_title"] if project["plate"] == "certificate" else project["subtitle"])}</p>
  </div></section>
  <div class="paper case-body"><div class="wrap">
    {plate(project, number, "../", eager=True)}
    <section class="case-overview" aria-labelledby="overview-title"><div>
      {kicker("Project brief")}<h2 class="display subheading" id="overview-title">The idea.</h2>
    </div><div><p class="case-context">{escape(project["context"])}</p><h3 class="eyebrow">Technology stack</h3>{tags(project["stack"])}</div></section>
    <section class="case-workflow" aria-labelledby="workflow-title"><h2 class="display subheading" id="workflow-title">How it works.</h2><ol>{steps}</ol></section>
    <div class="project-access"><p class="eyebrow">Project access</p><dl><div><dt>Live demo</dt><dd>Unavailable</dd></div><div><dt>Source repository</dt><dd>Unavailable</dd></div></dl></div>
    <div class="case-navigation"><a class="text-link" href="../index.html#projects">{icon("back")} All projects</a>
      <a class="next-project" href="{following["slug"]}.html"><span class="eyebrow">Next project</span><span>{escape(following["title"])} {icon("arrow")}</span></a>
    </div>
  </div></div>
</main>''' + footer("../") + '</body></html>'
    )


if __name__ == "__main__":
    (OUT / "projects").mkdir(parents=True, exist_ok=True)
    (OUT / "index.html").write_text(home_page(), encoding="utf-8")
    for i, project in enumerate(PROJECTS):
        (OUT / "projects" / (project["slug"] + ".html")).write_text(project_page(project, i), encoding="utf-8")
