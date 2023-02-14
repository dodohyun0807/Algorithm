function solution(n) {
  var answer = 1;

  for (let i = 1; i < parseInt(n / 2) + 1; i++) {
    let cnt = i;
    console.log(i);
    for (let j = i + 1; j < parseInt(n / 2) + 2; j++) {
      cnt += j;
      if (cnt === n) {
        answer += 1;
      }
      if (cnt > n) {
        break;
      }
    }
  }

  return answer;
}
