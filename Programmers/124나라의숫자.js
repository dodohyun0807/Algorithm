function solution(n) {
	let answer = "";
	const nara = ["1", "2", "4"];

	while (true) {
		if (n <= 0) {
			return answer;
		}

		n -= 1;
		answer = nara[n % 3] + answer;
		n = parseInt(n / 3);
	}

	return answer;
}
