// this solution was not done independently by me, I referenced another one while solving this one
import java.util.*;
import java.io.*;
public class Backspace {

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer tk = new StringTokenizer(reader.readLine());
        char[] chars = tk.nextToken().toCharArray();
        char[] outc = new char[chars.length];
        int skip = 0;
        for(int i=chars.length-1; i>=0; i--){
            if(chars[i] == '<'){
                outc[i] = ' ';
                skip++;
                
        }else if(skip > 0){
            skip--;
            outc[i] = ' ';
        }else{
            outc[i] = chars[i];
        }
    }
    System.out.println((new String(outc)).replaceAll(" ", ""));
}
}
