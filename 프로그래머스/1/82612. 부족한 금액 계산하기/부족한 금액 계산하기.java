
class Solution {
    public long solution(int price, int money, int count) {
        long totalCost = getTotalCost(price, money, count);
        return totalCost;
    }
    public static long getTotalCost(int price,int money, int count) {
       long answer = -1;
       long totalNPrice = 0;
       for(int i=1; i<=count; i++) {
            totalNPrice += price*i;
       }
       answer = totalNPrice - money;
        if (answer < 1) {
            return 0;
        }
        return answer;
    }
}