package Multithreading_java;


import java.io.*;
import java.net.*;

public class MultiThreadServer extends Thread{
    public static void main(String[] args){new MultiThreadServer().start();}
    @Override 
    public void run(){
        try{
            ServerSocket serverSocket= new ServerSocket(1234);
            while(true){
                Socket socket= serverSocket.accept();
                new Conversation(socket).start();
            }
        } catch(IOException e){
            throw new RuntimeException(e);
        }
    }
}

class Conversation extends Thread{
    private Socket socket;
    Conversation(Socket socket){this.socket = socket ; }
    @Override
    public void run(){
        try{
            InputStream is= socket.getInputStream();
            InputStreamReader isr= new InputStreamReader(is);
            BufferedReader bufferdReader = new BufferedReader(isr);
            PrintWriter printWriter = new PrintWriter(socket.getOutputStream(), true);
            printWriter.println("Welcome ...");
            String line;
            while((line=bufferdReader.readLine())!=null){
                String response = "Request length: " + line.length();
                printWriter.println(response);
            }
        }catch(IOException e){throw new RuntimeException(e);}
    }
}
