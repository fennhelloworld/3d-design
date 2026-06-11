difference() {
	union() {
		difference() {
			cube(size = [55.0, 35.0, 6.55]);
			translate(v = [2.0, 2.0, 2.0]) {
				cube(size = [51.0, 31.0, 6.55]);
			}
			translate(v = [24.5, -1, 4.0]) {
				cube(size = [6, 4.0, 4]);
			}
			translate(v = [23.5, 32.0, 4.0]) {
				cube(size = [8, 4.0, 5]);
			}
		}
		union() {
			translate(v = [4.5, 4.5, 2.0]) {
				cylinder(h = 5.0, r = 2.0);
			}
			translate(v = [50.5, 4.5, 2.0]) {
				cylinder(h = 5.0, r = 2.0);
			}
			translate(v = [4.5, 30.5, 2.0]) {
				cylinder(h = 5.0, r = 2.0);
			}
			translate(v = [50.5, 30.5, 2.0]) {
				cylinder(h = 5.0, r = 2.0);
			}
		}
	}
	union() {
		translate(v = [4.5, 4.5, 2.0]) {
			cylinder(h = 6.0, r = 1.0);
		}
		translate(v = [50.5, 4.5, 2.0]) {
			cylinder(h = 6.0, r = 1.0);
		}
		translate(v = [4.5, 30.5, 2.0]) {
			cylinder(h = 6.0, r = 1.0);
		}
		translate(v = [50.5, 30.5, 2.0]) {
			cylinder(h = 6.0, r = 1.0);
		}
	}
}
