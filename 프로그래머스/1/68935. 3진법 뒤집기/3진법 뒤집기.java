class Solution {
    public int solution(int n) {
        Calculate calAnswer = new Calculate();
        String terNumber = calAnswer.decimalToTernary(n);
        String reverseNumber = calAnswer.reverseNumber(terNumber);
        int decimalNumber = calAnswer.ternaryToDecimal(reverseNumber);
        return decimalNumber;
    }
}


class Calculate {
    //3진법
    public String decimalToTernary (int n) {
        return Integer.toString(n, 3);
    }

    public String reverseNumber (String n) {
        return new StringBuilder(n).reverse().toString();
    }
    
    //10진법으로 변환
    public int ternaryToDecimal(String n) {
        return Integer.parseInt(n, 3);
    }
}