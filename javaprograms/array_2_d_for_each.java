public  class array_2_d_for_each {
    public static void main(String[] args) {
        int a[][] = {{1,2,3,4},{2,4,6,8},{3,5,7,9}};
        for(int x[] : a)
        {
            for(int i : x)
            {
                System.out.print(i+" ");
            }
            System.out.println("\n ");
        }
        }
    
}
