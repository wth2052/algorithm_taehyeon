import java.util.Arrays;

class Solution {
    public int solution(int[] d, int budget) {
        Arrays.sort(d);
        int result = 0;
        for (int i : d) {
            System.out.println(">"+ i + "<");
            System.out.println(">"+ d + "<");
            
            budget -= i;
            if(budget < 0) {
                return result;
            }
            result += 1;
        }
        //예산을 딱 맞게 쓴 경우 = d 갯수만큼 줄 수 있음
        if(budget >= 0) {
            // System.out.println("!"+ budget + "!");
            result = d.length;
        }
        return result;
    }
}