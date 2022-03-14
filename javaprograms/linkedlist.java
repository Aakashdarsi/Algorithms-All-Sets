 import java.util.*;    
 class linkedlist {
    public static void main(String[] args) {
        LinkedList<Integer> l = new LinkedList<>();
        l.add(23);
        l.add(33);
        LinkedList<Integer> b = new LinkedList<>(List.of(22,33,44,55,66));
        l.addAll(b);
        System.out.println(l);
        l.addFirst(33);
        l.addLast(44);
        System.out.println(l.get(5));
        System.out.println(l.getFirst());
        System.out.println(l.getLast());


    }
}
