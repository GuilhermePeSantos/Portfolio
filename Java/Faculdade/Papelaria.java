package teste;
import java.util.Scanner;
public class Papelaria {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        
        //1
        int i = 0;
        String DC[] = {"caneta","lapis","caderno","borracha","regua","apontador"};
        int QTD_ET[] = {35,40,10,20,30,60};
    //    double PU[] = {2,2,2,2,2,2};
        double PU[] = {100,1,2,3,10,5};
        
        //2
        double mediaPU, somaPU = 0;
        
        //3
        String Desc;
        double maior;
        
        //4
        String nome;
        
        //5
        double desc = 0;
        
        //1
        System.out.println("Descrição    " + "Quantidade em estoque    " + "Preçu Unitario ");
        maior = PU[0];
        Desc = DC[0];
        for (i = 0; i < 6; i++) {
            System.out.printf("%9s %24d %17.2f\n",DC[i],QTD_ET[i],PU[i]);
            
            //2
            somaPU = somaPU + PU[i];
            
            //3
                if(PU[i] > maior){
                    Desc = DC[i];
                    maior = PU[i];
                }
        }
        
        
        //2
        mediaPU = somaPU/6;
        System.out.printf("\n - A media dos preços unitarios é: R$%.2f", mediaPU);
        
        //3
        System.out.println("\n - O produto mais caro é: " + Desc + " | R$" + maior);
        
        //4
        System.out.println("\nDigite o nome do produto:");
        nome = scan.next();
        
        for (i = 0; i < 6; i++) {
            if(nome.equals(DC[i])){
                System.out.println(" - Quantidade em estoque: " + QTD_ET[i]);
                System.out.println(" - Preço unitario: R$" + PU[i]);
                
                if(QTD_ET[i] > 30){
                    desc = PU[i] - (PU[i]*0.10);
                    System.out.println(" - Valor com desconto: R$" + desc);
                }
                if(QTD_ET[i] > 40){
                    desc = PU[i] - (PU[i]*0.20);
                    System.out.println(" - Valor com desconto: R$" + desc);
                    
                }
                
            }
        }
    }
}

//6
//Os vetores são variaveis compostas que armazenam varias variaveis do mesmo tipo, que são identificadas por cada celulas do vetor. 
