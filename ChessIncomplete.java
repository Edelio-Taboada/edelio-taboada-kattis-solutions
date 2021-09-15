package practice;
import java.util.Scanner;
import java.util.Hashtable;
public class ChessIncomplete {

	public static void main(String[] args) {
		Scanner inp = new Scanner(System.in);
		Hashtable<String, Integer> letterToInt = new Hashtable<>();
		letterToInt.put("A", 1);
		letterToInt.put("B", 2);
		letterToInt.put("C", 3);
		letterToInt.put("D", 4);
		letterToInt.put("E", 5);
		letterToInt.put("F", 6);
		letterToInt.put("G", 7);
		letterToInt.put("H", 8);
		int testCases = inp.nextInt();
		for(int i = 0; i<testCases;i++){
			String initialXstring = inp.next();
			int initialY = inp.nextInt();
			String finalXstring = inp.next();
			int finalY = inp.nextInt();
			int initialX = letterToInt.get(initialXstring);
			int finalX = letterToInt.get(finalXstring);
			if (initialX%2 != initialY%2 || initialY%finalY != 0){
				System.out.println("Impossible");
			}
				
			
			
		}

	}

}
