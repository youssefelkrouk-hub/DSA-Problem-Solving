package TPSOCKET;
import java.net.*;
import java.io.*;
import java.util.Scanner;
public class Myclient {
    public static void main(String[] args)  throws IOException{
        System.out.println("Client is trying to connect to the server on port 1234");
        // on veut se connecter au serveur : il faut cree une socket
        Socket socket=new Socket("localhost", 1234);
        InputStream is=socket.getInputStream();
        OutputStream os=socket.getOutputStream();
        /*
         Saisir un nombre au clavier par la methode scanner : 
         */
        Scanner sc = new Scanner(System.in);
        System.out.println("Donner un nombre entier : ");
        int nb = sc.nextInt();
        System.out.println("j'ai envoyé l'octet : "+nb+" au serveur");
        os.write(nb);
        System.out.println("j'attends le résultat du serveur");
        int result=is.read();
        System.out.println("Le résultat reçu du serveur est : "+result);
        socket.close();
        sc.close();



    }
}
