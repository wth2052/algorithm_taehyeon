function solution(A,B){
    let 누적값 = 0;
    A.sort((a,b) => a - b)
    B.sort((a, b) => b - a)
    for(let i=0; i < A.length; i++) {
        누적값 += A[i] * B[i]
    }
    return 누적값;
}