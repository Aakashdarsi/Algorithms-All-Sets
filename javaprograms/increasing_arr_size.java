
import java.util.*;
class increasing_arr_size {
    public static void main(String args[]) {
        Scanner s = new Scanner(System.in);
      int a[] = {8,6,10,9,2,15,7,13,14,11};
      int b[] = new int[2*a.length];
      for(int i=0;i<a.length;i++)
      {
          b[i] = a[i];
      }
      
       System.out.println(Arrays.toString(b));
       a = null;
       System.out.println(a);
       s.close();
    }
}
