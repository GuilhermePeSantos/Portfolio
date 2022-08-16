
package teste;
import java.util.Scanner;
public class ex02 {
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        
        char x = 'a',tipo = 'x';
        double precoU;
        
        //A
        int estoque=0;
        
        //B
        double VEst,VTEst=0;
        
        //C
        int produt=0, ETC=0;
        double porcent;
        
        //D
        double mediaPU, PU=0;
        int TP=0;
        
        //E
        double PMC=0;
        char categoria='x';
        int QTDE=0;
        
        do{
            System.out.println("Digite o tipo do produto: "
                                + "\np – perecível"
                                + "\nl – limpeza"
                                + "\nh – higiene pessoal");
            tipo = scan.next().charAt(0);
            //Validação
            while(tipo != 'p' && tipo != 'l' && tipo != 'h'){
                System.out.println("\n--LETRA INVALIDA--");
                System.out.println("Digite novamente o tipo do produto: "
                                + "\np – perecível"
                                + "\nl – limpeza"
                                + "\nh – higiene pessoal");
                tipo = scan.next().charAt(0);
            }
            
            System.out.println("Digite a quantidade em estoque: ");
            estoque = scan.nextInt();
            
            System.out.println("Digite o preço unitario: ");
            precoU = scan.nextDouble();
            
            //A
            if(estoque > 30){
                System.out.println("\n - Estoque alto!\n");
            }else if(estoque <= 30 && estoque >=10){
                System.out.println(" - Estoque normal!\n");
            }else if(estoque < 10 && estoque > 0){
                System.out.println(" - Estoque crítico!\n");
                ETC++;
            }else{
                System.out.println(" - PRODUTO ESGOTADO!!\n");
            }
            
            
            //B
            VEst = estoque*precoU;
            System.out.println(" - O valor total em estoque é: R$" + VEst + "\n");
            
            //C
            produt++;
            
            //D
            if(tipo == 'p'){
                TP++;
                PU = PU + precoU;
            }
            
            //E
            if(produt == 1){
                PMC = precoU;
                categoria = tipo;
                QTDE = estoque;
            }
            
            if(precoU > PMC){
                PMC = precoU;
                categoria = tipo;
                QTDE = estoque;
            }
            
            //Validação
            System.out.println("Deseja continuar? s-sim n-nao");
            x = scan.next().charAt(0);
            
            while(x != 's' && x != 'n'){
                System.out.println("--LETRA INVALIDA--");
                System.out.println("Deseja continuar? s-sim n-nao");
                x = scan.next().charAt(0);
            }
        }while(x == 's');
        
        //C
        porcent = ((ETC/(double)produt)*100);
        System.out.printf("\n - A porcentagem de produtos em estoque critico é: %.2f" , porcent);
        System.out.println("%");
        
        //D
        mediaPU = PU/TP;
        System.out.printf("\n%.2f - O preço unitário médio de produtos do tipo p é: R$" , mediaPU);
        
        //E
        System.out.println("\n\n - A categoria do produto mais caro é: " + categoria);
        System.out.println(" - A quantidade em estoque do produto mais caro é: " + QTDE);
    }
    
}
    