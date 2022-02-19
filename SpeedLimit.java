import java.util.Scanner;
public class SpeedLimit {

    public static void main(String[] args) {
        Scanner inp = new Scanner(System.in);
        while(true){
            int n = inp.nextInt();
            if(n == -1){
                System.exit(0);
            }else{
                int miles = 0;
                int totalHours = 0;
                for(int i = 0; i<n;i++){
                    int mph = inp.nextInt();
                    int tempHours = totalHours;
                    totalHours = inp.nextInt();
                    miles += mph * (totalHours - tempHours);
                }
                System.out.println(miles + " miles");
            }
            
        }

    }

}
