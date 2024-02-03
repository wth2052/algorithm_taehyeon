function solution(absolutes, signs) {
    let 배열 = []
    for (let i = 0; i < absolutes.length; i++) {
        if(signs[i] === true) {
            배열.push(absolutes[i])
        } else if(signs[i] === false) {
            배열.push(-absolutes[i])
        }
    }
    return 배열.reduce((a,b) => a + b);
}