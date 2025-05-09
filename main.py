from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    readme_html_content = """
  <div id="readme-html-content">
  <h1>Caesar Cipher Tool</h1>
  <p>This project combines a Caesar Cipher cryptographic tool with my interactive visualization skills, all served as a single-page web application using Flask.</p>

  <h2>Features</h2>

  <h3>Caesar Cipher Tool (Center Panel)</h3>
  <ul>
    <li>Encrypt and decrypt alphabetic messages (spaces are preserved).</li>
    <li>User-specified shift value ranging from 1 to 25.</li>
    <li>Real-time input validation and clear error messages.</li>
    <li>Convenient "Copy to Clipboard" functionality for the processed text.</li>
    <li>A sleek, space-themed interface designed for usability.</li>
  </ul>


  <h3>Application Structure (Layout)</h3>
  <ul>
    <li><strong>Left Panel</strong>: Displays this project overview.</li>
    <li><strong>Center Panel</strong>: Hosts the interactive Caesar Cipher tool.</li>
    <li><strong>Right Panel</strong>: Features the live 3D "Cosmic Commits" visualization.</li>
  </ul>

  <h2>Technologies Used</h2>
  <ul>
    <li><strong>Python (Flask)</strong>: Serves the single-page application.</li>
    <li><strong>HTML, CSS, JavaScript</strong>: Structure, style, and client-side logic.</li>
    <li><strong>Three.js</strong>: Powers the 3D graphics for the globe, particles, arcs, and towers.</li>
    <li><strong>Anime.js</strong>: Used for sophisticated animations of 3D elements and UI transitions.</li>
  </ul>

  <h2>How to Get</h2>
  <ol>
    <li><strong>Clone the repository</strong>
      <pre><code>git clone https://github.com/Golgrax/caesar-cipher-tool.git</code></pre>
    </li>
    <li><strong>Change into the project directory</strong>
      <pre><code>cd caesar-cipher-tool</code></pre>
    </li>
    <li><strong>(Optional) Inspect the code</strong>
      Open the folder in your editor of choice:
      <pre><code>code .</code></pre>
    </li>
    <li><strong>Verify Python version</strong>
      Make sure you’re running Python 3.7 or newer:
      <pre><code>python3 --version</code></pre>
    </li>
  </ol>

  <h2>How to Run</h2>
  <ol>
    <li><strong>Create a virtual environment</strong>
      <pre><code>python3 -m venv venv</code></pre>
    </li>
    <li><strong>Activate the virtual environment</strong>
      <p>On macOS/Linux:</p>
      <pre><code>source venv/bin/activate</code></pre>
      <p>On Windows (PowerShell):</p>
      <pre><code>.\\venv\\Scripts\\Activate.ps1</code></pre>
    </li>
    <li><strong>Install dependencies</strong>
      <pre><code>pip install Flask</code></pre>
    </li>
    <li><strong>Run the application</strong>
      <pre><code>python main.py
  # or
  python3 main.py</code></pre>
    </li>
    <li><strong>Open in your browser</strong>
      Navigate to <code>http://127.0.0.1:5000/</code> to see the app in action.</li>
  </ol>

  <hr>
  <p><em>This project overview is embedded directly into the application.</em></p>
  </div>

    """

    html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ceasar Cipher Tool</title>
    <style>
        html {{
            scroll-behavior: smooth;
        }}
        body {{
            margin: 0;
            background-color: #00050a;
            color: #e0e0e0;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            /* display: flex; // This will be on page-container for media query control */
            /* height: 100vh; // Removed to allow natural page scroll on mobile */
            /* width: 100vw; // Default */
        }}

        #page-container {{
            display: flex;
            width: 100%;
            height: 100vh; /* Default to full viewport height for desktop */
        }}

        #left-column {{
            width: 28%;
            height: 100%; /* Full height of parent for desktop */
            padding: 20px;
            box-sizing: border-box;
            border-right: 1px solid #003355;
            overflow-y: auto;
            background-color: rgba(5, 15, 30, 0.7);
        }}
        #readme-html-content h1, #readme-html-content h2, #readme-html-content h3 {{
            color: #00cFFF; border-bottom: 1px solid #0077aa; padding-bottom: 5px; margin-top: 25px;
        }}
        #readme-html-content h1 {{ font-size: 1.7em; margin-top: 5px; }}
        #readme-html-content h2 {{ font-size: 1.4em; }}
        #readme-html-content h3 {{ font-size: 1.15em; color: #7ddcff; }}
        #readme-html-content p {{ line-height: 1.6; color: #c0d8f0; margin-bottom: 12px; }}
        #readme-html-content ul, #readme-html-content ol {{ margin-left: 20px; padding-left: 10px; color: #b0c8e0; }}
        #readme-html-content li {{ margin-bottom: 8px; }}
        #readme-html-content code {{ background-color: rgba(0, 50, 80, 0.7); padding: 2px 6px; border-radius: 4px; font-family: Consolas, Monaco, 'Andale Mono', 'Ubuntu Mono', monospace; color: #90e0ef; font-size: 0.9em;}}
        #readme-html-content pre {{ background-color: rgba(0, 20, 40, 0.85); padding: 12px; border-radius: 5px; overflow-x: auto; border: 1px solid #004466; font-size: 0.85em;}}
        #readme-html-content pre code {{ background-color: transparent; padding: 0; }}
        #readme-html-content hr {{ border: 0; height: 1px; background-image: linear-gradient(to right, rgba(0, 51, 85, 0), rgba(0, 119, 170, 0.75), rgba(0, 51, 85, 0)); margin: 20px 0;}}

        #center-column {{
            width: 30%;
            min-width: 330px;
            height: 100%; /* Full height of parent for desktop */
            padding: 15px;
            box-sizing: border-box;
            overflow-y: auto;
            display: flex;
            flex-direction: column;
            align-items: center;
            background-color: #020810;
        }}

        #right-column {{
            flex-grow: 1;
            height: 100%; /* Full height of parent for desktop */
            position: relative;
            border-left: 1px solid #003355;
            min-width: 300px;
        }}
        #background-canvas {{
            position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: 0;
        }}

        /* Cipher Container Styling */
        #cipher-container {{
            position: relative; z-index: 1; background-color: rgba(10, 25, 45, 0.94);
            padding: 20px; border-radius: 12px; box-shadow: 0 0 20px rgba(0, 160, 255, 0.6);
            width: 100%; max-width: 460px; margin-top: 25px; text-align: left;
            border: 1px solid rgba(0, 150, 255, 0.4);
        }}
        #cipher-container h2 {{ font-size: 20px; margin-bottom:18px; text-align:center; color: #00cFFF; text-shadow: 0 0 8px rgba(0, 180, 255, 0.5); margin-top:0;}}
        #cipher-container label {{ display: block; margin-top: 15px; margin-bottom: 5px; color: #c0e0ff; font-weight: 500; font-size:13px;}}
        #cipher-container input[type="text"], #cipher-container input[type="number"] {{ width: calc(100% - 20px); padding: 9px; border-radius: 5px; border: 1px solid #0088cc; background-color: #060d1c; color: #d0f0ff; font-size: 14px;}}
        #cipher-container input[type="text"]:focus, #cipher-container input[type="number"]:focus {{ border-color: #00cFFF; box-shadow: 0 0 8px rgba(0, 180, 255, 0.5); outline: none;}}
        #cipher-container .buttons {{ text-align: center; margin-top: 20px; margin-bottom: 8px; }}
        #cipher-container button {{ padding: 9px 16px; margin: 0 8px; border-radius: 5px; border: none; background-color: #007bff; color: white; font-size: 14px; font-weight: 500; cursor: pointer; transition: background-color 0.2s ease, transform 0.1s ease;}}
        #cipher-container button:hover {{ background-color: #006acc; transform: translateY(-1px); }}
        #cipher-container button#decrypt-btn {{ background-color: #17a2b8; }}
        #cipher-container button#decrypt-btn:hover {{ background-color: #117a8b; }}
        .result-header {{ display: flex; justify-content: space-between; align-items: center; margin-top: 20px; margin-bottom: 6px; }}
        .result-header h3 {{ margin: 0; color: #00cFFF; font-size: 15px; }}
        #copy-result-btn {{ padding: 5px 10px; font-size: 11px; background-color: #00aaff; color: #000020; border: none; border-radius: 4px; cursor: pointer; transition: background-color 0.2s ease;}}
        #copy-result-btn:hover {{ background-color: #33ceff; }}
        #copy-result-btn.copied {{ background-color: #28a745; color: white; }}
        #result-text-container {{ padding: 10px; background-color: rgba(0,0,0,0.5); border-radius: 5px; min-height: 20px; max-height: 100px; overflow-y: auto; word-wrap: break-word; border: 1px dashed #0088cc; color: #c0e8ff;}}
        #result-text-container #result{{ font-size: 13px; white-space: pre-wrap; margin:0; }}
        #error-message {{ margin-top: 15px; color: #ff6666; font-weight: bold; text-align: center; min-height: 18px; font-size: 12px;}}

        /* --- Mobile Friendliness --- */
        @media (max-width: 992px) {{
            body {{
                /* overflow-y: auto; Let page-container handle this if needed */
                overflow-x: hidden; /* Prevent horizontal scroll as a fallback */
            }}
            #page-container {{
                flex-direction: column; /* Stack columns vertically */
                height: auto;           /* Allow page container to grow with content */
                min-height: 100vh;      /* Ensure it at least fills the viewport */
                overflow-y: auto;       /* Allow whole page to scroll if content is too tall */
            }}
            #left-column, #center-column, #right-column {{
                width: 100%;        /* Full width when stacked */
                min-width: 0;       /* Remove desktop min-width constraints */
                height: auto;       /* Height based on content or specific rules below */
                border-right: none;
                border-left: none;
                border-bottom: 1px solid #003355;
            }}
            #left-column {{
                max-height: 50vh; /* Limit height of README, make it scrollable within its section */
                order: 1;
            }}
            #center-column {{
                order: 2;
                padding: 15px; /* Consistent padding */
                 /* min-height to ensure visibility even if cipher tool is short */
            }}
            #cipher-container {{
                margin-top: 20px;
                margin-bottom: 20px;
                max-width: 95%; /* Allow it to be slightly wider on tablets */
            }}
            #right-column {{
                height: 60vh;
                min-height: 300px; /* Minimum visible height for 3D canvas */
                order: 3;
                border-bottom: none; /* No border for the last item */
            }}
        }}

        @media (max-width: 480px) {{ /* Specific tweaks for very small screens */
            #left-column {{
                padding: 15px 10px; /* Top/bottom, Left/right */
                max-height: 40vh;
            }}
            #readme-html-content h1 {{ font-size: 1.4em; }}
            #readme-html-content h2 {{ font-size: 1.1em; }}
            #readme-html-content p {{ font-size: 0.9em; }}
            #readme-html-content li {{ font-size: 0.9em; }}


            #center-column {{
                padding: 10px;
            }}
            #cipher-container {{
                padding: 15px;
                max-width: 100%; /* Full width of its parent */
            }}
            #cipher-container h2 {{ font-size: 18px; margin-bottom: 15px; }}
            #cipher-container label {{ font-size:12px; margin-top: 12px; }}
            #cipher-container input[type="text"], #cipher-container input[type="number"] {{ font-size: 13px; padding: 8px;}}
            #cipher-container button {{ font-size: 13px; padding: 8px 12px; margin: 0 5px;}}
            .result-header h3 {{ font-size: 14px; }}
            #copy-result-btn {{ font-size: 10px; padding: 4px 8px;}}
            #result-text-container {{ max-height: 80px; }}
            #result-text-container #result {{ font-size: 12px; }}
            #error-message {{ font-size: 11px; }}

            #right-column {{
                height: 50vh;
                min-height: 250px;
            }}
        }}

    </style>
