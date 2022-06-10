function solution(clothes) {
	let answer = 0;
	let arr = {};

	for (let i = 0; i < clothes.length; i++) {
		if (arr[clothes[i][1]]) {
			arr[clothes[i][1]].push(clothes[i][0]);
		} else {
			arr[clothes[i][1]] = [clothes[i][0]];
			arr[clothes[i][1]].push(0);
		}
	}

	for (let i in arr) {
		if (answer === 0) {
			answer += arr[i].length;
		} else {
			answer *= arr[i].length;
		}
	}

	return answer - 1;
}
