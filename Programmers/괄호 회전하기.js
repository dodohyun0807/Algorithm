function solution(s) {
  let ans = 0;
  
  for(let i = 0 ; i < s.length; i++){
      let temp = s.slice(i).concat(s.slice(0, i))
      let q = []
      let chk = 0
      
      for(let j = 0; j < s.length; j++){
          if(q.length === 0){
              if(temp[j] === "]" || temp[j] === ")" || temp[j] === "}"){
                  break
              } else{
                  q.push(temp[j])    
              }
          } else if(q.slice(-1)[0] === "[" && temp[j] === "]"){
              q.pop()
              chk += 2
          } else if (q.slice(-1)[0] === "{" && temp[j] === "}"){
              q.pop()
              chk += 2
          } else if (q.slice(-1)[0] === "(" && temp[j] === ")"){
              q.pop()
              chk += 2  
          } else{
              q.push(temp[j])
          }
      }
      
      if(q.length === 0 && chk === s.length){
          ans += 1
      }
  }
  
  
  
  
  return ans;
}