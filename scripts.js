// =========================================
// Three.js Quantum Network Background
// =========================================
(function () {
    'use strict';

    if (typeof THREE === 'undefined') return;

    const canvas = document.getElementById('bg-canvas');
    if (!canvas) return;

    // Scene setup
    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(60, window.innerWidth / window.innerHeight, 1, 3000);
    camera.position.set(0, 0, 1200);

    const renderer = new THREE.WebGLRenderer({ canvas, alpha: true, antialias: true });
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
    renderer.setSize(window.innerWidth, window.innerHeight);
    renderer.setClearColor(0x000000, 0); // transparent

    // Mouse
    let mouseX = 0, mouseY = 0;
    let targetX = 0, targetY = 0;
    document.addEventListener('mousemove', (e) => {
        targetX = (e.clientX / window.innerWidth - 0.5) * 600;
        targetY = (e.clientY / window.innerHeight - 0.5) * 300;
    });

    // Window resize
    window.addEventListener('resize', () => {
        camera.aspect = window.innerWidth / window.innerHeight;
        camera.updateProjectionMatrix();
        renderer.setSize(window.innerWidth, window.innerHeight);
    });

    // ---- NODES ----
    const NODE_COUNT = 180;
    const AREA = 1600;
    const CONNECT_DIST = 200;

    const nodePositions = [];
    const nodeVelocities = [];
    const geo = new THREE.BufferGeometry();
    const pos = new Float32Array(NODE_COUNT * 3);

    for (let i = 0; i < NODE_COUNT; i++) {
        const x = (Math.random() - 0.5) * AREA;
        const y = (Math.random() - 0.5) * AREA;
        const z = (Math.random() - 0.5) * 600;
        nodePositions.push([x, y, z]);
        nodeVelocities.push([
            (Math.random() - 0.5) * 0.18,
            (Math.random() - 0.5) * 0.18,
            (Math.random() - 0.5) * 0.08,
        ]);
        pos[i * 3] = x;
        pos[i * 3 + 1] = y;
        pos[i * 3 + 2] = z;
    }

    geo.setAttribute('position', new THREE.BufferAttribute(pos, 3));

    const pointMat = new THREE.PointsMaterial({
        color: 0x0A0A0A,    // monochrome black
        size: 2.5,
        sizeAttenuation: true,
        transparent: true,
        opacity: 0.5,
    });

    const points = new THREE.Points(geo, pointMat);
    scene.add(points);

    // ---- LINES (lazy allocation) ----
    const lineMat = new THREE.LineBasicMaterial({
        color: 0x5B21B6,   // single accent: violet
        transparent: true,
        opacity: 0.12,
    });
    const lineGeo = new THREE.BufferGeometry();
    const lineSegs = new THREE.LineSegments(lineGeo, lineMat);
    scene.add(lineSegs);

    // ---- ANIMATION LOOP ----
    let frame = 0;
    function animate() {
        requestAnimationFrame(animate);
        frame++;

        // Smooth camera parallax
        mouseX += (targetX - mouseX) * 0.04;
        mouseY += (targetY - mouseY) * 0.04;
        camera.position.x += (mouseX * 0.15 - camera.position.x) * 0.06;
        camera.position.y += (-mouseY * 0.15 - camera.position.y) * 0.06;
        camera.lookAt(scene.position);

        // Update node positions
        const posArr = geo.attributes.position.array;
        for (let i = 0; i < NODE_COUNT; i++) {
            nodePositions[i][0] += nodeVelocities[i][0];
            nodePositions[i][1] += nodeVelocities[i][1];
            nodePositions[i][2] += nodeVelocities[i][2];

            // Wrap around — creates seamless looping
            if (nodePositions[i][0] > AREA / 2) nodePositions[i][0] = -AREA / 2;
            if (nodePositions[i][0] < -AREA / 2) nodePositions[i][0] = AREA / 2;
            if (nodePositions[i][1] > AREA / 2) nodePositions[i][1] = -AREA / 2;
            if (nodePositions[i][1] < -AREA / 2) nodePositions[i][1] = AREA / 2;
            if (nodePositions[i][2] > 300) nodePositions[i][2] = -300;
            if (nodePositions[i][2] < -300) nodePositions[i][2] = 300;

            posArr[i * 3] = nodePositions[i][0];
            posArr[i * 3 + 1] = nodePositions[i][1];
            posArr[i * 3 + 2] = nodePositions[i][2];
        }
        geo.attributes.position.needsUpdate = true;

        // Update connections every 2 frames for performance
        if (frame % 2 === 0) {
            const linePositions = [];
            for (let i = 0; i < NODE_COUNT; i++) {
                for (let j = i + 1; j < NODE_COUNT; j++) {
                    const dx = nodePositions[i][0] - nodePositions[j][0];
                    const dy = nodePositions[i][1] - nodePositions[j][1];
                    const dz = nodePositions[i][2] - nodePositions[j][2];
                    const dist = Math.sqrt(dx * dx + dy * dy + dz * dz);
                    if (dist < CONNECT_DIST) {
                        linePositions.push(
                            nodePositions[i][0], nodePositions[i][1], nodePositions[i][2],
                            nodePositions[j][0], nodePositions[j][1], nodePositions[j][2]
                        );
                    }
                }
            }
            lineGeo.setAttribute('position', new THREE.Float32BufferAttribute(linePositions, 3));
        }

        // Very slow network rotation for depth feel
        scene.rotation.y += 0.0005;
        scene.rotation.x += 0.0002;

        renderer.render(scene, camera);
    }

    animate();
})();

// =========================================
// Scroll Reveal + Mobile Menu
// =========================================
document.addEventListener('DOMContentLoaded', () => {
    // Reveal on scroll
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('reveal-active');
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.08, rootMargin: '0px 0px -40px 0px' });

    document.querySelectorAll(
        'section, .sidebar, .pub-item, .talk-card, .project-card, .teaching-card, .awards-list li, .news-item'
    ).forEach(el => {
        el.classList.add('reveal');
        observer.observe(el);
    });

    // Mobile menu
    const menuBtn = document.getElementById('menuBtn');
    const navLinks = document.getElementById('navLinks');
    if (menuBtn && navLinks) {
        menuBtn.addEventListener('click', () => {
            navLinks.classList.toggle('active');
        });
        // Close on nav link click
        navLinks.querySelectorAll('a').forEach(a => {
            a.addEventListener('click', () => navLinks.classList.remove('active'));
        });
    }
});
