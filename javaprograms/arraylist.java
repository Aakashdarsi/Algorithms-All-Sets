 import java.util.*;
 class arraylist {
    public static void main(String[] args) {
        ArrayList<Integer> a = new ArrayList<>(20);
        ArrayList<Integer> b = new ArrayList<>(List.of(50,60,70,80,90));
        a.add(22);
        a.add(33);
        System.out.println(a);
        a.addAll(b);
        System.out.print(a);
        System.out.println(a.contains(2));
        b.clear();
        System.out.println(b);
        System.out.println(a.get(2));
        System.out.println(a.indexOf(70));
        a.add(2,70);
        System.out.println(a.lastIndexOf(70));
        a.set(2,20);
        System.out.println(a);
        for(int x : a){
            System.out.println(x);
        }

    }
}
