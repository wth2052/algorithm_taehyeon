import java.util.ArrayList;
import java.lang.Math;
import java.util.Collections;
class Solution {
    public ArrayList<Integer> solution(int[] answers) {
        Student student = new Student();
        int[] supoja1 = {1, 2, 3, 4, 5, 1, 2, 3, 4, 5};
        int[] supoja2 = {2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5};
        int[] supoja3 = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
        int supoja1Result = student.문제풀기(supoja1, answers);
        int supoja2Result = student.문제풀기(supoja2, answers);
        int supoja3Result = student.문제풀기(supoja3, answers);
        ArrayList<Integer> result = student.성적비교하기(supoja1Result, supoja2Result, supoja3Result);
        return result;
    }
}

class Student {
    public int 문제풀기(int[] supoja, int[] answers) {
        int studentAnswerResult = 0;
        for(int i = 0; i < answers.length; i++) {
            if(supoja[i % supoja.length] == answers[i]) {
                studentAnswerResult += 1;
            }
        }
        return studentAnswerResult;
    }
    
    public ArrayList<Integer> 성적비교하기(int supoja1, int supoja2, int supoja3) {
        ArrayList<Integer> result = new ArrayList<>();
        result.add(supoja1);
        result.add(supoja2);
        result.add(supoja3);
        int maxScore = Math.max(supoja1, Math.max(supoja2, supoja3));
        ArrayList<Integer> answer = new ArrayList<>();
        if (supoja1 == maxScore) answer.add(1);
        if (supoja2 == maxScore) answer.add(2);
        if (supoja3 == maxScore) answer.add(3);
        Collections.sort(answer);
        return answer;

    }
    
}