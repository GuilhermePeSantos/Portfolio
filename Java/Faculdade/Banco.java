package teste;

import java.util.Scanner;

public class Banco {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        int x = 1, achou = 0, i = 0;

        //Numero da Conta
        int NC[] = new int[10];
        int NumC = 0;
        int indice = 0;
        int proc = 0;

        //Tipo da Conta 
        String TC[] = new String[10];
        String TiC = "x";

        //Nome do Cliente 
        String NoCl[] = new String[10];
        String NomCl = "x";

        //CPF 
        int CPF[] = new int[10];
        int cpf = 0;

        //Telefone
        int Tel[] = new int[10];
        int tel = 0;

        //Saldo
        double Saldo[] = new double[10];
        double saldo = 0;

        //Saque
        double Saq_Dep = 0;

        while (x >= 1 && x <= 4) {
            System.out.println("\nDigite o que deseja fazer: "
                    + "\n1 - Cadastrar contas"
                    + "\n2 - Visualizar os dados de um cliente"
                    + "\n3 - Realizar um Saque"
                    + "\n4 - Realizar um Depósito"
                    + "\n5 - Sair");
            x = scan.nextInt();

            switch (x) {
                case 1:
                    System.out.println("\n\n-------Cadastro de Conta-------");

                    System.out.println("Digite o NÚMERO DA CONTA:");
                    NumC = scan.nextInt();

                    achou = 0;
                    for (i = 0; i < 10; i++) {
                        if (NumC == NC[i]) {
                            achou = 1;
                        }
                    }

                    if (achou == 1) {
                        System.out.println("\nESSA CONTA JÁ EXISTE!!");
                    }

                    if (achou == 0) {
                        NC[indice] = NumC;

                        System.out.println("\nDigite o TIPO DA CONTA:");
                        TiC = scan.next();
                        TC[indice] = TiC;

                        System.out.println("\nDigite o NOME DO CLIENTE:");
                        NomCl = scan.next();
                        NoCl[indice] = NomCl;

                        System.out.println("\nDigite o seu CPF:");
                        cpf = scan.nextInt();
                        CPF[indice] = cpf;

                        System.out.println("\nDigite o seu TELEFONE:");
                        tel = scan.nextInt();
                        Tel[indice] = tel;

                        System.out.println("\nDigite o seu SALDO:");
                        saldo = scan.nextDouble();
                        Saldo[indice] = saldo;

                        System.out.println("\nCONTA CADASTRADA COM SUCESSO!!");
                        indice++;
                    }
                    break;

                case 2:
                    System.out.println("\nDigite o NUMERO DA CONTA:");
                    NumC = scan.nextInt();

                    proc = 0;
                    achou = 0;
                    i = 0;
                    do {
                        if (NumC == NC[i]) {
                            achou = 1;
                            proc = i;
                        }
                        i++;
                    } while (achou == 0 && i < 10);
                    
                    if (achou == 1) {
                        System.out.println("\n NOME DO CLIENTE: " + NoCl[proc]);
                        System.out.println(" TIPO DA CONTA: " + TC[proc]);
                        System.out.println(" CPF: " + CPF[proc]);
                        System.out.println(" TELEFONE: " + Tel[proc]);
                        System.out.println(" SALDO: " + Saldo[proc]);
                        }
            

                    if (achou == 0) {
                        System.out.println("\nCONTA NÃO ENCONTRADA!");
                    }
                    break;

                case 3:
                    System.out.println("\nDigite o NUMERO DA CONTA:");
                    NumC = scan.nextInt();

                    proc = 0;
                    achou = 0;
                    i = 0;
                    do {
                        if (NumC == NC[i]) {
                            achou = 1;
                            proc = i;
                        }
                        i++;
                    } while (achou == 0 && i < 10);

                    if (achou == 1) {
                        System.out.println("\nNome da conta: " + NoCl[proc]);
                        System.out.println("Digite o VALOR DE SAQUE R$:");
                        Saq_Dep = scan.nextInt();

                        if (Saq_Dep > Saldo[proc]) {
                            System.out.println("\nSALDO INSUFICIENTE!");
                        } else {
                            Saldo[proc] = Saldo[proc] - Saq_Dep;
                            System.out.println("\nSaque realizado com sucesso!");
                            System.out.println(" - Saldo atual: R$" + Saldo[proc]);
                        }
                    }

                    if (achou == 0) {
                        System.out.println("\nCONTA NÃO ENCONTRADA!");
                    }
                    break;

                case 4:
                    System.out.println("\nDigite o NUMERO DA CONTA:");
                    NumC = scan.nextInt();

                    proc = 0;
                    achou = 0;
                    i = 0;
                    do {
                        if (NumC == NC[i]) {
                            achou = 1;
                            proc = i;
                        }
                        i++;
                    } while (achou == 0 && i < 10);

                    if (achou == 1) {
                        System.out.println("\nNome da conta: " + NoCl[proc]);
                        System.out.println("Digite o VALOR DE DEPÓSITO R$:");
                        Saq_Dep = scan.nextInt();

                        Saldo[proc] = Saldo[proc] + Saq_Dep;
                        System.out.println("\nDepósito realizado com sucesso!");
                        System.out.println(" - Saldo atual: R$" + Saldo[proc]);
                    }

                    if (achou == 0) {
                        System.out.println("\nCONTA NÃO ENCONTRADA!");
                    }
                    break;
            }
        }
    }
}
