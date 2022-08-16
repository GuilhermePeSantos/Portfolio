package teste;
import java.util.Scanner;
public class Vendas {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        
        int i = 0;
        //1
        String NC[] = {"Ana", "Luis", "Bia", "Ivo", "Ana", "Luis", "Bia", "Ana", "Bia", "Ian"};
        double VB[] = {400.00, 700.00, 200.00, 900.00, 500.00, 800.00, 100.00, 600.00, 300.00, 150.00};
        int NP[] = {1, 2, 1, 3, 2, 3, 1, 3, 2, 1};

            System.out.println("Nome do cliente    ValorBase    NumPrestacoes");
            for (i = 0; i < 10; i++) {
                System.out.printf("%15s %12.2f %16d\n",NC[i],VB[i],NP[i]);
            }
        
        //2
        double mediaA, somaA = 0;
        int contadorA = 0;
        
            for (i = 0; i < 10; i++) {
                if(NP[i] == 1){
                    somaA = somaA + VB[i];
                    contadorA++;
                }
            }
        
        mediaA = somaA/contadorA;
        System.out.printf("\n - A media das vendas á vista é: R$%.2f\n", mediaA);
        
        //3
        double maior = VB[0];
        String nome = NC[0];
        int NumP = NP[0];
        
            for (i = 0; i < 10; i++) {
                if(VB[i] > maior){
                    maior = VB[i];
                    nome = NC[i];
                    NumP = NP[i];
                }
            }
            System.out.printf("\n - O valor da venda mais cara é: R$%.2f\n", maior);
            System.out.println(" - O nome do cliente da venda mais cara é: " + nome);
            if(NumP > 1){
                System.out.println(" - Venda em " + NumP + " prestações");
            }else{
                System.out.println(" - Venda à vista");
            }
            
            //4
            String Nome;
            double VTotal = 0;
            
                System.out.println("\nDigite o nome do cliente:");
                Nome = scan.next();
            
                for (i = 0; i < 10; i++) {
                    if(Nome.equals(NC[i])){
                        System.out.printf(" - Compra de R$%.2f\n",VB[i]);
                        VTotal = VTotal + VB[i];
                    }
                }
                System.out.printf(" - O valor total comprado é: R$%.2f\n", VTotal);
                
            //5
            double desc_acre = 0, Caixa = 50;
            
            for (i = 0; i < 10; i++) {
                
                if(NP[i] == 1){
                    desc_acre = VB[i] - (VB[i]*0.05);
                    Caixa = Caixa + desc_acre;
                }
                if(NP[i] == 2){
                    Caixa = Caixa + (VB[i]/NP[i]);
                }
                if(NP[i] == 3){
                    desc_acre = VB[i] + (VB[i]*0.10);
                    Caixa = Caixa + (desc_acre/NP[i]);
                }
            }
            System.out.printf("\n - O valor total do caixa no dia é: R$%.2f\n", Caixa);
            
    }
}