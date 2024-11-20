import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        String findText = sc.next();
        sc.nextLine();
        int count = 0;
        int RingN = sc.nextInt();
        for (int i = 0; i < RingN; i++) {
                String text = sc.next();
                text += text;//반지는 원형 이어져 있으니깐
                if(text.contains(findText)){ //찾고자하는 문자열이 있는지 확인 
                    count++; 
                }
            }
        System.out.println(count);



    }
}
