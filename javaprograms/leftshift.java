
import java.util.*;
class leftshift {
    public static void main(String args[]) {
        int a[] = {3,9,7,8,12,6,15,5,4,10};
        
        
        int rotate = 5;
        for(int j=0;j<rotate;j++)
        {
            int t = a[0];
            for(int i=1;i<a.length;i++)
        {
            a[i-1] = a[i];
        }
        a[a.length - 1] = t;
        
        }
        System.out.println(Arrays.toString(a));
      
}}
