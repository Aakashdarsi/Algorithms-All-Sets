class secondmax
{
         public static void main(String args[]) {
          int a[] = {3,9,7,8,12,6,15,5,4,10};
          int max1,max2;
          max1 = max2 = a[0];
          for(int i=0;i<a.length;i++)
          {
              if (a[i]>max1)
              {
                   max2 = max1;
                   max1 = a[i];
                  
              }
              else if(a[i] > max2)
              {
                 max2 = a[i];
              }
          }
          System.out.println("second largest is :"+max2);
            
        }
    
}