</head>
<body>
    <div id="page-container">
        <div id="left-column">
            {readme_html_content}
        </div>
        <div id="center-column">
            <div id="cipher-container">
                <h2>Ceasar Cipher Tool</h2>
                <div><label for="message">Datastream (Message):</label><input type="text" id="message" placeholder="Alphabetic text & spaces"></div>
                <div><label for="shift">Quantum Shift (1-25):</label><input type="number" id="shift" min="1" max="25" value="3"></div>
                <div id="error-message"></div>
                <div class="buttons"><button id="encrypt-btn">Encrypt</button><button id="decrypt-btn">Decrypt</button></div>
                <div class="result-header"><h3>Output Signal:</h3><button id="copy-result-btn" title="Copy">Copy</button></div>
                <div id="result-text-container"><p id="result"></p></div>
            </div>
        </div>
        <div id="right-column">
            <canvas id="background-canvas"></canvas>
        </div>
    </div>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/animejs/3.2.1/anime.min.js"></script>

    <script>
        // --- Global Variables ---
        // (All global JS variables for cipher and Three.js are the same as your last provided version)
        let scene, camera, renderer, stars, starGeo, dustClouds, dustGeo, matrixGlobe;
        let particleSpeed = 0.2;
        const speedController = {{ speed: 0.2 }};
        const initialStarSize = 0.5;
        const initialDustSize = 100;
        const GLOBE_RADIUS = 40;
        let activeArcs = [];
        let activeTowers = [];
        let messageInput, shiftInput, encryptBtn, decryptBtn, resultP, errorDiv, copyBtn;

        // --- Caesar Cipher Functions ---
        // (validateInputs, caesarCipher are the same as your last provided version)
        function validateInputs() {{
            errorDiv.textContent = '';
            const message = messageInput.value;
            const shiftStr = shiftInput.value;
            if (message.trim() === "" && message.length > 0 && !message.includes(" ")) {{
            }} else if (message.trim() === "" && message.length === 0) {{
                 errorDiv.textContent = 'Datastream cannot be empty.';
                 return null;
            }}
            for (let i = 0; i < message.length; i++) {{
                if (!/^[a-zA-Z]$/.test(message[i]) && message[i] !== ' ') {{
                    errorDiv.textContent = 'Datastream: alphabetic characters or spaces only. Invalid: "' + message[i] + '"';
                    return null;
                }}
            }}
            const shift = parseInt(shiftStr);
            if (isNaN(shift) || shift < 1 || shift > 25) {{
                errorDiv.textContent = 'Quantum Shift: integer 1-25.';
                return null;
            }}
            return {{ message, shift }};
        }}
        function caesarCipher(text, shift, encrypt) {{
            let result_str = '';
            for (let i = 0; i < text.length; i++) {{
                let char = text[i];
                if (char === ' ') {{ result_str += ' '; continue; }}
                let code = text.charCodeAt(i);
                let base = (code >= 65 && code <= 90) ? 65 : 97;
                let shiftedCode = encrypt ? ((code - base + shift) % 26) + base : ((code - base - shift + 26) % 26) + base;
                result_str += String.fromCharCode(shiftedCode);
            }}
            return result_str;
        }}

        // --- Three.js Background (Right Column) ---
        // (initThreeJSVisualization, latLonToVector3, createArc, createCommitTower, createRandomArcAndTowers,
        //  onWindowResizeRightColumn, animateParticles, animateVisualization, startHyperspeedSequenceForRightColumn)
        //  These functions are identical to your provided version.

        function initThreeJSVisualization() {{
            const container = document.getElementById('right-column');
            if (!container || container.clientWidth === 0 || container.clientHeight === 0) {{
                return false;
            }}
            scene = new THREE.Scene();
            camera = new THREE.PerspectiveCamera(60, container.clientWidth / container.clientHeight, 0.1, 2000);
            camera.position.set(0, GLOBE_RADIUS * 0.5, GLOBE_RADIUS * 2.5);
            camera.lookAt(0,0,0);
            renderer = new THREE.WebGLRenderer({{ canvas: document.getElementById('background-canvas'), antialias: true, alpha: true }});
            renderer.setSize(container.clientWidth, container.clientHeight);
            renderer.setPixelRatio(window.devicePixelRatio);
            const ambientLight = new THREE.AmbientLight(0x507090, 0.7); scene.add(ambientLight);
            const directionalLight = new THREE.DirectionalLight(0xffffff, 0.5); directionalLight.position.set(0.5, 1, 1.5); scene.add(directionalLight);
            starGeo = new THREE.BufferGeometry();
            const starVertices = []; const starColorsAttribute = []; const numStars = 8000;
            const starColor = new THREE.Color(); const baseStarColors = [0x88aaff, 0xffffff, 0xbbddff];
            for (let i = 0; i < numStars; i++) {{
                const x = THREE.MathUtils.randFloatSpread(1500); const y = THREE.MathUtils.randFloatSpread(1500);
                const z = THREE.MathUtils.randFloat(-1000, -300);
                starVertices.push(x, y, z);
                starColor.setHex(baseStarColors[Math.floor(Math.random() * baseStarColors.length)]);
                starColor.offsetHSL(Math.random() * 0.1 - 0.05, Math.random() * 0.1 - 0.05, Math.random() * 0.1 - 0.05);
                starColorsAttribute.push(starColor.r, starColor.g, starColor.b);
            }}
            starGeo.setAttribute('position', new THREE.Float32BufferAttribute(starVertices, 3));
            starGeo.setAttribute('color', new THREE.Float32BufferAttribute(starColorsAttribute, 3));
            const starMaterial = new THREE.PointsMaterial({{ size: initialStarSize, sizeAttenuation: true, transparent: true, opacity: 0.8, vertexColors: true }});
            stars = new THREE.Points(starGeo, starMaterial); scene.add(stars);
            dustGeo = new THREE.BufferGeometry();
            const dustVertices = []; const dustColorsAttribute = []; const numDustParticles = 150;
            const dustBaseColor = new THREE.Color(0x100020);
            for (let i = 0; i < numDustParticles; i++) {{
                const x = THREE.MathUtils.randFloatSpread(1800); const y = THREE.MathUtils.randFloatSpread(1800);
                const z = THREE.MathUtils.randFloat(-1200, -500);
                dustVertices.push(x, y, z);
                const c = dustBaseColor.clone();
                c.offsetHSL(Math.random() * 0.1 - 0.05, Math.random()*0.2 - 0.1, Math.random()*0.2-0.1);
                dustColorsAttribute.push(c.r, c.g, c.b);
            }}
            dustGeo.setAttribute('position', new THREE.Float32BufferAttribute(dustVertices, 3));
            dustGeo.setAttribute('color', new THREE.Float32BufferAttribute(dustColorsAttribute, 3));
            const dustMaterial = new THREE.PointsMaterial({{ size: initialDustSize, sizeAttenuation: true, transparent: true, opacity: 0.05, vertexColors: true }});
            dustClouds = new THREE.Points(dustGeo, dustMaterial); scene.add(dustClouds);
            const globePointsGeometry = new THREE.SphereGeometry(GLOBE_RADIUS, 24, 18);
            const globePointsMaterial = new THREE.PointsMaterial({{ color: 0x00ffaa, size: 0.8, sizeAttenuation: true, transparent: true, opacity: 0.7 }});
            matrixGlobe = new THREE.Points(globePointsGeometry, globePointsMaterial); scene.add(matrixGlobe);
            window.addEventListener('resize', onWindowResizeRightColumn, false);
            animateVisualization(); setInterval(createRandomArcAndTowers, 800); return true;
        }}
        function latLonToVector3(lat, lon, radius, targetVector = null) {{ /* ... same ... */
            const vec = targetVector || new THREE.Vector3();
            const phi = (90 - lat) * (Math.PI / 180);
            const theta = (lon + 180) * (Math.PI / 180);
            vec.set(-(radius * Math.sin(phi) * Math.cos(theta)), radius * Math.cos(phi), radius * Math.sin(phi) * Math.sin(theta));
            return vec;
        }}
        const tempStartVec = new THREE.Vector3(); const tempEndVec = new THREE.Vector3();
        const tempControlPoint = new THREE.Vector3(); const tempMidPoint = new THREE.Vector3();
        function createArc(startLatLon, endLatLon, globeRadius) {{ /* ... same ... */
            latLonToVector3(startLatLon.lat, startLatLon.lon, globeRadius, tempStartVec);
            latLonToVector3(endLatLon.lat, endLatLon.lon, globeRadius, tempEndVec);
            tempMidPoint.addVectors(tempStartVec, tempEndVec).multiplyScalar(0.5);
            const dist = tempStartVec.distanceTo(tempEndVec);
            const arcHeight = Math.min(dist * 0.4, globeRadius * 0.5);
            tempControlPoint.copy(tempMidPoint).normalize().multiplyScalar(globeRadius + arcHeight);
            const curve = new THREE.CubicBezierCurve3(tempStartVec, tempControlPoint, tempControlPoint, tempEndVec);
            const points = curve.getPoints(30);
            const geometry = new THREE.BufferGeometry().setFromPoints(points);
            geometry.setDrawRange(0, 0);
            const material = new THREE.LineBasicMaterial({{ color: 0x33ff88, transparent: true, opacity: 0.9, depthTest: false }});
            const arcLine = new THREE.Line(geometry, material);
            arcLine.userData = {{ curve, startPos: tempStartVec.clone(), endPos: tempEndVec.clone() }};
            return arcLine;
        }}
        function createCommitTower(position, isSender) {{ /* ... same ... */
            const towerHeight = GLOBE_RADIUS * 0.15; const towerRadius = GLOBE_RADIUS * 0.015;
            const geometry = new THREE.CylinderGeometry(towerRadius, towerRadius, towerHeight, 8);
            const material = new THREE.MeshBasicMaterial({{ color: isSender ? 0x55ffaa : 0x00ddcc, transparent: true, opacity: 0.85 }});
            const tower = new THREE.Mesh(geometry, material);
            tower.position.copy(position);
            tower.quaternion.setFromUnitVectors(new THREE.Vector3(0, 1, 0), position.clone().normalize());
            tower.translateY(towerHeight / 2);
            tower.scale.set(1, 0.01, 1);
            return tower;
        }}
        function createRandomArcAndTowers() {{ /* ... same ... */
            if (!matrixGlobe || !scene || activeArcs.length > 25) return;
            const startLatLon = {{ lat: THREE.MathUtils.randFloat(-80, 80), lon: THREE.MathUtils.randFloat(-180, 180) }};
            const endLatLon = {{ lat: THREE.MathUtils.randFloat(-80, 80), lon: THREE.MathUtils.randFloat(-180, 180) }};
            if (Math.abs(startLatLon.lat - endLatLon.lat) < 30 && Math.abs(startLatLon.lon - endLatLon.lon) < 30) {{
                endLatLon.lon = (endLatLon.lon + THREE.MathUtils.randFloat(60, 180)) % 360 - 180;
            }}
            const arc = createArc(startLatLon, endLatLon, GLOBE_RADIUS);
            matrixGlobe.add(arc); activeArcs.push(arc);
            const senderTower = createCommitTower(arc.userData.startPos, true);
            const receiverTower = createCommitTower(arc.userData.endPos, false);
            matrixGlobe.add(senderTower, receiverTower); activeTowers.push(senderTower, receiverTower);
            const totalPoints = arc.geometry.attributes.position.count;
            const arcDrawDuration = 1200; const towerAnimDuration = 400;
            const fadeDelay = 300; const fadeDuration = 800;
            anime({{
                targets: [senderTower.scale, receiverTower.scale], y: 1, duration: towerAnimDuration, easing: 'easeOutQuad',
                complete: () => anime({{ targets: [senderTower.scale, receiverTower.scale], y: 0.01, duration: towerAnimDuration, delay: arcDrawDuration - towerAnimDuration * 1.5, easing: 'easeInQuad' }})
            }});
            anime({{
                targets: arc.geometry.drawRange, count: totalPoints, duration: arcDrawDuration, easing: 'easeInOutSine',
                complete: () => anime({{
                    targets: [arc.material, senderTower.material, receiverTower.material], opacity: 0, duration: fadeDuration, delay: fadeDelay, easing: 'linear',
                    complete: () => {{
                        matrixGlobe.remove(arc, senderTower, receiverTower);
                        arc.geometry.dispose(); arc.material.dispose();
                        senderTower.geometry.dispose(); senderTower.material.dispose();
                        receiverTower.geometry.dispose(); receiverTower.material.dispose();
                        activeArcs = activeArcs.filter(a => a !== arc);
                        activeTowers = activeTowers.filter(t => t !== senderTower && t !== receiverTower);
                    }}
                }})
            }});
        }}
        function onWindowResizeRightColumn() {{ /* ... same, with valid dimension check ... */
            const container = document.getElementById('right-column');
            if (camera && renderer && container && container.clientWidth > 0 && container.clientHeight > 0) {{
                camera.aspect = container.clientWidth / container.clientHeight;
                camera.updateProjectionMatrix();
                renderer.setSize(container.clientWidth, container.clientHeight);
            }}
        }}
        function animateParticles(geometry, currentSpeed, respawnZFar, respawnZNear, scatterFactor) {{ /* ... same, with camera check ... */
            if (!geometry) return;
            const positions = geometry.attributes.position.array;
            for (let i = 0; i < positions.length; i += 3) {{
                positions[i+2] += currentSpeed * 2;
                if (camera && positions[i+2] > camera.position.z) {{
                    positions[i+2] = respawnZNear - Math.random() * Math.abs(respawnZFar - respawnZNear);
                    positions[i] = THREE.MathUtils.randFloatSpread(scatterFactor);
                    positions[i+1] = THREE.MathUtils.randFloatSpread(scatterFactor);
                }}
            }}
            geometry.attributes.position.needsUpdate = true;
        }}
        let initialHyperspeedDone = false;
        function animateVisualization() {{ /* ... same, with scene/camera guard ... */
            requestAnimationFrame(animateVisualization);
            if (!scene || !camera) return;
            if (initialHyperspeedDone) {{
                 animateParticles(starGeo, speedController.speed, -900, -1000, 1200);
                 animateParticles(dustGeo, speedController.speed * 0.1, -1100, -1200, 1500);
            }}
            if (stars && stars.material) {{ stars.material.opacity = 0.6 + Math.sin(Date.now() * 0.0005) * 0.2; }}
            if (dustClouds && dustClouds.material) {{ dustClouds.material.opacity = 0.03 + Math.sin(Date.now() * 0.0002) * 0.01; }}
            if (matrixGlobe) {{ matrixGlobe.rotation.y += 0.0015; matrixGlobe.rotation.x += 0.0003; }}
            if (renderer) {{ renderer.render(scene, camera); }}
        }}
        function startHyperspeedSequenceForRightColumn() {{ /* ... same, with container check and corrected typo ... */
            const rightColContainer = document.getElementById('right-column');
            if (!camera || typeof anime === 'undefined' || !stars || !stars.material || !rightColContainer || rightColContainer.clientWidth === 0) {{
                initialHyperspeedDone = true;
                return;
            }}
            const initialCamPos = {{ x: 0, y: GLOBE_RADIUS * 2, z: GLOBE_RADIUS * 8 }};
            const targetCamPos = {{ x: 0, y: GLOBE_RADIUS * 0.3, z: GLOBE_RADIUS * 2.2 }};
            camera.position.set(initialCamPos.x, initialCamPos.y, initialCamPos.z); // Corrected typo here
            if(matrixGlobe) camera.lookAt(matrixGlobe.position); else camera.lookAt(0,0,0);
            const originalParticleSpeed = speedController.speed;
            speedController.speed = 20;
            const tl = anime.timeline({{
                easing: 'easeInOutSine',
                complete: () => {{ speedController.speed = originalParticleSpeed; initialHyperspeedDone = true; }}
            }});
            tl.add({{ targets: camera.position, x: targetCamPos.x, y: targetCamPos.y, z: targetCamPos.z, duration: 3500, easing: 'easeOutExpo', update: () => {{ if(matrixGlobe) camera.lookAt(matrixGlobe.position); else camera.lookAt(0,0,0); }} }})
            .add({{ targets: camera, fov: 45, duration: 2000, easing: 'easeInOutQuad', update: () => camera.updateProjectionMatrix() }}, '-=3000')
            .add({{ targets: stars.material, size: initialStarSize * 3, duration: 1500, easing: 'easeInExpo' }}, '-=2800')
            .add({{ targets: camera, fov: 60, duration: 2500, easing: 'easeOutQuad', update: () => camera.updateProjectionMatrix() }}, '-=1000')
            .add({{ targets: stars.material, size: initialStarSize, duration: 2000, easing: 'easeOutExpo' }}, '-=2000');
        }}

        // --- DOMContentLoaded ---
        document.addEventListener('DOMContentLoaded', () => {{
            messageInput = document.getElementById('message');
            shiftInput = document.getElementById('shift');
            encryptBtn = document.getElementById('encrypt-btn');
            decryptBtn = document.getElementById('decrypt-btn');
            resultP = document.getElementById('result');
            errorDiv = document.getElementById('error-message');
            copyBtn = document.getElementById('copy-result-btn');

            encryptBtn.addEventListener('click', () => {{
                const inputs = validateInputs();
                if (inputs) {{ resultP.textContent = caesarCipher(inputs.message, inputs.shift, true); }}
                else {{ resultP.textContent = ''; }}
            }});
            decryptBtn.addEventListener('click', () => {{
                const inputs = validateInputs();
                if (inputs) {{ resultP.textContent = caesarCipher(inputs.message, inputs.shift, false); }}
                else {{ resultP.textContent = ''; }}
            }});
            copyBtn.addEventListener('click', () => {{
                 if (resultP.textContent) {{
                    navigator.clipboard.writeText(resultP.textContent)
                        .then(() => {{
                            copyBtn.textContent = 'Copied!'; copyBtn.classList.add('copied');
                            setTimeout(() => {{ copyBtn.textContent = 'Copy'; copyBtn.classList.remove('copied'); }}, 1500);
                        }})
                        .catch(err => {{ console.error('Copy fail: ', err); copyBtn.textContent = 'Fail!'; }});
                }}
            }});

            let attempts = 0; const maxAttempts = 30;
            function tryInit3D() {{
                const rightColContainer = document.getElementById('right-column');
                if (typeof THREE !== 'undefined' && typeof anime !== 'undefined') {{
                    if (initThreeJSVisualization()) {{
                        startHyperspeedSequenceForRightColumn();
                    }} else if (attempts < maxAttempts) {{
                        attempts++; setTimeout(tryInit3D, 100);
                    }} else {{
                        console.error("Right column container not ready for 3D init after multiple attempts.");
                        if (rightColContainer) rightColContainer.innerHTML = "<p style='color:orange;text-align:center;margin-top:50px;'>3D View Area Not Ready</p>";
                    }}
                }} else {{
                    console.error("Three.js or Anime.js not loaded.");
                     if (rightColContainer) rightColContainer.innerHTML = "<p style='color:orange;text-align:center;margin-top:50px;'>Required Libraries Missing for 3D View</p>";
                }}
            }}
            tryInit3D();
        }});
    </script>
</body>
</html>
    """
    return html_content

if __name__ == '__main__':
    app.run(debug=True)
