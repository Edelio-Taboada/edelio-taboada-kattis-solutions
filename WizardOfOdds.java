import java.util.Scanner;
import java.lang.Math;
class WizardOfOdds {

    public static void main(String[] args) {
        Scanner inp = new Scanner(System.in);
        double N = inp.nextDouble();
        double K = inp.nextDouble();
        if (Math.pow(2, K) >= N){
            System.out.println("Your wish is granted!");
        }else{
            System.out.println("You will become a flying monkey!");
        }
    }

}
