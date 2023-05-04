import java.util.LinkedList;
import java.util.Scanner;

public class DZ_04 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        LinkedList<String> list = new LinkedList<>();

        while (true) {
            System.out.println("Введите строку (Введите print выводит строки/revert удаляет предыдущую введенную строку/exit выход):");
            String input = scanner.nextLine();

            

            if (input.equals("print")) {
                System.out.println("Строки в обратном порядке:");
                while (!list.isEmpty()) {
                    System.out.println(list.removeLast());
                }
            } else if (input.equals("revert")) {
                if (!list.isEmpty()) {
                    list.removeLast();
                    System.out.println("Последняя введенная строка удалена из памяти.");
                } else {
                    System.out.println("Нет сохраненных строк для удаления.");
                }
            } else {
                
                if ((input.equals("exit"))) {
                    System.out.println(list.removeLast());
                }
            }
        
        

        
        
        }

   
   
   
    }
}