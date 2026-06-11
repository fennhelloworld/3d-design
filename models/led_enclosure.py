"""LED Driver PCB Enclosure - SolidPython2"""
import sys
sys.path.insert(0, '/home/fenn/.local/lib/python3.10/site-packages')
from solid2 import cube, cylinder, difference, translate, union, color, rotate, hull
from solid2 import scad_render_to_file

# PCB dimensions (mm)
pcb_x, pcb_y, pcb_z = 50, 30, 1.6
wall = 2.0
clearance = 0.5
post_r = 2.0
post_h = 5.0

# Enclosure outer dimensions
outer_x = pcb_x + 2 * (wall + clearance)
outer_y = pcb_y + 2 * (wall + clearance)
outer_z = pcb_z + post_h + wall + clearance

# Bottom shell
bottom = cube([outer_x, outer_y, outer_z / 2 + wall])

# Hollow interior
inner = translate([wall, wall, wall])(
    cube([outer_x - 2*wall, outer_y - 2*wall, outer_z / 2 + wall])
)

# Mounting posts (4 corners)
post_offset = wall + clearance + post_r
posts = union()(
    translate([post_offset, post_offset, wall])(cylinder(r=post_r, h=post_h)),
    translate([outer_x - post_offset, post_offset, wall])(cylinder(r=post_r, h=post_h)),
    translate([post_offset, outer_y - post_offset, wall])(cylinder(r=post_r, h=post_h)),
    translate([outer_x - post_offset, outer_y - post_offset, wall])(cylinder(r=post_r, h=post_h)),
)

# Screw holes in posts
screw_r = 1.0
screw_holes = union()(
    translate([post_offset, post_offset, wall])(cylinder(r=screw_r, h=post_h + 1)),
    translate([outer_x - post_offset, post_offset, wall])(cylinder(r=screw_r, h=post_h + 1)),
    translate([post_offset, outer_y - post_offset, wall])(cylinder(r=screw_r, h=post_h + 1)),
    translate([outer_x - post_offset, outer_y - post_offset, wall])(cylinder(r=screw_r, h=post_h + 1)),
)

# Wire exit hole
wire_hole = translate([outer_x / 2 - 3, -1, wall + 2])(
    cube([6, wall + 2, 4])
)

# LED window
led_window = translate([outer_x / 2 - 4, outer_y - wall - 1, wall + 2])(
    cube([8, wall + 2, 5])
)

# Assemble
enclosure = difference()(
    bottom,
    inner,
    wire_hole,
    led_window,
)
enclosure = union()(enclosure, posts)
enclosure = difference()(enclosure, screw_holes)

# Export
import os
model_dir = os.path.dirname(os.path.abspath(__file__))
scad_path = os.path.join(model_dir, 'led_enclosure.scad')
scad_render_to_file(enclosure, scad_path)
print(f"OpenSCAD file generated: {scad_path}")
