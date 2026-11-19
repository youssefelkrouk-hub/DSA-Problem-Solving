package Multithreading_java;

public class Nombre implements Runnable{
    int nombre;
    public Nombre(int n){
        this.nombre=n;
    }
    public void run(){
        for(int i=1;i<=nombre;i++){
            if(i%2==0){
                System.out.println(i);
            }
        }
    }

}
