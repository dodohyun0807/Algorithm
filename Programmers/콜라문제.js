function solution(a, b, n) {
  let ans = 0;
  
  while(n >= a){
      let bottle = parseInt(n / a)
      let el = n % a
      n = bottle * b
      n += el
      ans += bottle * b
  }
  
  
  return ans;
}