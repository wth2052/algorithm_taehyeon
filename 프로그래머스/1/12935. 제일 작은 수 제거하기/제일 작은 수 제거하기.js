function solution(arr) {
    let 가장작은수 = Math.min(...arr)
    let 작은수의위치 = arr.indexOf(가장작은수)
    let 답안 = arr.filter((num) => num !== 가장작은수)
    if(답안.length === 0) return [-1]
    return 답안
}