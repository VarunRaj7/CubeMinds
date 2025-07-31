Project Name: CubeMinds – A Visual-Intelligent Rubik’s Cube Solver
Hackathon: AeroHack 2025 – Design Dexterity Challenge
Author: Varun Raj

---

📌 OVERVIEW
CubeMinds is a custom-built Rubik’s Cube solver designed to simulate the solving process of a standard 3x3 cube. 
It prioritizes realism, educational clarity, and modular design — with features like animated move tracking, voice-input simulation, and a 3D visual web interface.

---

📂 CONTENTS

1. cube_solver.py
   → Core Python script with cube modelling, move engine, scramble logic, and console visualization.
   → Includes voice-based mock input and move animation simulation.

2. cube_visual.html
   → A browser-based 3D Rubik’s Cube viewer using Three.js.
   → Automatically displays a full 3×3 cube with rotation animation.
   → No internet or install required – just double-click to run locally.

3. AeroHack_CubeMinds.pptx
   → Presentation deck describing the design, approach, features, and outputs of the solution.

4. README.txt
   → You’re reading it now :)

---

⚙️ HOW TO RUN

➤ Run the Solver:
    On macOS/Linux:
        python3 cube_solver.py

    On Windows:
        py cube_solver.py

    Output includes:
    - Solved cube
    - Simulated scramble
    - Scrambled cube
    - Move-by-move solving feedback
    - Move history log

➤ View the 3D Cube:
    - Open `cube_visual.html` in any browser (Chrome, Edge, Safari)
    - Rotate and inspect the cube interactively

---

🚀 UNIQUE FEATURES

✓ Animated move tracker (real-time simulation with delay)
✓ Flattened cube printer for educational step tracking
✓ Mock voice-based user input
✓ Beginner-friendly output
✓ Modular logic to scale to 2x2, 4x4, and CFOP-style solvers
✓ 3D HTML visual with interactive cube using Three.js

---

🛠️ TO EXTEND
- Add support for other moves (R, L, F, B, D, and their primes)
- Integrate actual solver logic (Beginner’s method or IDA*)
- Use webcam or real-time colour scanning (for visual input)

---

📞 CONTACT
Pallekonda Varun Raj  
Email: vp9860@srmist.edu.in, varun.pallekonda@gmail.com 
Phone: 9989295385

