import java.util.Arrays;
import java.util.Scanner;


public class Tasck_02 {
    public static void main(String[] args) {
        // заполняем массив
        Scanner sc = new Scanner(System.in);
            System.out.print("Введите количество элементов массива: ");
            int n = sc.nextInt();
            int[] newArr = new int[n];
            System.out.println("Введите элементы массива: ");
            for (int i = 0; i < n; i++){
                newArr[i] = sc.nextInt();           
            }
            System.out.println("Исходный массив: " + Arrays.toString(newArr));
        //сортируем массив
            int[] filterArr = Arrays.stream(newArr).filter(i -> i%2 != 0).toArray();
            System.out.println("Полученный массив: " + Arrays.toString(filterArr));
    } 
}