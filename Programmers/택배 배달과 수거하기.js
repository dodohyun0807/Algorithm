function solution(cap, n, deliveries, pickups) {
  var answer = 0;

  while(deliveries.length !== 0 || pickups.length !== 0){
      while(deliveries && deliveries.slice(-1)[0] === 0){
          deliveries.pop();
      }
      while(pickups && pickups.slice(-1)[0] === 0){
          pickups.pop();
      }
      
      answer += 2 * Math.max(deliveries.length, pickups.length);
      
      let canD = cap
      for(let i = deliveries.length-1; i >= 0; i--){
          if(deliveries[i] > canD){
              deliveries[i] -= canD;
              break;
          } else {
              canD -= deliveries[i]
              deliveries[i] = 0 ;
          }
      }
      
      let canP = cap
      for(let i = pickups.length-1; i >= 0; i--){
          if(pickups[i] > canP){
              pickups[i] -= canP;
              break;
          } else {
              canP -= pickups[i]
              pickups[i] = 0 ;
          }
      }
  }
  
  return answer;
}