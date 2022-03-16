/* If No base condtion then it will lead to stack overflow*/
// In recursion base case is mandatory otherwise segmentation error will occur 
// recurence relation should be mandatory 
// Processing part !!! Optional !!! 
// if reccurece relation comes at end after processing uch relation is called tail recursion
// if reccurence relation comes before processing such recuurence relation is calld head recursion 
import java.util.*;
class factorial 
{
    public static void main(String[] args) {

        Scanner s = new Scanner(System.in);
        int n ;
        n = s.nextInt();
        int res;
        res = factorial_num(n);
        System.out.println(res);
        s.close();

        
    }

static int factorial_num(int n)
{
    if (n <=1) // basecase 
    {
        return 1; 
    }
    else{
        return n*factorial_num(n-1);
    }

    

}
}
