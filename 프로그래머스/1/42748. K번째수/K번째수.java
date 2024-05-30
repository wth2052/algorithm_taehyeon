import java.util.Arrays;
import java.util.ArrayList;


class Solution {
    public ArrayList<Integer> solution(int[] array, int[][] commands) {
        ArrayList<Integer> answer = new ArrayList<>();
        System.out.println(answer.toString());
        // [i][0]-1 번째부터 [i][1] 번째까지 자르고
        //[i][2]번째 있는 수를 return
        for(int i=0; i < commands.length; i++) {
            int from = commands[i][0];
            int to = commands[i][1];
            int commandReturn = commands[i][2]-1;
            //from 인덱스는 포함되고 to 인덱스는 제외되기 때문
            int[] cutedArrays = Arrays.copyOfRange(array, from-1, to);
            Arrays.sort(cutedArrays);
            int answerNumber = cutedArrays[commandReturn];
            answer.add(answerNumber);
        }
        return answer;

    }
}