function solution(users, emoticons) {
	let answer = [0, 0];
	const cases = [10, 20, 30, 40];
	const arr = [];

	function pwc(items, index, k, lst, result) {
		if (items.length === k) {
			result.push(items);
			return;
		}

		for (let i = index; i < lst.length; i++) {
			pwc([...items, lst[i]], 0, k, lst, result);
		}
	}

	pwc([], 0, emoticons.length, cases, arr);

	for (i of arr) {
		let total = 0;
		let cnt = 0;
		for (let j = 0; j < users.length; j++) {
			let temp = 0;
			for (let k = 0; k < emoticons.length; k++) {
				if (i[k] >= users[j][0]) {
					temp += (emoticons[k] * (100 - i[k])) / 100;
				}
				if (temp >= users[j][1]) {
					cnt += 1;
					temp = 0;
					break;
				}
			}
			total += temp;
		}

		if (answer[0] < cnt) {
			answer[0] = cnt;
			answer[1] = total;
		} else if (answer[0] === cnt && answer[1] < total) {
			answer[1] = total;
		}
	}

	return answer;
}
