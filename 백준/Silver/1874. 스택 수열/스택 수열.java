import java.util.*;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        //입력 수열
        int[] number = new int[N];
        for (int i = 0; i < N; i++){
            number[i] = sc.nextInt();
        }
        Stack<Integer> numberlist = new Stack<>();
        //결과
        List<String> result = new ArrayList<>();
        //스택에 넣을 값
        int stacknumber = 1;
        boolean possible_next = true;

        for (int num : number){
            while(stacknumber <= num){
                numberlist.push(stacknumber);
                result.add("+"); //push라서
                stacknumber++;
            }
            if(numberlist.peek() == num){ //스택 먄위에 숫자와 같으면 peek
                numberlist.pop();
                result.add("-");
            }
            else{
                possible_next = false;
                break;
            }
        }
        //최종결과
        if(!possible_next){
            System.out.println("NO");
        }
        else {
            for (String s : result) {
                System.out.println(s);
            }
        }

    }
}
