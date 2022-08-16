package teste;
import java.util.Scanner;
public class ex01 {
    
    
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        
        char especie, ESml='x';
        double idade,peso,Sid=0,Sp=0,mediaI,mediaP,mediaG=0,somaPG=0,Porcent,IDml=0,PSml=0, outros=0;
        int i=0,SG=0;
        
        for(i=0; i<5; i++){
            System.out.println("Digite a espécie: \n"
                    + "g - gatos\n"
                    + "c - cachorros\n"
                    + "o - outros");
            
            especie = scan.next().charAt(0);
            
            while(especie != 'g' && especie != 'c' && especie != 'o'){
                System.out.println("\n\n-------LETRA INVALIDA!-------");
                
                System.out.println("Digite novamente: \n"
                    + "g - gatos\n"
                    + "c - cachorros\n"
                    + "o - outros");
            
            especie = scan.next().charAt(0);
            }
            
            System.out.println("Digite a idade em meses: ");
            idade = scan.nextDouble();
            
            System.out.println("Digite o peso: ");
            peso = scan.nextDouble();
            
            if(i==0){
                PSml = peso;
                IDml = idade;
                ESml = especie;
            }
            
            if(peso < PSml){
                IDml = idade;
                ESml = especie;
            }
            
            if(especie == 'c' && peso > 20 ){
                System.out.println("Cão de porte grande");
            }
            else if (especie == 'c' && peso < 20 && peso > 5){
                System.out.println("Cão de porte médio");
            }
            else if(especie == 'c' && peso <= 5)
            {
                System.out.println("Cão de porte pequeno");
            }
            
           Sid = Sid + idade;
           Sp = Sp + peso;
           
           if(especie == 'g' && idade > 60){
               somaPG = somaPG + peso;
               SG++;
           }
           
           if(especie == 'o'){
               outros++;
           }
           
        }
        mediaI = Sid / 5;
        System.out.println("A média das idades é: " + mediaI + " meses");
        
        mediaP = Sp / 5;
        System.out.println("A média dos pesos é: " + mediaP);
         
        if (SG != 0){
            mediaG = somaPG / SG;
            System.out.println("A média dos gatos é: " + mediaG);
            
        }else{
             System.out.println("A média dos gatos é: Não existe gatos acima de 5 ");
         }
        
        Porcent = (outros/5)*100;
        System.out.println("A porcentagem de outros animais é: " + Porcent + "%");

        System.out.println("A espécie do animal mais leve é: " + ESml);
        System.out.println("A idade do animal mais leve é: " + IDml);
        
    }
    
}