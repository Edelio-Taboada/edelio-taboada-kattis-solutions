import java.util.Scanner;
public class TrainPassengers {

    public static void main(String[] args) {
        Scanner inp = new Scanner(System.in);
        int Capacity = inp.nextInt();
        int n = inp.nextInt();
        int trainPop = 0;
        int waiting = 0;
        boolean possible = true;
        for(int i = 0;i<n;i++){
            if(trainPop > Capacity || trainPop < 0){
                System.out.println("impossible");
                possible = false;
                break;
            }
            int leaving = inp.nextInt();
            if(i==0 && leaving > 0){
                possible = false;
                System.out.println("impossible");
                break;
            }
            trainPop -= leaving;
            int entering = inp.nextInt();
            trainPop += entering;
            waiting = inp.nextInt();
            if(trainPop < Capacity && waiting > 0){
                System.out.println("impossible");
                possible = false;
                break;
            }
            
        }
        if(trainPop > 0 || waiting > 0){
            if(possible){
                possible = false;
                System.out.println("impossible");
            }

        }
        if(possible){
            System.out.println("possible");
        }
    }

}
