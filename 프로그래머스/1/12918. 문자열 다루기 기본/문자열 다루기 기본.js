function solution(s) {
    let answer = true;
    let splitedS = s.split('')
    let isLengthFour = splitedS.length === 4
    let isLengthSix = splitedS.length === 6
    for(let i = 0; i < splitedS.length; i++) {
        if(isNaN(splitedS[i])) {
            return false
        } 
        if(!isLengthFour && !isLengthSix){
            return false
        }

    }
    return true
}