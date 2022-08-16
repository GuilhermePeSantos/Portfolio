package teste;
import java.util.Scanner;
public class Livraria {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        
        int x = 1, achou = 0, i = 0;

        //Código do livro
        int CL[] = new int[10];
        int CodL = 0;
        int indice = 0;
        int proc = 0;

        //Area
        String Area[] = new String[10];
        String AR = "x";

        //Editora 
        String Editora[] = new String[10];
        String Edit = "x";

        //Nome da obra 
        String NomeObra[] = new String[10];
        String NomObr = "x";

        //Nome do autor
        String NomeAutor[] = new String[10];
        String NomAut = "x";

        //Quantidade de exemplares
        int QuantExemp[] = new int[10];
        int QtdEx = 0;
        int soma = 0;

        while (x >= 1 && x <= 4) {
            System.out.println("\nDigite o que deseja fazer: "
                    + "\n1 - Cadastro de um novo livro"
                    + "\n2 - Mostrar as obras e a quantidade de exemplares de um determinado autor"
                    + "\n3 - Fazer um pesquisa por Obra (Título)"
                    + "\n4 - Realizar venda de um livro"
                    + "\n5 - Sair");
            x = scan.nextInt();

            switch (x) {
                case 1:
                    System.out.println("\n\n------Cadastro de um novo livro------");

                    System.out.println("Digite o código do novo livro:");
                    CodL = scan.nextInt();

                    achou = 0;
                    for (i = 0; i < 10; i++) {
                        if (CodL == CL[i]) {
                            achou = 1;
                        }
                    }

                    if (achou == 1) {
                        System.out.println("\nESSE LIVRO JÁ ESTÁ CADASTRADO!!");
                    }

                    if (achou == 0) {
                        CL[indice] = CodL;

                        System.out.println("\nDigite a área do livro:");
                        AR = scan.next();
                        Area[indice] = AR;

                        System.out.println("\nDigite a editora do livro:");
                        Edit = scan.next();
                        Editora[indice] = Edit;

                        System.out.println("\nDigite o nome da obra:");
                        NomObr = scan.next();
                        NomeObra[indice] = NomObr;

                        System.out.println("\nDigite o nome do autor:");
                        NomAut = scan.next();
                        NomeAutor[indice] = NomAut;

                        System.out.println("\nDigite a quantidade de exemplares:");
                        QtdEx = scan.nextInt();
                        QuantExemp[indice] = QtdEx;

                        System.out.println("\nLIVRO CADASTRADA COM SUCESSO!!");
                        indice++;
                    }

                    break;
                    
                case 2:
                    System.out.println("Digite o nome do autor:");
                    NomAut = scan.next();
                    
                    System.out.println("As obras são:");
                    for (i = 0; i < 10; i++) {
                        if (NomAut.equals(NomeAutor[i])) {
                            System.out.println("Obra: " + NomeObra[i]);
                            System.out.println("QTD de exemplares: \n" + QuantExemp[i]);
                        }
                    }
                    break;
                }
            }
        }
    }


