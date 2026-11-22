package TPSOCKET;


import java.net.*;
import java.io.*;
public class Myserver {
    public static void main(String[] args) throws IOException {
        ServerSocket ss= new ServerSocket(1234); //il se peut que le port 1234 soit déjà utilisé par une autre application,on gere l'exception
        System.out.println("Server is listening on port 1234");
        Socket s=ss.accept();
        System.out.println("Client connected"+s.getRemoteSocketAddress());
        InputStream is=s.getInputStream();
        OutputStream os=s.getOutputStream();
        System.out.println("J'attend le client envoie un octet par la methode read() de l'InputStream");
        int b=is.read();// je ne peut lire qu'un octet à la fois
        System.out.println("Le client a envoyé l'octet : "+b);
        int result=b*2;
        // je vais envoyer le résultat au client en utilisant la methode write() de l'OutputStream
        System.out.println("Le résultat envoyé au client est : "+result);
        os.write(result);
        s.close();

    }
}
