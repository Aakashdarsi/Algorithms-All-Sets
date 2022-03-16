import java.util.*;
class src_to_destination
{
    public static void main(String[] args) {
        Scanner s= new Scanner(System.in);
        int src = 0;
        int destination = 10;
        result(src,destination);
        s.close();
        
    }
    static void result(int src,int destination)
    {
        if (src == destination) // base case
        {
            System.out.println("Reached Destination");
            System.exit(0);
        }
        System.out.println(src+" At current position move forward "+destination); // processing
        // processing
        src++;
        result(src, destination); // reccurence relation
    }
}