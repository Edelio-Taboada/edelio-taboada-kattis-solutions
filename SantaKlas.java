import java.util.Scanner;
import java.lang.Math;
public class SantaKlas {

    public static void main(String[] args) {
        Scanner inp = new Scanner(System.in);
        int H = inp.nextInt();
        int v = inp.nextInt();
        double moddedAngle;
        int time = 0;
        boolean crashing = true;
        if (v <= 180 && v>=0){
            System.out.println("safe");
            crashing = false;
        }else if(v<270){
            moddedAngle = v - 180;
            moddedAngle = 90 - moddedAngle;
            moddedAngle = Math.toRadians(moddedAngle);
            time = (int)(H/Math.cos(moddedAngle));
        }else if(v==270){
            System.out.println(H);
            crashing = false;
        }else if(v>270){
            moddedAngle = v - 270;
            moddedAngle = Math.toRadians(moddedAngle);
            time = (int)(H/Math.cos(moddedAngle));
        }
        if(crashing){
            System.out.println(time);
        }
        
    }

}
