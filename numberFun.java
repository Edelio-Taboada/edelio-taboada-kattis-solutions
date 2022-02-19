import java.util.Scanner;

class Main {
  public static void main(String[] args) {
    Scanner inp = new Scanner(System.in);
    int N = inp.nextInt();
    for (int i = 0;i<N;i++){
      double a = inp.nextDouble();
      double b = inp.nextDouble();
      double c = inp.nextDouble();
      if(a + b == c || a - b == c || b - a == c || a*b == c || a/b == c || b/a == c){
        System.out.println("Possible");
      } else{
        System.out.println("Impossible");
      }
    }
  }
}
