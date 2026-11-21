package ServerBasic;

import java.io.*;
import java.net.*;

/**
 * CLIENT BASIQUE : envoie un nombre, lit la reponse du serveur.
 *
 * A RETENIR (les 3 etapes du client) :
 *   1. SE CONNECTER -> new Socket(ip, port)
 *   2. TUYAUX       -> getInputStream() / getOutputStream()
 *   3. DIALOGUER    -> write() puis read()
 *
 * Utilisation :
 *   java ClientBasique              -> envoie 23 a localhost
 *   java ClientBasique 50           -> envoie 50 a localhost
 *   java ClientBasique 50 192.168.1.23
 */
public class ClientBasique {
    public static void main(String[] args) throws IOException {
        int nombre = (args.length > 0) ? Integer.parseInt(args[0]) : 23;
        String ip  = (args.length > 1) ? args[1] : "localhost";

        // 1. SE CONNECTER (declenche le accept() cote serveur)
        try (Socket s = new Socket(ip, 1234)) {
            System.out.println("[Client] Connecte a " + ip + ":1234");

            // 2. TUYAUX
            InputStream is = s.getInputStream();
            OutputStream os = s.getOutputStream();

            // 3. DIALOGUER : ce que je WRITE, le serveur le READ (et inversement)
            System.out.println("[Client] J'envoie : " + nombre);
            os.write(nombre);
            os.flush();

            int rep = is.read();             // attend la reponse (bloquant)
            System.out.println("[Client] Reponse du serveur : " + rep);
        }
    }
}