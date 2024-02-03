function solution(phone_number) {
    let answer = '';
    let 마스킹해야할범위 = phone_number.length - 3
    let 맨뒤4자리 = phone_number.slice(마스킹해야할범위-1, phone_number.length)
    for(let i = 1; i < 마스킹해야할범위; i++) {
        answer += '*'
    }
    return answer+맨뒤4자리;
}