import java.util.Scanner;
public class OddGnome {

    public static void main(String[] args) {
        
        Scanner inp = new Scanner(System.in);
        int n = inp.nextInt();
        for(int i = 0; i<n;i++){
            int g = inp.nextInt();
            // System.out.println("g: " + g);
            int gnomeId;
            int tempId1 = 0;
            boolean kingFound = false;
            for(int j = 0;j<g;j++){
                if(j == 0){
                    gnomeId = inp.nextInt();
                    tempId1 = gnomeId;
                }else{
                    gnomeId = inp.nextInt();
                    // System.out.println("gnomeId: " + gnomeId + "--- tempId: " + tempId1 + " ---j: " + j + " ---kingFound: " + kingFound);
                    if(gnomeId != tempId1 + 1 || gnomeId == tempId1){
                        if(kingFound == false){
                            System.out.println(j + 1);
                            kingFound = true;
                        }
                            
                    }
                    tempId1 = gnomeId;
                }
            }
        }
    }

}
