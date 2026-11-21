package Multithreading_java;

import java.io.*;
import java.net.*;

public class Client {
    public static void main(String[] args) throws IOException {
        Socket socket = new Socket("localhost", 1234);
        BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
        PrintWriter out = new PrintWriter(socket.getOutputStream(), true);
        BufferedReader clavier = new BufferedReader(new InputStreamReader(System.in));

        System.out.println(in.readLine());   // "Welcome ..."

        String message;
        while ((message = clavier.readLine()) != null) {
            out.println(message);
            System.out.println(in.readLine());
        }
        socket.close();
    }
}
