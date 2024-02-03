function solution(x) {
    let array = x.toString().split('')
    let 숫자배열합계 = array.map((Number)).reduce((a,b) => a + b)
    console.log(x % 숫자배열합계)
   
    //나머지가 남지 않는다면 0(falthy) 남는다면 1(thruthy)
    return  x % 숫자배열합계 ? false : true
}