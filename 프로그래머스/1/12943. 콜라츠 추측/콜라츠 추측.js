function solution(num) {
    let answer = 콜라츠추측(num);
    
    return answer <= 500 ? answer : -1;
}



function 콜라츠추측(num) {
    let count = 0;
    //1이 아닌동안 반복해야 멈춤
    while(num !== 1) {

        num = num % 2 === 1 ? num * 3 + 1  : num / 2
        count++;
    }
    return count
    
}