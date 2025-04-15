import java.util.Scanner;
import java.math.BigInteger;

class Main {
    public static void main(String[] args) {
        Scanner kbd = new Scanner(System.in);
        String a,b;
        BigInteger A,B;

        a = kbd.nextLine();
        b = kbd.nextLine();

        A = new BigInteger(a);
        B = new BigInteger(b);

        System.out.println(A.add(B));
    }
}