import java.util.Arrays;

class Solution {
    public int solution(int[] d, int budget) {
        return calBudget(d, budget);
    }
    
    
    //예산 계산
    public int calBudget(int[] d, int budget) {
        Arrays.sort(d);
        int result = 0;
        for (int i : d) {
            budget -= i;
            if(budget < 0) {
                return result;
            }
            result += 1;
        }
        if(budget >= 0) {
            result = d.length;
        }
        return result;
        
    }
}