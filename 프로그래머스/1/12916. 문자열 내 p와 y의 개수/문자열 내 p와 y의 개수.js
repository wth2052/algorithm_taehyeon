function solution(s){
    let pCount = 0;
    let yCount = 0;
    let upper = s.toUpperCase()
    
    
    for(const i of upper) {
        if(i === 'P') {
            pCount += 1;
        } else if (i ==='Y') {
            yCount += 1;
        }
    }
    
    return pCount === yCount
    
}