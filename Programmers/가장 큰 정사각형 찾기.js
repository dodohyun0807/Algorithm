function solution(board) {
  let answer = 0;

  const dp = [];

  for (let i = 0; i <= board.length; i++) {
    const tmp = [];
    for (let j = 0; j <= board[0].length; j++) {
      tmp.push(0);
    }
    dp.push(tmp);
  }

  for (let i = 1; i <= board.length; i++) {
    for (let j = 1; j <= board[0].length; j++) {
      if (board[i - 1][j - 1] === 1) {
        dp[i][j] = Math.min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1;
      }

      if (dp[i][j] > answer) {
        answer = dp[i][j];
      }
    }
  }

  return answer ** 2;
}
