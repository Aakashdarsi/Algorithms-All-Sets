class adding_2_matrices {
    public static void main(String[] args) {
        int a[][] = {{3,5,9},{7,6,2},{4,3,5}};
        int b[][] = {{1,5,2},{6,8,4},{3,9,7}};
        int c[][] = new int[a.length][a.length];
        for(int i=0;i<a.length;i++)
        {
            for (int j = 0;j<a[0].length;j++)
            {
                c[i][j] = a[i][j]+b[i][j];
            }
        }
        for (int x[] : c)
        {
            for (int i : x)
            {
                System.out.print(i+" ");
            }
            System.out.println("\n");
        }

    }
}
