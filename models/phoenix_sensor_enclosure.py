"""LeoDrone Phoenix - ESP32-S3 Sensor Node Enclosure
SolidPython2 → OpenSCAD → STL for 3D Printing
"""
import sys
sys.path.insert(0, '/home/fenn/.local/lib/python3.10/site-packages')
from solid2 import (cube, cylinder, difference, translate, union, 
                    rotate, color, hull, linear_extrude, circle, text)
from solid2 import scad_render_to_file
import os

# ============================================================
# PCB Dimensions (based on circuit design)
# ============================================================
pcb_x = 45.0   # ESP32-S3 module width
pcb_y = 30.0   # Depth
pcb_z = 1.6    # Standard PCB thickness
pcb_comp_h = 12.0  # Max component height above PCB (ESP32-S3 module)

# ============================================================
# Enclosure Parameters
# ============================================================
wall = 2.0          # Wall thickness (min for FDM: 1.2mm)
clearance = 0.5     # PCB-to-wall clearance
floor_h = 2.0       # Bottom floor thickness
post_r = 2.0        # Mounting post radius
post_h = 5.0        # Post height
screw_r = 0.8       # Screw hole radius (M1.6)

# Outer dimensions
outer_x = pcb_x + 2 * (wall + clearance)
outer_y = pcb_y + 2 * (wall + clearance)
outer_z = floor_h + pcb_z + post_h + pcb_comp_h + wall  # Total height

# Lid dimensions
lid_h = wall + 1.0  # Lid thickness + lip
lid_lip = 1.5       # Lip depth into body

# ============================================================
# Bottom Shell
# ============================================================
body = cube([outer_x, outer_y, outer_z - lid_h])

# Hollow interior
inner = translate([wall, wall, floor_h])(
    cube([outer_x - 2*wall, outer_y - 2*wall, outer_z - lid_h - floor_h + 1])
)

# Mounting posts (4 corners)
post_x_off = wall + clearance + post_r
post_y_off = wall + clearance + post_r
posts = union()(
    translate([post_x_off, post_y_off, floor_h])(cylinder(r=post_r, h=post_h)),
    translate([outer_x - post_x_off, post_y_off, floor_h])(cylinder(r=post_r, h=post_h)),
    translate([post_x_off, outer_y - post_y_off, floor_h])(cylinder(r=post_r, h=post_h)),
    translate([outer_x - post_x_off, outer_y - post_y_off, floor_h])(cylinder(r=post_r, h=post_h)),
)

# Screw holes in posts
screw_holes = union()(
    translate([post_x_off, post_y_off, floor_h])(cylinder(r=screw_r, h=post_h + 1)),
    translate([outer_x - post_x_off, post_y_off, floor_h])(cylinder(r=screw_r, h=post_h + 1)),
    translate([post_x_off, outer_y - post_y_off, floor_h])(cylinder(r=screw_r, h=post_h + 1)),
    translate([outer_x - post_x_off, outer_y - post_y_off, floor_h])(cylinder(r=screw_r, h=post_h + 1)),
)

# Wire exit hole (side, for UART cable)
wire_hole = translate([outer_x / 2 - 4, -1, floor_h + 3])(
    cube([8, wall + 2, 5])
)

# I2C connector access (side)
i2c_hole = translate([-1, outer_y / 2 - 3, floor_h + post_h + 2])(
    cube([wall + 2, 6, 4])
)

# Antenna slot (for ESP32-S3 PCB antenna)
antenna_slot = translate([outer_x - wall - 1, outer_y / 2 - 5, floor_h + post_h])(
    cube([wall + 2, 10, 8])
)

# BME280 ventilation holes (top would be in lid, put on side instead)
vent_holes = union()
for i in range(4):
    vent_holes = union()(
        vent_holes,
        translate([wall + 4 + i * 9, -1, floor_h + 8])(
            cube([5, wall + 2, 2])
        )
    )

