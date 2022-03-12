import java.util.*;
class arraylist2 {
    public static void main(String[] args) {
        ArrayList<String> a = new ArrayList<>();
        a.add("Mahesh");
        a.add("Suresh");
        a.add("Mukesh");
        a.add(2,"Rajesh");
        System.out.println(a);
        System.out.println(a.contains("Mahesh"));
        System.out.println(a.indexOf("Mukesh"));
        a.set(1,"Aakash");
        System.out.println(a);
        // for (int i=0;i<a.size();i++){

        //     System.out.println(a.get(i));

        // }
        // for (String x : a){
        //     System.out.println(x);
        // }
        
        

    }
}
