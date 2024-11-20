import java.util.*;
import java.util.stream.IntStream;

public class Main{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Set<Integer> studentSet = new HashSet<>();
        for (int i = 1; i <= 28; i++) {
            int num = sc.nextInt();
            if (num >= 1 && num <= 30){
                studentSet.add(num);
            }
            else {
                return;
            }
        }
        //Set(=studentSet) 을 사용해서 새로운 Set을 사용할 수 있음(=ArrayList)
        List<Integer> homework = new ArrayList<>();
        for (int i = 1; i <= 30; i++) {
            if (!studentSet.contains(i)) {
                homework.add(i);
            }

        }
        Collections.sort(homework);
        System.out.println(homework.get(0));
        System.out.println(homework.get(1));
    }
}
