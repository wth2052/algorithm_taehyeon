function solution(n) {
    let 제곱값 = Math.sqrt(n)
    let 정수여부 = Number.isInteger(제곱값) ? (제곱값+1)*(제곱값+1) : -1;
    
    return 정수여부;
}