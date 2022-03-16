import java.util.*;

class power_of_two 
{
    public static void main(String[] args) {
        
        Scanner s = new Scanner(System.in);
        int n = s.nextInt();
        int res = cal(n);
        System.out.println(res);
        s.close();


    }
    static int cal(int n)
    {
        if (n == 0)
        {
            return 1;
        }
        return 2* cal(n-1);
    }
}