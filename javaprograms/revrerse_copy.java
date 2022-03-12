
import java.util.*;
 class revrerse_copy {
 
    // This program is to find reverse copy of the array
    
        public static void main(String args[]) {
            Scanner s = new Scanner(System.in);
          int a[] = {8,6,10,9,2,15,7,13,14,11};
          int b[] = new int[a.length];
          for(int i=a.length-1;i>=0;i--)
          {
              b[a.length - 1-i] = a[i];
          }
          System.out.println(Arrays.toString(a));
           System.out.println(Arrays.toString(b));
           s.close();
        }
    
       
}
