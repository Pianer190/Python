

<details><summary><h2>Семинар 6</h2></summary>

  - [x] Подумать над структурой класса Ноутбук для магазина техники - выделить поля и методы. Реализовать в java.
  - [x] Создать множество ноутбуков.
  - [x] Написать метод, который будет запрашивать у пользователя критерий фильтрации и выведет ноутбуки, отвечающие фильтру. Критерии фильтрации можно хранить в Map. минимум 5 NoteBook notebook1 = new NoteBook NoteBook notebook2 = new NoteBook NoteBook notebook3 = new NoteBook NoteBook notebook4 = new NoteBook NoteBook notebook5 = new NoteBook
Например:

```
Введите цифру, соответствующую необходимому критерию:
1 - ОЗУ
2 - Объем ЖД
3 - Операционная система
4 - Цвет
```

Дал


Приветствие
Выбор параметра:
1 - ОЗУ
2 - Объем ЖД
3 - Операционная система
4 - Цвет
выбор конкретнее
1 ---> Введите колво ---> 16
вывод всех подходящих ноутбуков по параметру


</details>

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Scanner;
import java.util.*;

//Создать класс Ноутбук и метод для фильтрации экземпляров данного класса по параметрам, введенными пользователем

public class Final_task {
    public static void main(String[] args) {
        ArrayList<Laptop> laptops = getLaptopList();
        HashMap<Integer, String> sortingValues = getSortingMap();
        HashMap<String, ArrayList<String>> allStr = getStringChoices(sortingValues, laptops);
        Scanner sc = new Scanner(System.in);

        int firstChoice = sortFirst(sortingValues, sc);
        int firstChoice = filterFirst(sortingValues, sc);

        System.out.println(firstChoice);
        int secondChoice = filterSecond(sortingValues, laptops, allStr, sc, firstChoice);

        for (Laptop el: laptops) el.getInfo();
        filterFinal(firstChoice, secondChoice, allStr, laptops);

        sc.close();
    }

    public static int sortSecond(HashMap<Integer, String> hm, Scanner sc) {
        return 1;
     //финальный этапа фильтрации и вывод результатов в консоль
    public static void filterFinal(int first, int second, HashMap<String, ArrayList<String>> strMap, ArrayList<Laptop> al) {
        ArrayList<Laptop> matching = new ArrayList<>();

        switch (first) {
            case 1:
                for (Laptop el: al)
                    if (el.ramGB >= second)
                        matching.add(el);
                break;

            case 2:
                for (Laptop el: al)
                    if (el.romGB >= second)
                        matching.add(el);
                break;

            case 3:
                if (strMap.get("Операционная система").size() <= second - 1 || second < 1) {
                    System.out.println("Такого выбора нет!");
                    break;
                }

                for (Laptop el: al)
                    if (strMap.get("Операционная система").get(second - 1).equals(el.os))
                        matching.add(el);
                break;

            case 4:
                if (strMap.get("Цвет").size() <= second - 1 || second < 1) {
                    System.out.println("Такого выбора нет!");
                    break;
                }

                for (Laptop el: al)
                    if (strMap.get("Цвет").get(second - 1).equals(el.color))
                        matching.add(el);
                break;

            default:
                break;
        }

        if (matching.size() < 1) System.out.println("Нет подходящих вариантов(");
        else {
            System.out.println("\n---- Все подходящие варианты ----\n");
            for (Laptop el: matching) el.getInfo();
            System.out.println("\n---------------------------------\n");
        }
    }

    // Метод для проведения второго этапа фильтрации
    public static int filterSecond(HashMap<Integer, String> hm, ArrayList<Laptop> al, HashMap<String, ArrayList<String>> strMap, Scanner sc, int firstChoice) {
        int choice = -1;

        if (firstChoice > 0 && firstChoice < 3) {
            System.out.println("Напишите минимально подходящее кол-во памяти (" + hm.get(firstChoice) + ").");
            System.out.print("Кол-во памяти (ГБ): ");

            choice = sc.nextInt();
            sc.nextLine();
        }

        else if (firstChoice > 2 && firstChoice < 5) {
            ArrayList<String> strChoices = strMap.get(hm.get(firstChoice));
            System.out.println("Выберите один из подходящих вариантов (" + hm.get(firstChoice) + "):");

            for (int i = 0; i < strChoices.size(); i++) {
                System.out.println((i + 1) + ". " + strChoices.get(i));
                }

            System.out.print("\nВаш выбор: ");
            choice = sc.nextInt();
            sc.nextLine();
        }

        else {
            System.out.println("Такого выбора нет!");
            }

        return choice;
    }

    // Метод для создания словаря с уникальными значениями ОС и цвета
    public static HashMap<String, ArrayList<String>> getStringChoices(HashMap<Integer, String> hm, ArrayList<Laptop> al) {
        HashMap<String, ArrayList<String>> strMap = new HashMap<>();


        HashSet<String> oses = new HashSet<>();
        HashSet<String> colors = new HashSet<>();
        ArrayList<String> osList = new ArrayList<>();
        ArrayList<String> colorList = new ArrayList<>();

        for (Laptop el: al) {
            oses.add(el.os);
            colors.add(el.color);
        }

        osList.addAll(oses);
        colorList.addAll(colors);

        strMap.put(hm.get(3), osList);
        strMap.put(hm.get(4), colorList);

        return strMap;
    }

    public static int sortFirst(HashMap<Integer, String> hm, Scanner sc) {
    // Метод для проведения первого этапа фильтрации
    public static int filterFirst(HashMap<Integer, String> hm, Scanner sc) {
        System.out.println("Выберите цифру, соответствующую необходимому критерию:");

        for (var el: hm.entrySet()) System.out.println(el.getKey() + ". " + el.getValue());
        System.out.println();
        System.out.print("Ваш выбор:");

        System.out.print("\nВаш выбор: ");
        int choice = sc.nextInt();
        sc.nextLine();

        return choice;
    }

    // Метод для создания словаря с критериями фильтрации
    public static HashMap<Integer, String> getSortingMap() {
        HashMap<Integer, String> hm = new HashMap<>();
        hm.put(1, "ОЗУ");
     public static HashMap<Integer, String> getSortingMap() {
        return hm;
    }


    // Метод для создания списка ноутбуков
    public static ArrayList<Laptop> getLaptopList() {
        ArrayList<Laptop> al = new ArrayList<>();
        Laptop testLaptop = new Laptop("Test Laptop", "White", 16, 512, "No OS");
        Laptop testLaptop = new Laptop("Test Laptop", "White", 16, 512, "DOS");
        Laptop macbook = new Laptop("Apple MacBook Air 13\"", "Silver", 8, 256, "MacOS");
        Laptop irbis = new Laptop("IRBIS NB80", "Black", 2, 32, "Windows 10 Home");
        Laptop hpLaptop = new Laptop("hp 255 g9 5Y3X5EA", "Dark gray", 16, 512, "FreeDOS");
}   }        