import java.util.*;

class Solution {
    public int[] solution(int[] arr) {
        int[] answer = new int[arr.length];
        
        for(int i = 0; i < arr.length; i++) {
            // 50보다 크거나 같은 짝수일경우 (2로 나누었을때 0이 되면 짝수)
            boolean 첫번째조건 = arr[i] >= 50 && arr[i] % 2 == 0;
            // 50보다 작은 홀수일경우 (2로 나누었을때 0이 되지 않으면 홀수)
            boolean 두번째조건 = arr[i] < 50 && arr[i] % 2 != 0;
        
            if(첫번째조건) {
                answer[i] = arr[i] / 2;
            }
            else if (두번째조건) {
                answer[i] = arr[i] * 2;
            }
            else {
                answer[i] = arr[i];
            }
        }
        return answer;
    }
}
