import java.util.*;

class counting_print {
    public static void main(String[] args) {
        
        Scanner s = new Scanner(System.in);
         int n = s.nextInt();
         print_e(n);
         s.close();
    }
    static void print_e(int n)
    {
        if (n == 0)
        {
            System.exit(0);
        }
        System.out.println(n);
        print_e(n-1);
    }
}
