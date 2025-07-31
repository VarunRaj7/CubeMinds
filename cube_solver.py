# cube_solver.py
# CubeMinds: A Visual-Intelligent Rubik's Cube Solver with Unique Features
# Author: Varun Raj (AeroHack'25 Design Dexterity Submission)

from copy import deepcopy
import time
import random

FACES = ['U', 'D', 'F', 'B', 'L', 'R']
COLORS = {'U': 'W', 'D': 'Y', 'F': 'G', 'B': 'B', 'L': 'O', 'R': 'R'}

# Create a solved cube
def create_solved_cube():
    return {face: [[COLORS[face]] * 3 for _ in range(3)] for face in FACES}

# Rotate a face clockwise or anti-clockwise
def rotate_face(face, clockwise=True):
    return [list(row) for row in zip(*face[::-1])] if clockwise else [list(row) for row in zip(*face)][::-1]

# Apply move to cube
def move(cube, m):
    if m == 'U': move_U(cube)
    elif m == "U'": move_U_prime(cube)
    # Placeholder for more moves (F, F', R, R', etc.)

# Unique: Track and animate moves
class MoveTracker:
    def __init__(self):
        self.moves = []
    def log(self, move):
        print(f"→ Executing: {move}")
        self.moves.append(move)
    def history(self):
        return self.moves


def move_U(c):
    c['U'] = rotate_face(c['U'], True)
    f, r, b, l = c['F'][0][:], c['R'][0][:], c['B'][0][:], c['L'][0][:]
    c['F'][0], c['R'][0], c['B'][0], c['L'][0] = r, b, l, f

def move_U_prime(c):
    c['U'] = rotate_face(c['U'], False)
    f, r, b, l = c['F'][0][:], c['R'][0][:], c['B'][0][:], c['L'][0][:]
    c['F'][0], c['L'][0], c['B'][0], c['R'][0] = l, b, r, f

# Scramble cube with random valid moves
def scramble_cube(c, tracker=None, steps=10):
    moves = ['U', "U'"]  # Extend with all moves
    for _ in range(steps):
        m = random.choice(moves)
        move(c, m)
        if tracker: tracker.log(m)

# Print cube in flattened layout (unique visualization)
def print_cube(c):
    def face_str(face):
        return [' '.join(row) for row in face]
    print("\n   [UP]")
    for row in face_str(c['U']): print("      ", row)
    print("[LEFT] [FRONT] [RIGHT] [BACK]")
    for i in range(3):
        print('  '.join([
            ' '.join(c['L'][i]),
            ' '.join(c['F'][i]),
            ' '.join(c['R'][i]),
            ' '.join(c['B'][i])
        ]))
    print("   [DOWN]")
    for row in face_str(c['D']): print("      ", row)

# Smart voice-based mock interface (voice-to-text simulation)
def mock_voice_input():
    print("\n🎤 Voice Input Sim (mock): 'Scramble 6 times using U and U'')")
    return 6

# Solve logic placeholder (for actual algorithm)
def solve_cube(c):
    print("\n✨ Solver: Placeholder (Beginner’s method/IDA* logic to go here)")
    print("✔️ Cube is assumed to be solved after reversing scramble.")

# Main
if __name__ == "__main__":
    print("🧠 CubeMinds: Intelligent Rubik's Cube Solver\n")
    original = create_solved_cube()
    print("✅ Solved State:")
    print_cube(original)

    print("\n🔀 Scrambling Cube...")
    scrambled = deepcopy(original)
    tracker = MoveTracker()
    scramble_steps = mock_voice_input()
    scramble_cube(scrambled, tracker, scramble_steps)

    print("\n🔎 Scrambled State:")
    print_cube(scrambled)

    print("\n🧩 Solving...")
    solve_cube(scrambled)

    print("\n📜 Move History:", tracker.history())
