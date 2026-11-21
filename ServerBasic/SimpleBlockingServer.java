package ServerBasic;
import java.io.*;
import java.net.*;
public class SimpleBlockingServer {
    public static void main(String[] args) throws IOException{
        ServerSocket ss=new ServerSocket(1234);
        System.out.println("=== [Serveur] En attente d'un client sur le port 1234...");
        System.out.println("========================");

        Socket socket=ss.accept();
        InputStream is=socket.getInputStream();
        OutputStream os = socket.getOutputStream();
        System.out.println("==== I'm waiting for a request from the client");
        int data = is.read();
        System.out.println("=== I received the data from the client: "+data);
        int response=data*2; 
        System.out.println("Sending the response to the client :"+response);
        os.write(response);
        socket.close(); // close the socket after the communication is done
        ss.close();  // close the server socket after the communication is done            




        }

    
}
