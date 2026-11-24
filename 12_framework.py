from flask import Flask, render_template

# Criação do app Flask
app = Flask(__name__)

# Rota para a pagina princial
# esse arroba é um decorator
@app.route('/')
def home():
    return "<h1> Bem vindo a minha suuuuuper pagina! </h1>"

# Rota para a pagina sobre!
@app.route('/sobre')
def sobre() :
    return """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Caio Rossi | Sobre</title>

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=DM+Sans:wght@400;500;600;700;800&family=Space+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css">

<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&display=swap');

#caio-about {
    --bg: #080b12;
    --surface: #101622;
    --surface2: #151e2d;
    --text: #f1f5fb;
    --muted: #8996aa;
    --accent: #8b7cff;
    --cyan: #51d9dc;
    --border: rgba(255,255,255,.09);

    background: var(--bg);
    color: var(--text);
    font-family: 'DM Sans', sans-serif;
    min-height: 100vh;
    overflow: hidden;
    position: relative;
    isolation: isolate;
    margin: -8px;
    padding: 0;
}

#caio-about * { box-sizing: border-box; }

#caio-about a {
    color: inherit;
    text-decoration: none;
}

#caio-about .ambient {
    position: absolute;
    width: 550px;
    height: 550px;
    border-radius: 50%;
    filter: blur(120px);
    opacity: .15;
    pointer-events: none;
    z-index: -1;
    animation: ambientFloat 12s ease-in-out infinite alternate;
}

#caio-about .ambient.one {
    background: #7255ff;
    top: -220px;
    left: -200px;
}

#caio-about .ambient.two {
    background: #00cbd1;
    right: -250px;
    top: 600px;
    animation-delay: -5s;
}

#caio-about .grid-bg {
    position: absolute;
    inset: 0;
    z-index: -1;
    opacity: .12;
    pointer-events: none;
    background-image:
        linear-gradient(rgba(255,255,255,.035) 1px, transparent 1px),
        linear-gradient(90deg, rgba(255,255,255,.035) 1px, transparent 1px);
    background-size: 55px 55px;
    mask-image: linear-gradient(to bottom, black, transparent 90%);
}

#caio-about .container {
    width: min(1100px, 91%);
    margin: auto;
}

#caio-about .topbar {
    height: 85px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    border-bottom: 1px solid var(--border);
}

#caio-about .brand {
    font-family: 'Space Grotesk', sans-serif;
    font-weight: 700;
    font-size: 19px;
    letter-spacing: -1px;
}

#caio-about .brand span { color: var(--accent); }

#caio-about .availability {
    display: flex;
    align-items: center;
    gap: 10px;
    font: 11px 'DM Mono', monospace;
    color: var(--muted);
    letter-spacing: 1px;
    text-transform: uppercase;
}

#caio-about .status-dot {
    width: 8px;
    height: 8px;
    border-radius: 50%;
    background: #54dc9b;
    box-shadow: 0 0 12px #54dc9b;
    animation: pulse 2s infinite;
}

#caio-about .hero {
    padding: 105px 0 90px;
    position: relative;
}

#caio-about .eyebrow {
    display: inline-flex;
    align-items: center;
    gap: 10px;
    color: var(--cyan);
    font: 11px 'DM Mono', monospace;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 25px;
}

#caio-about .eyebrow:before {
    content: '';
    height: 1px;
    width: 28px;
    background: var(--cyan);
}

#caio-about h1 {
    font-family: 'Space Grotesk', sans-serif;
    font-size: clamp(55px, 10vw, 108px);
    letter-spacing: -7px;
    line-height: .98;
    margin: 0;
    font-weight: 700;
}

#caio-about h1 .gradient {
    background: linear-gradient(110deg, #a99aff, #60dce0 75%);
    background-clip: text;
    -webkit-background-clip: text;
    color: transparent;
}

#caio-about .hero-description {
    max-width: 620px;
    font-size: 17px;
    line-height: 1.9;
    color: var(--muted);
    margin: 30px 0;
}

#caio-about .hero-description strong {
    color: var(--text);
    font-weight: 600;
}

#caio-about .hero-actions {
    display: flex;
    gap: 13px;
    flex-wrap: wrap;
    margin-top: 35px;
}

#caio-about .btn {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 11px;
    padding: 14px 21px;
    border-radius: 9px;
    font-size: 13px;
    font-weight: 700;
    transition: .3s;
    border: 1px solid var(--border);
}

#caio-about .btn-primary {
    background: var(--text);
    color: #090d15;
    border-color: var(--text);
}

#caio-about .btn-secondary {
    background: rgba(255,255,255,.035);
    color: var(--text);
}

#caio-about .btn:hover {
    transform: translateY(-4px);
    box-shadow: 0 12px 35px rgba(119,103,255,.2);
}

#caio-about .section {
    padding: 75px 0;
    border-top: 1px solid var(--border);
}

#caio-about .section-heading {
    margin-bottom: 38px;
}

#caio-about .section-label {
    color: var(--accent);
    font: 11px 'DM Mono', monospace;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 13px;
}

#caio-about h2 {
    font: 600 clamp(30px, 5vw, 43px)/1.2 'Space Grotesk', sans-serif;
    letter-spacing: -2px;
    margin: 0;
}

#caio-about .section-subtitle {
    color: var(--muted);
    font-size: 14px;
    line-height: 1.8;
    margin-top: 12px;
}

#caio-about .about-grid {
    display: grid;
    grid-template-columns: 1.15fr .85fr;
    gap: 20px;
}

#caio-about .panel {
    background: linear-gradient(145deg, rgba(255,255,255,.045), rgba(255,255,255,.012));
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 30px;
    transition: .35s;
}

#caio-about .panel:hover {
    border-color: rgba(139,124,255,.4);
    transform: translateY(-5px);
    background: linear-gradient(145deg, rgba(139,124,255,.09), rgba(255,255,255,.015));
}

#caio-about .panel p {
    color: var(--muted);
    line-height: 1.9;
    font-size: 14px;
    margin: 15px 0 0;
}

#caio-about .panel p strong { color: var(--text); }

#caio-about .panel-icon {
    font-size: 24px;
    color: var(--accent);
    margin-bottom: 18px;
}

#caio-about .panel h3 {
    font: 600 20px 'Space Grotesk', sans-serif;
    margin: 0;
}

#caio-about .principles {
    display: grid;
    gap: 13px;
}

#caio-about .principle {
    display: flex;
    align-items: center;
    gap: 13px;
    padding: 13px 0;
    border-bottom: 1px solid var(--border);
    color: #c6d0df;
    font-size: 13px;
}

#caio-about .principle i {
    color: var(--cyan);
    width: 20px;
}

#caio-about .projects {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 17px;
}

#caio-about .project {
    position: relative;
    overflow: hidden;
    min-height: 210px;
    border-radius: 15px;
    padding: 26px;
    border: 1px solid var(--border);
    background: var(--surface);
    transition: .35s;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}

#caio-about .project:before {
    content: '';
    position: absolute;
    width: 180px;
    height: 180px;
    border-radius: 50%;
    background: var(--project-color, #8b7cff);
    opacity: .09;
    filter: blur(65px);
    right: -50px;
    top: -60px;
    transition: .4s;
}

#caio-about .project:hover {
    transform: translateY(-7px);
    border-color: var(--project-color, var(--accent));
}

#caio-about .project:hover:before {
    opacity: .25;
    transform: scale(1.5);
}

#caio-about .project-top {
    display: flex;
    align-items: center;
    justify-content: space-between;
    position: relative;
}

#caio-about .project-icon {
    width: 43px;
    height: 43px;
    border-radius: 11px;
    background: rgba(255,255,255,.06);
    display: grid;
    place-items: center;
    color: var(--project-color, var(--accent));
    font-size: 18px;
}

#caio-about .project-number {
    font: 11px 'DM Mono', monospace;
    color: #627087;
}

#caio-about .project h3 {
    font: 600 21px 'Space Grotesk', sans-serif;
    margin: 20px 0 8px;
    position: relative;
}

#caio-about .project p {
    color: var(--muted);
    font-size: 12px;
    line-height: 1.7;
    margin: 0;
    max-width: 390px;
    position: relative;
}

#caio-about .project-link {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    margin-top: 20px;
    font-size: 11px;
    color: var(--project-color, var(--accent));
    font-weight: 700;
    position: relative;
}

#caio-about .project-link i { transition: .3s; }
#caio-about .project:hover .project-link i { transform: translateX(5px); }

#caio-about .interests {
    display: flex;
    flex-wrap: wrap;
    gap: 11px;
}

#caio-about .interest {
    padding: 13px 17px;
    border: 1px solid var(--border);
    background: rgba(255,255,255,.025);
    border-radius: 9px;
    color: #c1cddd;
    font-size: 12px;
    display: flex;
    align-items: center;
    gap: 10px;
    transition: .3s;
}

#caio-about .interest:hover {
    border-color: var(--cyan);
    color: var(--cyan);
    transform: translateY(-3px);
}

#caio-about .learning {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 15px;
}

#caio-about .learning-card {
    border: 1px solid var(--border);
    background: var(--surface);
    border-radius: 13px;
    padding: 23px;
}

#caio-about .learning-card i {
    font-size: 20px;
    color: var(--cyan);
    margin-bottom: 17px;
}

#caio-about .learning-card h3 {
    font: 600 16px 'Space Grotesk', sans-serif;
    margin: 0 0 9px;
}

#caio-about .learning-card p {
    color: var(--muted);
    font-size: 12px;
    line-height: 1.7;
    margin: 0;
}

#caio-about .contact {
    position: relative;
    overflow: hidden;
    border-radius: 20px;
    border: 1px solid rgba(139,124,255,.25);
    background: linear-gradient(120deg, rgba(139,124,255,.13), rgba(81,217,220,.07));
    padding: 55px 35px;
    text-align: center;
}

#caio-about .contact:after {
    content: '</>';
    position: absolute;
    right: 30px;
    bottom: -65px;
    font: 160px 'DM Mono', monospace;
    color: rgba(255,255,255,.035);
    pointer-events: none;
}

#caio-about .contact h2 {
    font-size: clamp(30px, 5vw, 43px);
}

#caio-about .contact p {
    color: var(--muted);
    max-width: 470px;
    margin: 17px auto 26px;
    line-height: 1.8;
    font-size: 14px;
}

#caio-about footer {
    padding: 30px 0;
    display: flex;
    justify-content: space-between;
    align-items: center;
    color: #68758a;
    font: 10px 'DM Mono', monospace;
    letter-spacing: 1px;
}

#caio-about .socials {
    display: flex;
    gap: 18px;
}

#caio-about .socials a {
    font-size: 16px;
    transition: .3s;
}

#caio-about .socials a:hover {
    color: var(--cyan);
    transform: translateY(-3px);
}

#caio-about .reveal {
    opacity: 0;
    transform: translateY(28px);
    transition: opacity .8s ease, transform .8s cubic-bezier(.2,.7,.2,1);
}

#caio-about .reveal.visible {
    opacity: 1;
    transform: translateY(0);
}

#caio-about .hero .reveal { transition-delay: .1s; }

#caio-about .scroll-indicator {
    position: absolute;
    bottom: 30px;
    left: 0;
    display: flex;
    align-items: center;
    gap: 12px;
    color: #647187;
    font: 10px 'DM Mono', monospace;
    letter-spacing: 2px;
    text-transform: uppercase;
}

#caio-about .scroll-line {
    width: 45px;
    height: 1px;
    background: var(--accent);
    animation: scrollLine 2s infinite;
}

@keyframes pulse {
    50% { opacity: .4; box-shadow: 0 0 3px #54dc9b; }
}

@keyframes ambientFloat {
    to { transform: translate(70px, 50px) scale(1.15); }
}

@keyframes scrollLine {
    0%,100% { transform: scaleX(.5); transform-origin: left; }
    50% { transform: scaleX(1); }
}

@media(max-width:700px) {
    #caio-about .hero { padding: 75px 0 95px; }
    #caio-about h1 { letter-spacing: -4px; }
    #caio-about .about-grid,
    #caio-about .projects { grid-template-columns: 1fr; }
    #caio-about .learning { grid-template-columns: 1fr; }
    #caio-about .section { padding: 55px 0; }
    #caio-about .panel { padding: 23px; }
    #caio-about footer { gap: 20px; flex-direction: column; text-align: center; }
    #caio-about .availability { font-size: 9px; }
}

@media(prefers-reduced-motion:reduce) {
    #caio-about *, #caio-about *:before, #caio-about *:after {
        animation-duration: .01ms !important;
        animation-iteration-count: 1 !important;
        transition-duration: .01ms !important;
        scroll-behavior: auto !important;
    }
    #caio-about .reveal { opacity: 1; transform: none; }
}
</style>
</head>

<body>
<div id="caio-about">

<div class="ambient one"></div>
<div class="ambient two"></div>
<div class="grid-bg"></div>

<div class="container">

<header class="topbar">
    <a href="#" class="brand">CAIO<span>.</span>ROSSI</a>
    <div class="availability">
        <span class="status-dot"></span>
        <span>Desenvolvendo ideias</span>
    </div>
</header>

<main>

<section class="hero">
    <div class="reveal">
        <div class="eyebrow">Um pouco sobre mim</div>
        <h1>Olá, eu sou<br><span class="gradient">Caio Rossi.</span></h1>
        <p class="hero-description">
            Sou <strong>programador, curioso por natureza e apaixonado por tecnologia.</strong>
            Gosto de transformar ideias em projetos, explorar possibilidades e entender
            como as coisas funcionam — do código à engenharia por trás dele.
            Estou sempre aprendendo, experimentando e construindo algo novo.
        </p>
        <div class="hero-actions">
            <a href="#projetos" class="btn btn-primary">
                <i class="fa-solid fa-code"></i> Explorar projetos
            </a>
            <a href="https://github.com/caioross" target="_blank" rel="noopener" class="btn btn-secondary">
                <i class="fa-brands fa-github"></i> Meu GitHub
            </a>
        </div>
    </div>
    <div class="scroll-indicator">
        <span class="scroll-line"></span> Continue explorando
    </div>
</section>

<section class="section">
    <div class="section-heading reveal">
        <div class="section-label">01 / Minha essência</div>
        <h2>Mais do que escrever código.</h2>
        <p class="section-subtitle">Tecnologia é o meio. Criar e descobrir são parte da jornada.</p>
    </div>

    <div class="about-grid">
        <article class="panel reveal">
            <div class="panel-icon"><i class="fa-solid fa-lightbulb"></i></div>
            <h3>Curiosidade que vira projeto</h3>
            <p>
                Minha relação com programação vai além de aprender linguagens.
                Gosto de investigar problemas, questionar soluções convencionais
                e descobrir até onde uma ideia pode chegar. Tenho interesse por
                <strong>software, inteligência artificial, automação, experiências
                interativas e sistemas complexos.</strong>
            </p>
        </article>

        <article class="panel reveal">
            <div class="panel-icon"><i class="fa-solid fa-compass"></i></div>
            <h3>Como penso</h3>
            <div class="principles">
                <div class="principle"><i class="fa-solid fa-brain"></i> Entender antes de implementar</div>
                <div class="principle"><i class="fa-solid fa-flask"></i> Experimentar sem medo</div>
                <div class="principle"><i class="fa-solid fa-gears"></i> Construir soluções funcionais</div>
                <div class="principle"><i class="fa-solid fa-book-open"></i> Aprender continuamente</div>
            </div>
        </article>
    </div>
</section>

<section class="section" id="projetos">
    <div class="section-heading reveal">
        <div class="section-label">02 / Laboratório de ideias</div>
        <h2>Projetos e experimentos.</h2>
        <p class="section-subtitle">
            Algumas das áreas e iniciativas que representam minha curiosidade tecnológica.
        </p>
    </div>

    <div class="projects">

        <a href="https://github.com/caioross/solitary10" target="_blank" rel="noopener"
           class="project reveal" style="--project-color:#a58aff">
            <div class="project-top">
                <div class="project-icon"><i class="fa-solid fa-infinity"></i></div>
                <span class="project-number">PROJECT_001</span>
            </div>
            <div>
                <h3>Solitary10</h3>
                <p>
                    Uma investigação matemática independente, explorando padrões,
                    relações numéricas e possibilidades de generalização.
                </p>
                <span class="project-link">Conhecer projeto <i class="fa-solid fa-arrow-right"></i></span>
            </div>
        </a>

        <a href="https://github.com/caioross" target="_blank" rel="noopener"
           class="project reveal" style="--project-color:#54d9df">
            <div class="project-top">
                <div class="project-icon"><i class="fa-solid fa-earth-americas"></i></div>
                <span class="project-number">PROJECT_002</span>
            </div>
            <div>
                <h3>Simulação da Terra</h3>
                <p>
                    Explorando a possibilidade de representar infraestrutura,
                    transportes e geografia em uma grande simulação digital.
                </p>
                <span class="project-link">Explorar repositórios <i class="fa-solid fa-arrow-right"></i></span>
            </div>
        </a>

        <a href="https://github.com/caioross" target="_blank" rel="noopener"
           class="project reveal" style="--project-color:#f2b66d">
            <div class="project-top">
                <div class="project-icon"><i class="fa-solid fa-robot"></i></div>
                <span class="project-number">PROJECT_003</span>
            </div>
            <div>
                <h3>Inteligência Artificial</h3>
                <p>
                    Experimentação com agentes inteligentes, automação,
                    ferramentas de desenvolvimento e novas formas de interação.
                </p>
                <span class="project-link">Ver experimentos <i class="fa-solid fa-arrow-right"></i></span>
            </div>
        </a>

        <a href="https://github.com/caioross" target="_blank" rel="noopener"
           class="project reveal" style="--project-color:#f18eaa">
            <div class="project-top">
                <div class="project-icon"><i class="fa-solid fa-microchip"></i></div>
                <span class="project-number">PROJECT_004</span>
            </div>
            <div>
                <h3>Hardware & Engenharia</h3>
                <p>
                    Ideias envolvendo eletrônica, dispositivos inteligentes,
                    prototipagem e integração entre software e mundo físico.
                </p>
                <span class="project-link">Ver projetos <i class="fa-solid fa-arrow-right"></i></span>
            </div>
        </a>

    </div>
</section>

<section class="section">
    <div class="section-heading reveal">
        <div class="section-label">03 / Interesses</div>
        <h2>O universo que me inspira.</h2>
        <p class="section-subtitle">Algumas das coisas que alimentam minha criatividade.</p>
    </div>

    <div class="interests reveal">
        <div class="interest"><i class="fa-solid fa-code"></i> Programação</div>
        <div class="interest"><i class="fa-solid fa-brain"></i> Inteligência Artificial</div>
        <div class="interest"><i class="fa-solid fa-microchip"></i> Eletrônica</div>
        <div class="interest"><i class="fa-solid fa-cube"></i> Computação 3D</div>
        <div class="interest"><i class="fa-solid fa-globe"></i> Simulações</div>
        <div class="interest"><i class="fa-solid fa-flask"></i> Matemática</div>
        <div class="interest"><i class="fa-solid fa-gamepad"></i> Desenvolvimento de jogos</div>
        <div class="interest"><i class="fa-solid fa-wand-magic-sparkles"></i> Experiências interativas</div>
        <div class="interest"><i class="fa-solid fa-water"></i> Surf</div>
        <div class="interest"><i class="fa-solid fa-music"></i> Música</div>
    </div>
</section>

<section class="section">
    <div class="section-heading reveal">
        <div class="section-label">04 / Evolução constante</div>
        <h2>Sempre existe algo novo para aprender.</h2>
        <p class="section-subtitle">
            Minha jornada de aprendizado é contínua. Atualmente, estou aprofundando meus conhecimentos em:
        </p>
    </div>

    <div class="learning">
        <article class="learning-card reveal">
            <i class="fa-brands fa-python"></i>
            <h3>Python</h3>
            <p>
                Estudando programação, lógica, estruturas de dados e desenvolvimento
                de aplicações através de um curso completo.
            </p>
        </article>

        <article class="learning-card reveal">
            <i class="fa-solid fa-terminal"></i>
            <h3>Engenharia de software</h3>
            <p>
                Explorando arquitetura, organização de projetos, automação,
                ferramentas e boas práticas de desenvolvimento.
            </p>
        </article>

        <article class="learning-card reveal">
            <i class="fa-solid fa-atom"></i>
            <h3>Novas tecnologias</h3>
            <p>
                Investigando IA, computação, sistemas interativos e possibilidades
                que conectam diferentes áreas da tecnologia.
            </p>
        </article>
    </div>
</section>

<section class="section">
    <div class="contact reveal">
        <div class="section-label">05 / Vamos nos conectar?</div>
        <h2>Boas ideias começam com uma conversa.</h2>
        <p>
            Se você também gosta de tecnologia, programação, inovação ou simplesmente
            tem uma ideia interessante para compartilhar, será um prazer trocar experiências.
        </p>
        <a href="https://github.com/caioross" target="_blank" rel="noopener"
           class="btn btn-primary">
            <i class="fa-brands fa-github"></i> Acessar meu GitHub
        </a>
    </div>
</section>

</main>

<footer>
    <span>© <span id="caio-year"></span> CAIO ROSSI</span>
    <span>FEITO COM CURIOSIDADE E CÓDIGO.</span>
    <div class="socials">
        <a href="https://github.com/caioross" target="_blank" rel="noopener" aria-label="GitHub">
            <i class="fa-brands fa-github"></i>
        </a>
    </div>
</footer>

</div>
</div>

<script>
(function () {
    const root = document.getElementById('caio-about');
    if (!root) return;

    const year = root.querySelector('#caio-year');
    if (year) year.textContent = new Date().getFullYear();

    const elements = root.querySelectorAll('.reveal');

    if ('IntersectionObserver' in window) {
        const observer = new IntersectionObserver((entries, obs) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('visible');
                    obs.unobserve(entry.target);
                }
            });
        }, {
            threshold: 0.12,
            rootMargin: '0px 0px -35px 0px'
        });

        elements.forEach(element => observer.observe(element));
    } else {
        elements.forEach(element => element.classList.add('visible'));
    }

    const cards = root.querySelectorAll('.project, .panel, .learning-card');

    cards.forEach((card, index) => {
        card.style.transitionDelay = (index % 4) * 70 + 'ms';
    });

    root.querySelectorAll('a[href^="#"]').forEach(link => {
        link.addEventListener('click', function (event) {
            const target = root.querySelector(this.getAttribute('href'));
            if (target) {
                event.preventDefault();
                target.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        });
    });
})();
</script>

</body>
</html>
"""

# rota com variaveis na URL
@app.route('/ola/<nome>')
def saudacao(nome):
    return f"<h1> Seja bem vindo </h1> {nome}"

if __name__ == '__main__':
    app.run(debug=True)
