import java.io.*;
import java.net.*;
import java.math.*;
import java.security.*;
public class DSSServer {
    public static void main(String h[]) throws IOException,NoSuchAlgorithmException{
        ServerSocket ss=new ServerSocket(9000);
        Socket st=ss.accept();
        PrintWriter pw=new PrintWriter(st.getOutputStream(),true);
        BufferedReader br=new BufferedReader(new InputStreamReader(st.getInputStream()));
        BigInteger s=BigInteger.valueOf(Integer.parseInt(br.readLine()));
        BigInteger p=BigInteger.valueOf(Integer.parseInt(br.readLine()));
        BigInteger r=BigInteger.valueOf(Integer.parseInt(br.readLine()));
        BigInteger q=BigInteger.valueOf(Integer.parseInt(br.readLine()));
        BigInteger y=BigInteger.valueOf(Integer.parseInt(br.readLine()));
        BigInteger g=BigInteger.valueOf(Integer.parseInt(br.readLine()));
        int message=Integer.parseInt(br.readLine());
        BigInteger w = s.modInverse(q);
        BigInteger u1 = (BigInteger.valueOf((int)message).multiply(w)).mod(q);
        BigInteger u2 = (r.multiply(w)).mod(q);
        BigInteger v= (((g.pow(u1.intValue())).multiply(y.pow(u2.intValue()))).mod(p)).mod(q);
        System.out.println(r + " " + v+" "+g+" "+y+" "+u1+" "+u2);
        if ((v.compareTo(r)) == 0) {
            System.out.println(v);
            System.out.println(r);
            System.out.println("Verified!");}
        else{
             System.out.println("Not Verified!!");       
        }}}
