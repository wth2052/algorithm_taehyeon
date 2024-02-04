function solution(s){
    let splitedS = s.split('')
    let count = 0;
    


    for(let i = 0; i < splitedS.length; i++) {
        if(splitedS[0] === ')') {
            return false
        } else if(splitedS[splitedS.length -1] === '(') {
            return false
        }
        
        if(splitedS[i] === '(') {
            count ++
        }
        else {
            count--
            if (count < 0) return false
            }
    }
    
    
       // splitedS.shift() + splitedS.pop() === '()' ? true : false;
    return count === 0 ? true : false
}