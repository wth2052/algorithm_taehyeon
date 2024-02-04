function solution(numbers) {
    let answer = 0;
    numbers.sort()
    
    for(let i=0; i < 10; i++) {
        if(!numbers.includes(i)) answer += i
}
    
    return answer;
}