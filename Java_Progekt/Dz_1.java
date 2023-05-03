import java.util.Scanner;

//*  Вычислить n-ое треугольного число(сумма чисел от 1 до n)

public class Task01 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in, "cp866");

        System.out.println("Введите число для вычисления ");
        System.out.print("треугольного числа и факториала: ");

        int number = Integer.parseInt(sc.nextLine());
        sc.close();

        // Рекурсивные методы
        System.out.println("Рекурсивные методы:");
        System.out.println(recTriangNumber(number));
        System.out.println(recFactorial(number));

        // Стандартные методы
        System.out.println("Стандартные методы:");
        System.out.println(triangNumber(number));
        System.out.println(factorial(number));
    }

    public static int recTriangNumber(int number) {
        if (number < 1) return 0;
        return number + recTriangNumber(number - 1);
    }

    public static int recFactorial(int number) {
        if (number < 2) return 1;
        return number * recFactorial(number - 1);
    }

    public static int triangNumber(int number) {
        int sum = 0;

        for (int i = 1; i <= number; i++) sum += i;

        return sum;
    }

    public static int factorial(int number) {
        int fact = 1;
        for (int i = 2; i <= number; i++) fact *= i;

        return fact;
    }
}

//* Вывести все простые числа от 1 до 1000

public class Task02 {
    public static void main(String[] args) {
        for (int i = 0; i <= 1000; i++)
            if (isPrime(i))
                System.out.print(i + " ");
    }

    public static boolean isPrime(int number) {
        for (int i = 2; i * i <= number; i++)
            if (number % i == 0) return false;
        return true;
    }
}
//* Реализовать простой калькулятор (+ - / *)

public class Task03 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in, "cp866");

        System.out.print("Введите первое число: ");
        double number1 = Double.parseDouble(sc.nextLine());

        System.out.print("Введите действие: ");
        String action = sc.nextLine();

        System.out.print("Введите второе число: ");
        double number2 = Double.parseDouble(sc.nextLine());

        sc.close();

        System.out.print(number1 + " " + action + " " + number2 + " = ");

        switch (action) {
            case "+":
                System.out.println(number1 + number2);
                break;
            case "-":
                System.out.println(number1 - number2);
                break;
            case "*":
                System.out.println(number1 * number2);
                break;
            case "/":
                System.out.println(number1 / number2);
                break;
            default:
                System.out.println("Некорректное действие!");
        }
    }
}