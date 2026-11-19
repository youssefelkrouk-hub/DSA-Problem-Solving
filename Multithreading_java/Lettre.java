package Multithreading_java;

public class Lettre extends Thread {

    char Lettre_dem, lettre_fin;
    public Lettre(char Lettre_dem,char l1){
        this.Lettre_dem=Lettre_dem;
        lettre_fin=l1;
    }
    @Override 
    public void run(){
        for(char i=Lettre_dem;i<=lettre_fin;i++){
            System.out.println(i);
        }
    }
    
    
    
}
