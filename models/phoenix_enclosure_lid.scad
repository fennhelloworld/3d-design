difference() {
	union() {
		translate(v = [0, 0, 19.6]) {
			cube(size = [50.0, 35.0, 3.0]);
		}
		translate(v = [2.0, 2.0, 18.1]) {
			cube(size = [46.0, 31.0, 4.5]);
		}
		union() {
			translate(v = [4.5, 4.5, 18.1]) {
				cylinder(h = 4.5, r = 2.0);
			}
			translate(v = [45.5, 4.5, 18.1]) {
				cylinder(h = 4.5, r = 2.0);
			}
			translate(v = [4.5, 30.5, 18.1]) {
				cylinder(h = 4.5, r = 2.0);
			}
			translate(v = [45.5, 30.5, 18.1]) {
				cylinder(h = 4.5, r = 2.0);
			}
		}
	}
	union() {
		translate(v = [4.5, 4.5, 18.1]) {
			cylinder(h = 5.5, r = 0.8);
		}
		translate(v = [45.5, 4.5, 18.1]) {
			cylinder(h = 5.5, r = 0.8);
		}
		translate(v = [4.5, 30.5, 18.1]) {
			cylinder(h = 5.5, r = 0.8);
		}
		translate(v = [45.5, 30.5, 18.1]) {
			cylinder(h = 5.5, r = 0.8);
		}
	}
	union() {
		union() {
			union() {
				union() {
					union();
					translate(v = [5.0, 5.0, 19.59]) {
						cube(size = [5, 25.0, 2.02]);
					}
				}
				translate(v = [14.0, 5.0, 19.59]) {
					cube(size = [5, 25.0, 2.02]);
				}
			}
			translate(v = [23.0, 5.0, 19.59]) {
				cube(size = [5, 25.0, 2.02]);
			}
		}
		translate(v = [32.0, 5.0, 19.59]) {
			cube(size = [5, 25.0, 2.02]);
		}
	}
}
