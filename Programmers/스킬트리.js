function solution(skill, skill_trees) {
	var answer = 0;

	for (let user of skill_trees) {
		let cnt = 0;
		let idx = 0;
		for (let i of user) {
			if (skill.includes(i)) {
				if (skill.search(i) !== idx) {
					break;
				} else {
					idx += 1;
					cnt += 1;
				}
			} else {
				cnt += 1;
				continue;
			}
		}
		if (cnt === user.length) {
			answer += 1;
		}
	}

	return answer;
}
