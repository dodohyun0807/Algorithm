function solution(dirs) {
	let ans = 0;
	let x = 0;
	let y = 0;
	let visited = [];

	for (dir of dirs) {
		if (dir === "U") {
			if (y < 5) {
				y += 1;
				let chk = false;
				visited.forEach((i) => {
					if (
						JSON.stringify(i) ===
							JSON.stringify([y - 1, x, y, x]) ||
						JSON.stringify(i) === JSON.stringify([y, x, y - 1, x])
					) {
						chk = true;
					}
				});
				if (chk === false) {
					visited.push([y - 1, x, y, x]);
					ans += 1;
				}
			}
		}

		if (dir === "D") {
			if (y > -5) {
				y -= 1;
				let chk = false;
				visited.forEach((i) => {
					if (
						JSON.stringify(i) ===
							JSON.stringify([y + 1, x, y, x]) ||
						JSON.stringify(i) === JSON.stringify([y, x, y + 1, x])
					) {
						chk = true;
					}
				});
				if (chk === false) {
					visited.push([y + 1, x, y, x]);
					ans += 1;
				}
			}
		}

		if (dir === "L") {
			if (x > -5) {
				x -= 1;
				let chk = false;
				visited.forEach((i) => {
					if (
						JSON.stringify(i) ===
							JSON.stringify([y, x + 1, y, x]) ||
						JSON.stringify(i) === JSON.stringify([y, x, y, x + 1])
					) {
						chk = true;
					}
				});
				if (chk === false) {
					visited.push([y, x + 1, y, x]);
					ans += 1;
				}
			}
		}

		if (dir === "R") {
			if (x < 5) {
				x += 1;
				let chk = false;
				visited.forEach((i) => {
					if (
						JSON.stringify(i) ===
							JSON.stringify([y, x - 1, y, x]) ||
						JSON.stringify(i) === JSON.stringify([y, x, y, x - 1])
					) {
						chk = true;
					}
				});
				if (chk === false) {
					visited.push([y, x - 1, y, x]);
					ans += 1;
				}
			}
		}
	}

	return ans;
}
