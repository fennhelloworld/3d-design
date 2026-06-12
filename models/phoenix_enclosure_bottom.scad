difference() {
	union() {
		difference() {
			cube(size = [50.0, 35.0, 19.6]);
			translate(v = [2.0, 2.0, 2.0]) {
				cube(size = [46.0, 31.0, 18.6]);
			}
			translate(v = [21.0, -1, 5.0]) {
				cube(size = [8, 4.0, 5]);
			}
			translate(v = [-1, 14.5, 9.0]) {
				cube(size = [4.0, 6, 4]);
			}
			translate(v = [47.0, 12.5, 7.0]) {
				cube(size = [4.0, 10, 8]);
			}
		}
		union() {
			translate(v = [4.5, 4.5, 2.0]) {
				cylinder(h = 5.0, r = 2.0);
			}
			translate(v = [45.5, 4.5, 2.0]) {
				cylinder(h = 5.0, r = 2.0);
			}
			translate(v = [4.5, 30.5, 2.0]) {
				cylinder(h = 5.0, r = 2.0);
			}
			translate(v = [45.5, 30.5, 2.0]) {
				cylinder(h = 5.0, r = 2.0);
			}
		}
	}
	union() {
		translate(v = [4.5, 4.5, 2.0]) {
			cylinder(h = 6.0, r = 0.8);
		}
		translate(v = [45.5, 4.5, 2.0]) {
			cylinder(h = 6.0, r = 0.8);
		}
		translate(v = [4.5, 30.5, 2.0]) {
			cylinder(h = 6.0, r = 0.8);
		}
		translate(v = [45.5, 30.5, 2.0]) {
			cylinder(h = 6.0, r = 0.8);
		}
	}
	union() {
		union() {
			union() {
				union() {
					union();
					translate(v = [6.0, -1, 10.0]) {
						cube(size = [5, 4.0, 2]);
					}
				}
				translate(v = [15.0, -1, 10.0]) {
					cube(size = [5, 4.0, 2]);
				}
			}
			translate(v = [24.0, -1, 10.0]) {
				cube(size = [5, 4.0, 2]);
			}
		}
		translate(v = [33.0, -1, 10.0]) {
			cube(size = [5, 4.0, 2]);
		}
	}
}
