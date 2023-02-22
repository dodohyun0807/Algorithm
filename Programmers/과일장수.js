function solution(k, m, score) {
  var answer = 0;

  score.sort((a, b) => {
    return a - b;
  });

  while (true) {
    let ans = 987654321;
    let cnt = 0;
    for (let i = 0; i < m; i++) {
      if (score.at(-1)) {
        sp = score.pop();
        if (ans > sp) {
          ans = sp;
        }
        cnt += 1;
      }
    }
    if (cnt === m) {
      answer += ans * m;
    } else {
      break;
    }
  }

  return answer;
}
