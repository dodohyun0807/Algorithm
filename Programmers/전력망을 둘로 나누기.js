function solution(n, wires) {
	const adjArr = [...Array(n + 1)].map(() => [...Array(n + 1)].map(() => 0));
	const visit = Array(n + 1).fill(0);
	let count = 0;

	wires.forEach(([v1, v2]) => {
		adjArr[v1][v2] = 1;
		adjArr[v2][v1] = 1;
	});

	// 순회
	const dfs = (tower) => {
		visit[tower] = 1;
		count++;

		for (let i = 1; i <= n; i++) {
			adjArr[tower][i] && !visit[i] && dfs(i);
		}
	};

	return wires.reduce((m, [v1, v2]) => {
		// 전선 끊기
		adjArr[v1][v2] = 0;
		adjArr[v2][v1] = 0;
		// 순회
		dfs(1);
		// 전선 회복
		adjArr[v1][v2] = 1;
		adjArr[v2][v1] = 1;

		m = Math.min(m, Math.abs(n - 2 * count)); // 송전탑 개수의 차이의 최솟값 갱신
		visit.forEach((_, i) => (visit[i] = 0)); // 방문 배열 초기화
		count = 0; // 개수 초기화

		return m;
	}, n);
}
