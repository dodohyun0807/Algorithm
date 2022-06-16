function solution(progresses, speeds) {
	let answer = [];

	while (progresses.length !== 0) {
		let cnt = 0;

		for (let i = 0; i < speeds.length; i++) {
			progresses[i] += speeds[i];
		}

		while (progresses[0] >= 100) {
			progresses.shift();
			speeds.shift();
			cnt += 1;
		}

		if (cnt > 0) {
			answer.push(cnt);
		}
	}
	return answer;
}
