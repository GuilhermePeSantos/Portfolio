
package teste;
import java.util.Scanner;
public class ex03 {
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
      
        int x=0;
        
        System.out.println("Digite um valor para X: ");
        x = scan.nextInt();
        
        switch (x){
            case 1:System.out.println("Voce escolheu 1");
            break;
            case 2:System.out.println("Voce escolheu 2");
            break;
            case 3:System.out.println("Voce escolheu 3");
            break;
            case 4:System.out.println("Voce escolheu 4");
            break;
            case 5:System.out.println("Voce escolheu 5");
            break;
            case 6:System.out.println("Voce escolheu 6");
            break;
        }
        
    }
}
