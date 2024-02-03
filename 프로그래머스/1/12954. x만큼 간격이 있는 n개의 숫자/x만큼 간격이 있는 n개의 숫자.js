function solution(x, n) {
  const answer = [];
  // i는 n만큼 반복
  for (let i = 1; i <= n; i++) {
      // x에 i를 곱한 배열 push
    answer.push(x * i);
  }

  return answer;
}