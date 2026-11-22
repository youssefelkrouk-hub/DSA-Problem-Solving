package ServerMT;
import java.net.*;
import java.io.*;

public class SeverMT extends Thread{
    private int numeroClient = 0;
    public static void main(String[] args){
        new SeverMT().start();

    }
    @Override
    public void run(){
        try{
            ServerSocket ss = new ServerSocket(1234); // on doit handle le fait que le numero du prot peut etre utilisé par une autre application
            System.out.println("Demarage du serveur...");
            while(true){
                Socket socket = ss.accept();// pour accepter les connections des clients
                ++numeroClient;
                System.out.println("Client " + numeroClient + " is connected");
                // maintenant on va cree un thread conversation qui prend socket en parametre pour communiquer avec le client
                new Conversation(socket, numeroClient).start();

            }
        }
        catch(IOException e){
            System.out.println(e.getMessage());
        }

    }
    public class Conversation extends Thread{
        private int nombreClient=0;
        private Socket socket;
        public Conversation(Socket s, int num){
            this.nombreClient=num;
            this.socket=s;
        }




        @Override
        public void run(){
            try{
                InputStream is = socket.getInputStream();
                InputStreamReader isr = new InputStreamReader(is);
                BufferedReader br = new BufferedReader(isr);

                OutputStream os = socket.getOutputStream();
                PrintWriter pw = new PrintWriter(os,true); // true pour que le buffer se vide automatiquement
                String IP=socket.getRemoteSocketAddress().toString();
                System.out.println("Connexion avec le client numéro :  " + nombreClient + "et du IP :" + IP + " est demarée");
                System.out.println("Bienvenue vous etes le client numéro : " + nombreClient);

                while(true){
                    String req = br.readLine();
                    System.out.println(" Le Client "+IP+" a envoyé la requete : " + req);
                    pw.println(req.length());
                }

            }catch(IOException e){
                System.out.println(e.getMessage());
            }

        }

    }

    
}
