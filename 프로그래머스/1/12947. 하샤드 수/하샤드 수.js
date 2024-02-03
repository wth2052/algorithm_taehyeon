function solution(x) {
    let array = x.toString().split('')
    let 숫자배열합계 = array.map((Number)).reduce((a,b) => a + b)
    console.log(x % 숫자배열합계)
   
    return  x % 숫자배열합계 ? false : true
}