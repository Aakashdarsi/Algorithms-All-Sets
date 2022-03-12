import java.util.*;
class copy_array {
    public static void main(String args[]) {
        Scanner s = new Scanner(System.in);
      int a[] = {8,6,10,9,2,15,7,13,14,11};
      int b[] = new int[a.length];
      for(int i=0;i<a.length;i++)
      {
          b[i] = a[i];
      }
      System.out.println(Arrays.toString(a));
       System.out.println(Arrays.toString(b));
       s.close();
    }
}
