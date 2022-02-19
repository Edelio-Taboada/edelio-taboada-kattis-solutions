import java.util.Scanner;
import java.util.ArrayList;
class NoDuplicates {
  public static void main(String[] args) {
    Scanner inp = new Scanner(System.in);
    ArrayList<String> words = new ArrayList<String>();
    while(inp.hasNext() == true){
      String word = inp.next();
      if (words.contains(word)){
        System.out.println("no");
        System.exit(0);
      } else {
        words.add(word);
      }
    }
    System.out.println("yes");
  }
}
