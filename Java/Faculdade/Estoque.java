
package teste;
import java.util.Scanner;
public class Estoque {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
            
        int x, i, achou = 0, indice = 0, proc = 0;
        
        //Codigo do produto
        int CP[] = new int[10];
        int CodP = 0;
        
        //Descrição do produto
        String DP[] = new String[10];
        String DescP;
        
        //Categoria do produto
        String CatP[] = new String[10];
        String CategP;
        
        //Preço unitario
        double PU[] = new double[10];
        double PrecU = 0;
        
        //Quantidade em estoque
        int QTDE[] = new int[10];
        int QTD = 0;
        
        do{
            System.out.println("\n---MENU---"
                                + "\n1 - Cadastrar produtos"
                                + "\n2 - Consultar produto"
                                + "\n3 - Adicionar ou Retirar do estoque"
                                + "\n4 - Sair"
                                + "\nDigite o que deseja fazer:");
            x = scan.nextInt();
            
            switch(x){
                case 1:System.out.println("\n-----CADASTRO DE PRODUTO-----");
                    System.out.println("Digite o CODIGO DO PRODUTO:");
                    CodP = scan.nextInt();
                       
                    achou = 0;
                    for (i = 0; i < 10; i++) {
                        if(CodP == CP[i]){
                            achou = 1;
                        }
                    }
                    
                    if(achou == 1){
                        System.out.println("\nPRODUTO JA CADASTRADO!");
                    }
                    
                    if(achou == 0 && indice < 10){
                        CP[indice] = CodP;
                        
                        System.out.println("Digite a DESCRIÇÃO DO PRODUTO:");
                        DescP = scan.next();
                        DP[indice] = DescP;
                        
                        System.out.println("Digite a CATEGORIA DO PRODUTO:");
                        CategP = scan.next();
                        CatP[indice] = CategP;
                        
                        System.out.println("Digite o PREÇO UNITARIO DO PRODUTO:");
                        PrecU = scan.nextDouble();
                        PU[indice] = PrecU;
                        
                        System.out.println("Digite a QUANTIDADE EM ESTOQUE DO PRODUTO:");
                        QTD = scan.nextInt();
                        QTDE[indice] = QTD;
                        
                        System.out.println("\nPRODUTO CADASTRADO COM SUCESSO!");
                        indice++;
                    }
                    if(indice > 9){
                        System.out.println("\nLIMITE DE CADASTRO ATINGIDO");
                    }
                    break;
                
                case 2: System.out.println("\n-----CONSULTA DE PRODUTO-----");
                    System.out.println("Digite o codigo do produto:");
                    CodP = scan.nextInt();
                    
                    achou = 0;
                    proc = 0;
                    for(i = 0; i < 10; i++){
                        if(CodP == CP[i]){
                            achou = 1;
                            proc = i;
                        }
                    }
                    
                    if(achou == 1){
                        System.out.println("\nDESCRIÇÂO: " + DP[proc]);
                        System.out.println("CATEGORIA: " + CatP[proc]);
                        System.out.println("PREÇO UNITARIO: R$" + PU[proc]);
                        System.out.println("QUANTIDADE EM ESTOQUE: " + QTDE[proc]);
                    }
                    
                    if(achou == 0){
                        System.out.println("\nPRODUTO NÂO ENCONTRADO!");
                    }
                    break;
                    
                case 3:System.out.println("Digite o codigo do produto:");
                    CodP = scan.nextInt();
                    
                    achou = 0;
                    proc = 0;
                    for(i = 0; i < 10; i++){
                        if(CodP == CP[i]){
                            achou = 1;
                            proc = i;
                        }
                    }
                    
                    if(achou == 1){
                        System.out.println("\n1 - Adicionar | 2 - Retirar");
                        System.out.println("Digite:");
                        x = scan.nextInt();

                        switch(x){
                            case 1:
                                   System.out.println("Digite a quantidade que deseja adicionar:");
                                   QTD = scan.nextInt();
                                   
                                   QTDE[proc] = QTDE[proc] + QTD; 
                                   System.out.println("\nQuantidade do estoque atualizada!");
                                   System.out.println("Estoque atual deste produto: " + QTDE[proc]);
                                   break;
                            
                            case 2:
                                   if(QTDE[proc] < 1){
                                       System.out.println("ESTOQUE VAZIO!");
                                   }else{
                                        System.out.println("Digite a quantidade que deseja retirar:");
                                        QTD = scan.nextInt();
                                        
                                        if(QTD <= QTDE[proc]){
                                        QTDE[proc] = QTDE[proc] - QTD; 
                                        System.out.println("\nQuantidade do estoque atualizada!");
                                        System.out.println("Estoque atual deste produto: " + QTDE[proc]);
                                        }else{
                                            System.out.println("ESTOQUE INSUFUCIENTE!");
                                        }
                                   }
                                   break;
                        }
                    }
                    if(achou == 0){
                           System.out.println("\nPRODUTO NÂO ENCONTRADO!");
                       }
                    break;
            }
        }while(x>=1 && x<=3);
    }
}

