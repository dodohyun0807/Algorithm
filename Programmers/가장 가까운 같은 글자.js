function solution(s) {
  var answer = [];
  
  let chk = {}
  
  for(let i = 0 ; i < s.length; i++){
      if(Object.keys(chk).includes(s[i])){
          answer.push(i - chk[s[i]])
          chk[s[i]] = i
      } else{
          chk[s[i]] = i
          answer.push(-1)
      }
  }
  
  return answer;
}