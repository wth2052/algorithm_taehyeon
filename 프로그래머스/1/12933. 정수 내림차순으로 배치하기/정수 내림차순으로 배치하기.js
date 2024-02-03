function solution(n) {
    let answer = 0;
    // 0 보다 작으면 a 는 b 앞에
    // 0이면 a b 안변함
    // 0보다 크면 a는 b 앞으로
    let 배열화 = n.toString().split('').sort((a, b) => b - a);
    
    return parseInt(배열화.join(''))
    
    }
