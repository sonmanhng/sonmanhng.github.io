// Advanced Background Particle System
class Particle {
    constructor(width, height, layer = 1) {
        this.width = width;
        this.height = height;
        this.layer = layer; // 1: Front, 2: Middle, 3: Back
        this.reset();
    }

    reset() {
        this.x = Math.random() * this.width;
        this.y = Math.random() * this.height;
        this.vx = (Math.random() - 0.5) * (0.6 / this.layer);
        this.vy = (Math.random() - 0.5) * (0.6 / this.layer);
        this.size = (Math.random() * 2 + 0.5) / this.layer;
        this.alpha = (Math.random() * 0.4 + 0.1) / this.layer;
    }

    update(mouse, mouseRange) {
        this.x += this.vx;
        this.y += this.vy;

        if (this.x < 0) this.x = this.width;
        if (this.x > this.width) this.x = 0;
        if (this.y < 0) this.y = this.height;
        if (this.y > this.height) this.y = 0;

        // Interaction
        const dx = mouse.x - this.x;
        const dy = mouse.y - this.y;
        const dist = Math.sqrt(dx * dx + dy * dy);

        if (dist < mouseRange / this.layer) {
            const force = (mouseRange / this.layer - dist) / (mouseRange / this.layer);
            this.x -= dx * force * 0.02;
            this.y -= dy * force * 0.02;
        }
    }

    draw(ctx) {
        ctx.fillStyle = `rgba(255, 255, 255, ${this.alpha})`;
        ctx.beginPath();
        ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
        ctx.fill();
    }
}

class BackgroundSystem {
    constructor() {
        this.canvas = document.getElementById('bg-canvas') || this.createCanvas();
        this.ctx = this.canvas.getContext('2d');
        this.particles = [];
        this.mouse = { x: -1000, y: -1000 };
        this.mouseRange = 250;
        this.connectionDistance = 150;

        window.addEventListener('mousemove', (e) => {
            this.mouse.x = e.clientX;
            this.mouse.y = e.clientY;
        });

        window.addEventListener('resize', () => this.init());
        this.init();
        this.animate();
    }

    createCanvas() {
        const c = document.createElement('canvas');
        c.id = 'bg-canvas';
        document.body.prepend(c);
        return c;
    }

    init() {
        this.width = this.canvas.width = window.innerWidth;
        this.height = this.canvas.height = window.innerHeight;
        this.particles = [];

        // Layered distribution
        const counts = [40, 60, 80]; // Front, Middle, Back
        counts.forEach((count, i) => {
            for (let j = 0; j < count; j++) {
                this.particles.push(new Particle(this.width, this.height, i + 1));
            }
        });
    }

    animate() {
        this.ctx.clearRect(0, 0, this.width, this.height);

        for (let i = 0; i < this.particles.length; i++) {
            const p = this.particles[i];
            p.update(this.mouse, this.mouseRange);
            p.draw(this.ctx);

            // Draw connections for the front/middle layers only for performance
            if (p.layer > 2) continue;

            for (let j = i + 1; j < this.particles.length; j++) {
                const p2 = this.particles[j];
                if (p.layer !== p2.layer) continue;

                const dx = p.x - p2.x;
                const dy = p.y - p2.y;
                const dist = Math.sqrt(dx * dx + dy * dy);

                const limit = this.connectionDistance / p.layer;
                if (dist < limit) {
                    this.ctx.strokeStyle = `rgba(255, 255, 255, ${(1 - dist / limit) * 0.1 / p.layer})`;
                    this.ctx.lineWidth = 0.5 / p.layer;
                    this.ctx.beginPath();
                    this.ctx.moveTo(p.x, p.y);
                    this.ctx.lineTo(p2.x, p2.y);
                    this.ctx.stroke();
                }
            }
        }

        requestAnimationFrame(() => this.animate());
    }
}

// Text Scramble Effect
class TextScramble {
    constructor(el) {
        this.el = el;
        this.chars = '!<>-_\\/[]{}—=+*^?#________';
        this.update = this.update.bind(this);
    }
    setText(newText) {
        const oldText = this.el.innerText;
        const length = Math.max(oldText.length, newText.length);
        const promise = new Promise((resolve) => this.resolve = resolve);
        this.queue = [];
        for (let i = 0; i < length; i++) {
            const from = oldText[i] || '';
            const to = newText[i] || '';
            const start = Math.floor(Math.random() * 40);
            const end = start + Math.floor(Math.random() * 40);
            this.queue.push({ from, to, start, end });
        }
        cancelAnimationFrame(this.frameRequest);
        this.frame = 0;
        this.update();
        return promise;
    }
    update() {
        let output = '';
        let complete = 0;
        for (let i = 0, n = this.queue.length; i < n; i++) {
            let { from, to, start, end, char } = this.queue[i];
            if (this.frame >= end) {
                complete++;
                output += to;
            } else if (this.frame >= start) {
                if (!char || Math.random() < 0.28) {
                    char = this.randomChar();
                    this.queue[i].char = char;
                }
                output += `<span class="dud">${char}</span>`;
            } else {
                output += from;
            }
        }
        this.el.innerHTML = output;
        if (complete === this.queue.length) {
            this.resolve();
        } else {
            this.frameRequest = requestAnimationFrame(this.update);
            this.frame++;
        }
    }
    randomChar() {
        return this.chars[Math.floor(Math.random() * this.chars.length)];
    }
}

// Global Initialization
document.addEventListener('DOMContentLoaded', () => {
    // Start Background
    new BackgroundSystem();

    // Scroll Reveal
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('reveal-active');

                const headings = entry.target.querySelectorAll('h1, h2, h3');
                headings.forEach(h => {
                    const fx = new TextScramble(h);
                    fx.setText(h.innerText);
                });

                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    document.querySelectorAll('section, .sidebar, .post, .pub-item, .talk-card, .project-card').forEach(el => {
        el.classList.add('reveal');
        observer.observe(el);
    });

    // Mobile Menu
    const menuBtn = document.getElementById('menuBtn');
    const navLinks = document.getElementById('navLinks');
    if (menuBtn && navLinks) {
        menuBtn.addEventListener('click', () => {
            navLinks.classList.toggle('active');
        });
    }
});
