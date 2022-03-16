import java.util.*;
class fibonacci {
    public static void main(String[] args) {
        
        Scanner s = new Scanner(System.in);
        int n = s.nextInt();
        int res = fibonacci_cal(n);
        System.out.println(res);
        s.close();
    }
    static int fibonacci_cal(int n)
    {
        if(n==0 || n==1)
        {
            return 1;
        }
        return fibonacci_cal(n-1)+fibonacci_cal(n-2);
    }
}
