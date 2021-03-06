function solution(numbers) {
	var answer = 0;

	var n = numbers.split("");
	var nums = new Set();
	comb(n, "");

	function comb(a, s) {
		if (s.length > 0) {
			if (nums.has(Number(s)) === false) {
				nums.add(Number(s));
				if (prime(Number(s))) {
					answer++;
				}
			}
		}
		if (a.length > 0) {
			for (var i = 0; i < a.length; i++) {
				var t = a.slice(0);
				t.splice(i, 1);
				comb(t, s + a[i]);
			}
		}
	}

	function prime(num) {
		if (num < 2) return false;
		if (num === 2) return true;
		for (var i = 2; i <= Math.sqrt(num); i++) {
			if (num % i === 0) return false;
		}
		return true;
	}

	return answer;
}