# Assemble bottom
bottom = difference()(
    body,
    inner,
    wire_hole,
    i2c_hole,
    antenna_slot,
)
bottom = union()(bottom, posts)
bottom = difference()(bottom, screw_holes, vent_holes)

# ============================================================
# Top Lid
# ============================================================
lid_z = outer_z - lid_h

lid_body = translate([0, 0, lid_z])(cube([outer_x, outer_y, lid_h]))

# Lip (fits inside body)
lid_lip_geom = translate([wall, wall, lid_z - lid_lip])(
    cube([outer_x - 2*wall, outer_y - 2*wall, lid_lip + lid_h])
)

# Lid screw bosses
lid_bosses = union()(
    translate([post_x_off, post_y_off, lid_z - lid_lip])(cylinder(r=post_r, h=lid_lip + lid_h)),
    translate([outer_x - post_x_off, post_y_off, lid_z - lid_lip])(cylinder(r=post_r, h=lid_lip + lid_h)),
    translate([post_x_off, outer_y - post_y_off, lid_z - lid_lip])(cylinder(r=post_r, h=lid_lip + lid_h)),
    translate([outer_x - post_x_off, outer_y - post_y_off, lid_z - lid_lip])(cylinder(r=post_r, h=lid_lip + lid_h)),
)

lid_screw_holes = union()(
    translate([post_x_off, post_y_off, lid_z - lid_lip])(cylinder(r=screw_r, h=lid_lip + lid_h + 1)),
    translate([outer_x - post_x_off, post_y_off, lid_z - lid_lip])(cylinder(r=screw_r, h=lid_lip + lid_h + 1)),
    translate([post_x_off, outer_y - post_y_off, lid_z - lid_lip])(cylinder(r=screw_r, h=lid_lip + lid_h + 1)),
    translate([outer_x - post_x_off, outer_y - post_y_off, lid_z - lid_lip])(cylinder(r=screw_r, h=lid_lip + lid_h + 1)),
)

# BME280 vent on top lid (4 slits for airflow)
lid_vents = union()
for i in range(4):
    lid_vents = union()(
        lid_vents,
        translate([wall + 3 + i * 9, wall + 3, lid_z - 0.01])(
            cube([5, outer_y - 2*wall - 6, wall + 0.02])
        )
    )

# Assemble lid
lid = union()(lid_body, lid_lip_geom, lid_bosses)
lid = difference()(lid, lid_screw_holes, lid_vents)

# ============================================================
# Full Assembly
# ============================================================
full = union()(
    color("#2196F3")(bottom),   # Blue body
    color("#90CAF9")(lid),      # Light blue lid
)

# ============================================================
# Export
# ============================================================
model_dir = "/home/fenn/projects/3d-design/models"
stl_dir = "/home/fenn/projects/3d-design/stl"
os.makedirs(model_dir, exist_ok=True)
os.makedirs(stl_dir, exist_ok=True)

# Full assembly (for visualization)
scad_render_to_file(full, os.path.join(model_dir, 'phoenix_sensor_enclosure.scad'))

# Bottom only (for separate printing)
scad_render_to_file(bottom, os.path.join(model_dir, 'phoenix_enclosure_bottom.scad'))

# Lid only
scad_render_to_file(lid, os.path.join(model_dir, 'phoenix_enclosure_lid.scad'))

print(f"OpenSCAD files generated:")
print(f"  Full: {model_dir}/phoenix_sensor_enclosure.scad")
print(f"  Bottom: {model_dir}/phoenix_enclosure_bottom.scad")
print(f"  Lid: {model_dir}/phoenix_enclosure_lid.scad")
print(f"\nEnclosure dims: {outer_x:.0f}x{outer_y:.0f}x{outer_z:.0f}mm")
print(f"PCB cavity: {pcb_x:.0f}x{pcb_y:.0f}mm")
print(f"Wall: {wall}mm | Floor: {floor_h}mm | Posts: M1.6 @ {post_h}mm")
