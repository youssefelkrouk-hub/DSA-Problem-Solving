
package ServerBasic;
import java.io.*;
import java.net.*;

/**
 * SERVEUR BASIQUE : recoit un nombre, le multiplie par 2, le renvoie.
 *
 * A RETENIR (les 4 etapes du serveur) :
 *   1. OUVRIR   -> new ServerSocket(port)
 *   2. ATTENDRE -> accept()  (bloquant, renvoie un Socket pour CE client)
 *   3. TUYAUX   -> getInputStream() / getOutputStream()
 *   4. DIALOGUER-> read() puis write()
 */
public class MiniServer {
    public static void main(String[] args) throws IOException {

        // 1. OUVRIR : le serveur ecoute sur le port 1234
        try (ServerSocket ss = new ServerSocket(1234)) {
            System.out.println("[Serveur] En attente d'un client sur le port 1234...");

            // 2. ATTENDRE : bloque jusqu'a ce qu'un client se connecte
            try (Socket s = ss.accept()) {
                System.out.println("[Serveur] Client connecte : " + s.getInetAddress());

                // 3. TUYAUX : un pour lire (is), un pour ecrire (os)
                InputStream is = s.getInputStream();
                OutputStream os = s.getOutputStream();

                // 4. DIALOGUER
                int nb = is.read();          // lit UN octet (bloquant)
                System.out.println("[Serveur] Recu    : " + nb);

                int rep = nb * 2;
                os.write(rep);               // n'envoie que les 8 bits de poids faible
                os.flush();
                System.out.println("[Serveur] Calcule : " + rep
                        + " | octet reellement envoye : " + (rep & 0xFF));
            }
            // try-with-resources : s puis ss sont fermes automatiquement
            // -> plus d'avertissement "resource leak"
        }
        System.out.println("[Serveur] Termine (un seul client servi).");
    }
}