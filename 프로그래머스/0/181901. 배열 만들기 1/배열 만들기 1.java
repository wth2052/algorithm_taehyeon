import java.util.ArrayList;
import java.util.List;

class Solution {
    public ArrayList<Integer> solution(int n, int k) {
        ArrayList<Integer> answer = new ArrayList<>();
        for(int i=k; i < n + 1; i++) {
            if(i%k == 0) {
                answer.add(i);
            }
        }
        return answer;
    }
}