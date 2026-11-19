package Multithreading_java;

public class Main {
    public static void main(String[] args) {
        // cree et appeler le thread lettre qu'on a cree on utlisant l'héritage de la classe Thread
        Lettre l1=new Lettre('q','z');
        l1.start(); //  la methode  fait deux choses: elle appelle la methode run() et elle cree un thread
        // l1 est bien un thread 
        // car il est une instance de la classe Lettre qui hérite de la classe Thread




        
        // cree et appeler le thread nombre qu'on a cree on utlisant l'interface Runnable
        Thread N1=new Thread(new Nombre(10));
        N1.start(); //  la methode  fait deux choses: elle appelle la methode run() et elle cree un thread
        // N1 est bien un thread 
        // car il est une instance de la classe Thread en implementant l'interface Runnable 
    }
}
