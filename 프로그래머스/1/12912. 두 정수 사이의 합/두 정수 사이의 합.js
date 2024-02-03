function solution(a, b) {
    
    return ab사이구하기(a, b);
}




function ab사이구하기(a, b) {
    let 합계 = 0;
        if (a > b){
        for(let i = b; i < a+1; i++) {
            합계 += i;
        }
        } else if(a < b){
        for(let i = a; i < b+1; i++) {
            합계 += i;
        }
    
        }
        else if  (a === b) {
            합계 +=a;
            return a;
        }
    return 합계

}