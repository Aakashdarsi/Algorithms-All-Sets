import java.util.*;
class treemap {
    public static void main(String[] args) {
        TreeMap<Integer,String> s = new TreeMap<>(Map.of(0,"A",1,"B"));
        System.out.println(s);
        s.put(3,"Mahesh");
        System.out.println(s);
    }
}
