import java.util.*;
class deque {
    public static void main(String[] args) {
        ArrayDeque<Integer> dq = new ArrayDeque<>();
        dq.offerLast(22);
        dq.offerLast(33);
        dq.offerLast(44);
        System.out.println(dq);
    }
}
