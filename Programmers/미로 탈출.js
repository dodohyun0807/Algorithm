function solution(maps) {
  var ansL = 987654321;
  var ansE = 987654321;
  let startY = 0;
  let startX = 0;
  let startLY = 0;
  let startLX = 0;
  let visited = [];
  let visited2 = [];
  const yy = [-1, 0, 1, 0];
  const xx = [0, -1, 0, 1];
  let lenY = maps.length;
  let lenX = 0;

  for (let i = 0; i < maps.length; i++) {
    let temp = [];
    let temp2 = [];
    for (let j = 0; j < maps[i].length; j++) {
      temp.push(0);
      temp2.push(0);
      if (maps[i][j] === "S") {
        startY = i;
        startX = j;
      }
    }
    visited.push(temp);
    visited2.push(temp2);
    if (i === 0) {
      lenX = temp.length;
    }
  }
  visited[startY][startX] = 1;

  const dfs = (y, x, cnt) => {
    for (let i = 0; i < 4; i++) {
      let dy = y + yy[i];
      let dx = x + xx[i];

      if (
        0 <= dy &&
        dy < lenY &&
        0 <= dx &&
        dx < lenX &&
        visited[dy][dx] === 0 &&
        maps[dy][dx] !== "X"
      ) {
        if (maps[dy][dx] === "L") {
          startLY = dy;
          startLX = dx;
          if (ansL > cnt + 1) {
            ansL = cnt + 1;
          }
        }
        visited[dy][dx] = 1;
        dfs(dy, dx, cnt + 1);
        visited[dy][dx] = 0;
      }
    }
  };

  dfs(startY, startX, 0);

  if (ansL === 987654321) {
    return -1;
  }

  //

  visited2[startLY][startLX] = 1;

  const dfs2 = (y, x, cnt) => {
    for (let i = 0; i < 4; i++) {
      const dy = y + yy[i];
      const dx = x + xx[i];

      if (
        0 <= dy &&
        dy < lenY &&
        0 <= dx &&
        dx < lenX &&
        visited2[dy][dx] === 0 &&
        maps[dy][dx] !== "X"
      ) {
        if (maps[dy][dx] === "E") {
          if (ansE > cnt + 1) {
            ansE = cnt + 1;
          }
        }
        visited2[dy][dx] = 1;
        dfs2(dy, dx, cnt + 1);
        visited2[dy][dx] = 0;
      }
    }
  };

  dfs2(startLY, startLX, 0);

  if (ansE === 987654321) {
    return -1;
  }

  return ansL + ansE;
}
