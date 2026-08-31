import trimesh
import numpy as np

# 1. Create a scene container for our 3D objects
scene = trimesh.Scene()

rows = 5
columns = 5

print("=== Generating 3D Grid for Python 3.14 ===")

for x in range(rows):
    for y in range(columns):
        # 2. Create a basic 3D cube mesh (size 1x1x1)
        cube = trimesh.creation.box(extents=[1, 1, 1])
        
        # 3. Calculate position with spacing
        x_pos = x * 1.5
        y_pos = y * 1.5
        z_pos = 0
        
        # Move the cube to its grid coordinates
        cube.apply_translation([x_pos, y_pos, z_pos])
        
        # Color it (RGBA format: Red, Green, Blue, Alpha)
        cube.visual.face_colors = [0, 200, 255, 255] # Cyan color
        
        # 4. Add the finished cube to our scene
        scene.add_geometry(cube)

print("Generation complete! Saving 3D file...")

# 5. Export this directly as a 3D file you can open in a game engine!
scene.export("game_grid.obj")
print("Saved asset as 'game_grid.obj' in your folder.")

# Try to show the interactive pop-up window
try:
    scene.show()
except Exception:
    print("Window viewer skipped. Check your folder for the 'game_grid.obj' file!")
