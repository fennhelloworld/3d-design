# 3D Design

3D design & printing with OpenSCAD/SolidPython/FreeCAD, AI-assisted via Claude Code & Codex.

## Overview

This repository implements a **programmatic 3D design workflow** using Python-based tools for model generation, OpenSCAD for rendering, and FreeCAD for mechanical design. The approach treats 3D modeling as code — enabling parametric design, version control, and AI-assisted iteration.

## Toolchain

| Tool | Version | Purpose |
|------|---------|---------|
| [SolidPython2](https://github.com/jeff-dh/SolidPython) | 2.1.3 | Programmatic 3D model generation in Python |
| [OpenSCAD](https://openscad.org/) | 2021.01 | CSG rendering and STL export |
| [FreeCAD](https://www.freecad.org/) | 0.21.2 | Mechanical design and STEP export |
| Claude Code | 2.1.118 | AI-assisted 3D design & code generation |
| Codex CLI | 0.135.0 | AI-assisted design exploration |

## Directory Structure

```
3d-design/
├── models/     # SolidPython/OpenSCAD model source files
├── prints/     # Print settings and project files
├── lib/        # Reusable modules, utilities, and MCAD parts
├── stl/        # Generated STL files for printing
├── gcode/      # Sliced G-code files ready for printing
└── docs/       # Design notes, print logs, and references
```

## Workflow

1. **Model** — Write SolidPython2 scripts that generate OpenSCAD geometry programmatically
2. **Render** — Compile to OpenSCAD and render STL files
3. **Slice** — Convert STL to G-code for 3D printing
4. **Print** — Send G-code to printer and document results

### Quick Start

```python
# models/enclosure.py
from solid2 import *

# Parametric enclosure generator
def enclosure(length=100, width=60, height=30, wall=2, tolerance=0.2):
    outer = cube([length, width, height])
    inner = translate([wall, wall, wall])(
        cube([length - 2*wall - tolerance,
              width - 2*wall - tolerance,
              height])
    )
    return outer - inner

model = enclosure()
model.save_as_scad("enclosure.scad")
```

```bash
# Render to STL
~/Applications/OpenSCAD.AppImage -o stl/enclosure.stl models/enclosure.scad
```

## Focus Areas

- **Outdoor filming equipment** — camera housings, drone parts, gear mounts
- **PCB enclosures** — parameterized by board dimensions from circuit-design repo
- **Functional prototypes** — quick iteration with AI-assisted design

## Related

- Part of the [hardware-lab](https://github.com/fennhelloworld/hardware-lab) workspace
- Companion repo: [circuit-design](https://github.com/fennhelloworld/circuit-design) for PCB design
