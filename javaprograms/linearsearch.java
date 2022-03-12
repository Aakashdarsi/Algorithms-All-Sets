public class linearsearch {
    
        public static void main(String args[]) {
          int a[] = {3,9,7,8,12,6,15,5,4,10};
          int max = Integer.MIN_VALUE;
          for (int x: a)
          {
              if (x == 15)
              {
                  System.out.println("Found at"+x);
                  System.exit(0);
              }
          }
          System.out.println("Not Found");
        }
    
}
