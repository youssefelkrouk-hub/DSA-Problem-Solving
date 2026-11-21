package ServerBasic;

import java.io.*;
import java.net.*;

public class SimpleBlockingClient {
    public static void main(String[] args) throws IOException {
        Socket socket=new Socket("localhost",1234);
        InputStream is=socket.getInputStream();
        OutputStream os = socket.getOutputStream();
        System.out.println("==== I'm sending the data to the server");
        int data=5;
        os.write(data);
        System.out.println("=== I sent the data to the server: "+data);
        int response=is.read();
        System.out.println("=== I received the response from the server: "+response);
            socket.close(); // close the socket after the communication is done
            
        }
        
}
    

