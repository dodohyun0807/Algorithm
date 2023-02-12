function solution(cards) {
  var answer = 0;

  const temp = (idx, arr, cnt) => {
    const tmp = arr[idx];
    arr[idx] = 0;
    if (tmp === 0) {
      return cnt;
    } else {
      return temp(tmp - 1, arr, cnt + 1);
    }
  };

  cards.forEach((card) => {
    if (card !== 0) {
      const arr = [...cards];
      const first = temp(card - 1, arr, 0);
      arr.forEach((card2) => {
        if (card2 !== 0) {
          const arr2 = [...arr];
          const second = temp(card2 - 1, arr2, 0);
          answer = Math.max(answer, first * second);
        }
      });
    }
  });
  return answer;
}
