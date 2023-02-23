function solution(s) {
  let arr = []    
  let chk = false
  let X = ''
  let cntX = 0
  let cntY = 0
  
  for(let i = 0; i < s.length; i++){
      if(chk === false){
          if(i === s.length-1){
              arr.push(1)
          }
          chk = true
          X = s[i]
          cntX += 1
          continue
      }
      if(s[i] === X){
          if(i === s.length-1){
              arr.push(1)
          }
          cntX += 1
          continue
      }
      
      cntY += 1

      if(cntX === cntY){
          arr.push(1)
          X = ''
          cntX = 0
          cntY = 0
          chk = false
          continue
      }
      if(i === s.length-1){
          arr.push(1)
      }
  }
  
  return arr.length;
}