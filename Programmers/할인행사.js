function solution(want, number, discount) {
  var answer = 0;
  const want_s = [...new Set(want)].length;
  const arr = [];

  for (let i = 0; i < discount.length; i++) {
    const temp = discount.slice(i, i + 10);
    const sale = new Set(temp);
    const sale_s = [...sale].length;
    if (sale_s >= want_s) {
      arr.push(temp);
    }
  }

  for (let i = 0; i < arr.length; i++) {
    let nn = [...number];
    for (let j = 0; j < arr[i].length; j++) {
      const chk = want.indexOf(arr[i][j]);
      if (chk !== -1) {
        nn[chk] -= 1;
      }
    }
    let check_minus = 0;
    for (let k = 0; k < nn.length; k++) {
      if (nn[k] <= 0) {
        check_minus++;
      }
    }
    if (check_minus === want.length) {
      answer++;
    }
  }

  return answer;
}
