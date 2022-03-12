import java.util.*;
 class rightshift {
    public static void main(String args[]) {
        int a[] = {3,9,7,8,12,6,15,5,4,10};
        int temp = a[a.length - 1];
        for(int i = a.length-2;i>=0;i--)
        {
            a[i+1] = a[i];
        }
        a[0] = temp;
        
        
      System.out.println(Arrays.toString(a));
      
}}
