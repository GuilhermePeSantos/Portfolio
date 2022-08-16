package teste;
import java.util.Scanner;
public class Vôos {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        
        int x = 1, i, achou = 0, indice = 0, proc = 0;
        
        //Numero do vôo
        int NV[] = new int[10];
        int NumV = 0;

        //Origem
        String OR[] = new String[10];
        String Ori;

        //Destino
        String DT[] = new String[10];
        String Dest;

        //Numero de lugares
        int NL[] = new int[10];
        int NumL = 0;
        
        while(x>=1 && x<=3){
            System.out.println("\n1 - Cadastrar vôos"
                                + "\n2 - Consultar vôos"
                                + "\n3 - Efetuar reserva"
                                + "\n4 - Sair"
                                + "\nDigite o que deseja fazer:");
            x = scan.nextInt();
            
            switch(x){
                case 1: System.out.println("\n-CADASTRO DE VÔOS-");
                    System.out.println("Digite o numero do vôo:");
                    NumV = scan.nextInt();
                       
                    achou = 0;
                    for (i = 0; i < 10; i++) {
                        if(NumV == NV[i]){
                            achou = 1;
                        }
                    }
                    
                    if(achou == 1){
                        System.out.println("\nNumero do vôo ja existe!");
                    }
                    
                    if(achou == 0 && indice < 10){
                        NV[indice] = NumV;
                        
                        System.out.println("Digite a origem:");
                        Ori = scan.next();
                        OR[indice] = Ori;
                        
                        System.out.println("Digite o destino:");
                        Dest = scan.next();
                        DT[indice] = Dest;
                        
                        System.out.println("Digite o numero de lugares:");
                        NumL = scan.nextInt();
                        NL[indice] = NumL;
                        
                        System.out.println("\nVôo cadastrado com sucesso!");
                        indice++;
                    }
                    if(indice > 9){
                        System.out.println("\nLimite de cadastro atingido!");
                    }
                break;
                       
                case 2:
                    System.out.println("\n-CONSULTA DE VÔO-");
                    System.out.println("\n1 - Por número do vôo"
                                + "\n2 - Por origem"
                                + "\n3 - Por destino"
                                + "\nDigite:");
                    x = scan.nextInt();
                    
                    switch(x){
                        case 1:
                                System.out.println("Digite o numero do vôo:");
                                NumV = scan.nextInt();
                               
                                achou = 0;
                                proc = 0;
                                for(i = 0; i < 10; i++){
                                    if(NumV == NV[i]){
                                        achou = 1;
                                        proc = i;
                                    }
                                }

                                if(achou == 1){
                                    System.out.println("\nOrigem: " + OR[proc]);
                                    System.out.println("Destino: " + DT[proc]);
                                    System.out.println("Numero de lugares: " + NL[proc]);
                                }

                                if(achou == 0){
                                    System.out.println("\nVôo nao encontrado!");
                                }
                        break;
                                    
                        case 2:
                                System.out.println("Digite a origem do vôo:");
                                Ori = scan.next();
                               
                                achou = 0;
                                proc = 1;
                                for(i = 0; i < 10; i++){
                                    if(Ori.equals(OR[i])){
                                        achou = 1;
                                        System.out.println("\n" + proc + "°");
                                        System.out.println("Origem: " + OR[i]);
                                        System.out.println("Destino: " + DT[i]);
                                        System.out.println("Numero de lugares: " + NL[i]);
                                        proc++;
                                    }
                                }

                                if(achou == 0){
                                    System.out.println("\nOrigem nao encontrado!");
                                }
                        break;
                                    
                        case 3:
                                System.out.println("Digite o destino do vôo:");
                                Dest = scan.next();
                               
                                achou = 0;
                                proc = 1;
                                for(i = 0; i < 10; i++){
                                    if(Dest.equals(DT[i])){
                                        achou = 1;
                                        System.out.println("\n" + proc + "°");
                                        System.out.println("Origem: " + OR[i]);
                                        System.out.println("Destino: " + DT[i]);
                                        System.out.println("Numero de lugares: " + NL[i]);
                                        proc++;
                                    }
                                }

                                if(achou == 0){
                                    System.out.println("\nDestino nao encontrado!");
                                }
                        break;
                            }
                break;
                
                case 3:
                    System.out.println("\n-RESERVA DE VÔO-");
                    System.out.println("Digite o número do vôo:");
                    NumV = scan.nextInt();
                    
                    achou = 0;
                    proc = 0;
                    for(i = 0; i < 10; i++){
                        if(NumV == NV[i]){
                            achou = 1;
                            proc = i;
                        }
                    }
                    
                    if(achou == 1 && NL[proc] > 0){
                        System.out.println("\nReserva confirmada!");
                        NL[proc] = NL[proc] - 1;
                    }else if(achou == 0){
                        System.out.println("\nVôo inexistente!");
                    }else if(NL[proc] < 1){
                        System.out.println("\nVôo lotado!");
                    }
                break;
            }
        }
    }
}
