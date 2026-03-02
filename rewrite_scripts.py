import re

with open('scripts.js', 'w') as f:
    f.write("""// Light Quantum Academic Three.js Background
let scene, camera, renderer, particles, linesMesh;
const particleCount = 200;
const interactionDistance = 150;
const connectionDistance = 100;
let mouse = new THREE.Vector2(-1000, -1000);
let targetMouse = new THREE.Vector2(-1000, -1000);
let windowHalfX = window.innerWidth / 2;
let windowHalfY = window.innerHeight / 2;

function initThreeJS() {
    const canvas = document.getElementById('bg-canvas');
    if (!canvas || typeof THREE === 'undefined') return;

    scene = new THREE.Scene();
    scene.background = null; // Transparent background to let CSS show through
    scene.fog = new THREE.FogExp2(0xfafafa, 0.0015);

    camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 1, 2000);
    camera.position.z = 1000;

    renderer = new THREE.WebGLRenderer({ canvas: canvas, alpha: true, antialias: true });
    renderer.setPixelRatio(window.devicePixelRatio);
    renderer.setSize(window.innerWidth, window.innerHeight);

    // Particles
    const geometry = new THREE.BufferGeometry();
    const positions = new Float32Array(particleCount * 3);
    const velocities = [];

    for (let i = 0; i < particleCount; i++) {
        positions[i * 3] = (Math.random() - 0.5) * 2000;
        positions[i * 3 + 1] = (Math.random() - 0.5) * 2000;
        positions[i * 3 + 2] = (Math.random() - 0.5) * 1000;

        velocities.push({
            x: (Math.random() - 0.5) * 0.5,
            y: (Math.random() - 0.5) * 0.5,
            z: (Math.random() - 0.5) * 0.5
        });
    }

    geometry.setAttribute('position', new THREE.BufferAttribute(positions, 3));
    
    // Custom shader material for soft glowing points
    const material = new THREE.PointsMaterial({
        color: 0x0284c7, // Quantum light blue
        size: 3.5,
        transparent: true,
        opacity: 0.6,
        sizeAttenuation: true
    });

    particles = new THREE.Points(geometry, material);
    particles.velocities = velocities;
    scene.add(particles);

    // Lines for Connections
    const lineMaterial = new THREE.LineBasicMaterial({
        color: 0x94a3b8, // Light slate
        transparent: true,
        opacity: 0.15,
        linewidth: 1
    });
    
    // Initialize empty line geometry
    const lineGeometry = new THREE.BufferGeometry();
    linesMesh = new THREE.LineSegments(lineGeometry, lineMaterial);
    scene.add(linesMesh);

    // Events
    document.addEventListener('mousemove', onDocumentMouseMove, false);
    window.addEventListener('resize', onWindowResize, false);

    animate();
}

function onWindowResize() {
    windowHalfX = window.innerWidth / 2;
    windowHalfY = window.innerHeight / 2;
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth, window.innerHeight);
}

function onDocumentMouseMove(event) {
    // Map mouse to 3D space rough equivalent
    targetMouse.x = (event.clientX - windowHalfX) * 2;
    targetMouse.y = (event.clientY - windowHalfY) * 2;
}

function animate() {
    requestAnimationFrame(animate);
    render();
}

function render() {
    const positions = particles.geometry.attributes.position.array;
    const vels = particles.velocities;
    
    // Smooth mouse follow
    mouse.x += (targetMouse.x - mouse.x) * 0.05;
    mouse.y += (targetMouse.y - mouse.y) * 0.05;
    
    // Add subtle camera movement based on mouse
    camera.position.x += (mouse.x * 0.2 - camera.position.x) * 0.05;
    camera.position.y += (-mouse.y * 0.2 - camera.position.y) * 0.05;
    camera.lookAt(scene.position);

    const linePositions = [];

    // Update particles and prepare lines
    for (let i = 0; i < particleCount; i++) {
        let i3 = i * 3;
        
        // Move
        positions[i3] += vels[i].x;
        positions[i3 + 1] += vels[i].y;
        positions[i3 + 2] += vels[i].z;
        
        // Bounds checking
        if (Math.abs(positions[i3]) > 1000) positions[i3] *= -0.99;
        if (Math.abs(positions[i3 + 1]) > 1000) positions[i3 + 1] *= -0.99;
        if (Math.abs(positions[i3 + 2]) > 500) positions[i3 + 2] *= -0.99;

        // Interaction with mouse (repel/attract effect)
        // Project mouse to 3D roughly
        let mx = mouse.x;
        let my = -mouse.y; 
        
        let dx = mx - positions[i3];
        let dy = my - positions[i3 + 1];
        let distToMouse = Math.sqrt(dx*dx + dy*dy);
        
        if (distToMouse < interactionDistance * 2) {
             positions[i3] -= dx * 0.005;
             positions[i3 + 1] -= dy * 0.005;
        }

        // Draw connections
        for (let j = i + 1; j < particleCount; j++) {
            let j3 = j * 3;
            let p1dx = positions[i3] - positions[j3];
            let p1dy = positions[i3 + 1] - positions[j3 + 1];
            let p1dz = positions[i3 + 2] - positions[j3 + 2];
            let dist = Math.sqrt(p1dx*p1dx + p1dy*p1dy + p1dz*p1dz);

            if (dist < connectionDistance) {
                linePositions.push(
                    positions[i3], positions[i3 + 1], positions[i3 + 2],
                    positions[j3], positions[j3 + 1], positions[j3 + 2]
                );
            }
        }
    }

    particles.geometry.attributes.position.needsUpdate = true;
    
    // Update line geometry
    linesMesh.geometry.setAttribute('position', new THREE.Float32BufferAttribute(linePositions, 3));
    
    // Slowly rotate the whole network
    scene.rotation.y += 0.001;
    scene.rotation.x += 0.0005;

    renderer.render(scene, camera);
}

// Global Initialization
document.addEventListener('DOMContentLoaded', () => {
    // Start Background
    initThreeJS();

    // Scroll Reveal
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('reveal-active');
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
""")
