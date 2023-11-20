
import java.io.*;
import java.net.*;
import java.util.*;
import java.security.*;
import java.math.*;
public class DSSClient {
    public static void main(String sk[]) throws IOException, NoSuchAlgorithmException {
        Socket st=new Socket("localhost",9000);
        PrintWriter pw=new PrintWriter(st.getOutputStream(),true);
        BufferedReader br=new BufferedReader(new InputStreamReader(st.getInputStream()));
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the H(m): ");
        int message =sc.nextInt();
        System.out.println("Enter the p: ");
        BigInteger p = BigInteger.valueOf(sc.nextInt());//BigInteger.valueOf(sc.nextLong());
        System.out.println("Enter the q: ");
        BigInteger q = BigInteger.valueOf(sc.nextInt());
        System.out.println("Enter the g: ");
        BigInteger g = BigInteger.valueOf(sc.nextInt()); 
        System.out.println("Enter the x: ");
        BigInteger x = BigInteger.valueOf(sc.nextInt());
        System.out.println("Enter the k: ");
        BigInteger k = BigInteger.valueOf(sc.nextInt());
        BigInteger y = g.modPow(x, p);
        System.out.println("Performing Sigining...");      
        BigInteger r = (g.modPow(k, p)).mod(q);
        BigInteger s = ((k.modInverse(q)).multiply(BigInteger.valueOf(message).add(x.multiply(r)))).mod(q);
        System.out.println("Sending signature..:  " + r + " " + s);
        pw.println(s);
        pw.println(p);
        pw.println(r);
        pw.println(q);
        pw.println(y);
        pw.println(g);
        pw.println(message);}}
