# Звіт до роботи
## Тема: Тестування та юніт-тести у Python
### Мета роботи: Навчитись перевіряти правильність роботи програм, використовувати assert, unittest та PyTest, а також збирати статистику покриття коду за допомогою coverage.

---

### Виконання роботи

* Результати виконання завдань:

1. **Перевірка assert та валідація даних**
    - Введення числа через `input`:
      ```python
      a = input("Enter a number: ")
      assert a.isdigit(), "Input must be a number"
      a = int(a)
      assert a > 0, "Number must be greater than zero"
      print(f"Entered number: {a}")
      ```
      - При введенні `5` → `Entered number: 5` ✅
      - При введенні `-3` → `AssertionError: Number must be greater than zero` ❌
      - При введенні `abc` → `AssertionError: Input must be a number` ❌

2. **Клас Figure з assert**
    ```python
    class Figure:
        FIGURES = ["square", "rectangle", "triangle"]

        def __init__(self, figure_type, length):
            assert length > 0, "Length must be greater than zero"
            assert figure_type in self.FIGURES, "Invalid figure type"
            self.figure_type = figure_type
            self.length = length
    ```
    - Створення обʼєктів:
      - `Figure("square", 1)` → створено ✅
      - `Figure("trapezoid", 12)` → AssertionError ❌
      - `Figure("square", 0)` → AssertionError ❌

3. **Клас Name з ValueError**
    ```python
    class Name:
        def __init__(self, name, hobby):
            if name not in ["Bohdan", "Anonymous", "Artem"]:
                raise ValueError("Invalid name")
            if not hobby:
                raise ValueError("Hobby must not be empty")
            self.name = name
            self.hobby = hobby

    a = Name("Artem", "programming")   # ✅
    b = Name("Bodko", "football")      # ❌ ValueError
    c = Name("Artem", "")               # ❌ ValueError
    ```

4. **Юніт-тести через unittest**
    ```python
    import unittest
    from random import choice, randint
    from app import Figure

    class TestFigure(unittest.TestCase):
        def setUp(self):
            self.figure = choice(Figure.FIGURES)
            self.length = randint(1, 10)
            self.obj = Figure(self.figure, self.length)

        def tearDown(self):
            del self.obj

        def test_figure_type(self):
            self.assertEqual(self.figure, self.obj.get_figure_type)

        def test_figure_length(self):
            self.assertEqual(self.length, self.obj.get_figure_length)

        def test_invalid_object(self):
            with self.assertRaises(AssertionError):
                Figure("circle", 1)

    if __name__ == "__main__":
        unittest.main(verbosity=2)
    ```
    - Результати запуску:
      - `test_figure_type` → ✅
      - `test_figure_length` → ❌ (навмисна помилка)
      - `test_invalid_object` → ✅

5. **PyTest**
    ```python
    def test_app_triangle():
        fig = "triangle"
        triangle = Figure(fig, 4)
        assert triangle.get_figure_type == fig
        assert triangle.get_figure_length == 4
    ```
    - Запуск:
      ```bash
      python -m pytest --cov=app -v test_app.py
      ```
      - 1 тест пройшов ✅
    - Детальний вивід та HTML-звіт згенеровано

6. **Coverage та HTML-звіт**
    - Додана нова проперті `get_angles`:
      ```python
      @property
      def get_angles(self):
          if self.figure_type in ["square", "rectangle"]:
              return 4
          if self.figure_type == "triangle":
              return 3
      ```
    - Тести для `get_angles`:
      ```python
      def test_get_angles_triangle():
          fig = "triangle"
          triangle = Figure(fig, 1)
          assert triangle.get_angles == 3

      def test_get_angles_square():
          fig = "square"
          square = Figure(fig, 2)
          assert square.get_angles == 4
      ```
    - Покриття коду:
      ```bash
      python -m pytest --cov=app --cov-report term-missing --cov-report html -v
      ```
    - HTML-звіт у `htmlcov/index.html` ✅
    - Створено `.coveragerc` для обмеження файлів:
      ```
      [run]
      source = app.py

      [report]
      omit =
          */__init__.py
          */tests/*
          */venv/*
      ```

---
# Скріншоти
![alt text]({E2B17F81-B89B-4C5C-A157-79E391763C0A}.png)
![alt text]({6C5C6EF3-AA22-4DCD-BEA0-1364C70CB810}.png)
![ - 2 завдання]({4074A913-EEF7-45DF-B490-7C98D9FFE0A7}.png)

![alt text]({13021956-D77A-4656-8E9B-A4D2FF599851}.png)
![alt text]({4D1E1A24-DD31-4977-A8F6-0A4692D1E5A9}.png)
### Висновок:

1. **Що було виконано в роботі**
- Перевірка правильності введених даних через assert.  
- Створено класи з валідацією через assert та ValueError.  
- Реалізовано юніт-тести через unittest та PyTest.  
- Проведено збір статистики покриття коду за допомогою coverage.  
- Генерація HTML-звіту для візуалізації покриття коду.  

2. **Чи досягнуто мети роботи**
- Мета досягнута: навчитись тестувати Python-код, використовувати assert, unittest, PyTest та збирати покриття коду.  

3. **Нові знання, отримані під час роботи**
- Застосування assert для перевірки даних.  
- Створення класів із валідацією.  
- Написання юніт-тестів та їх запуск через unittest і PyTest.  
- Використання coverage та генерація HTML-звітів.  

4. **Чи вдалося відповісти на всі поставлені питання**
- Так, всі питання щодо тестування та покриття коду були опрацьовані.  

5. **Чи виконані всі завдання**
- Так, усі завдання з assert, OOP, unittest, PyTest та coverage виконані успішно.  

6. **Чи виникали труднощі під час виконання завдання**
- Спершу були труднощі з викликом pytest у Windows, але вони були вирішені через використання `python -m pytest`.  

7. **Чи подобається формат виконання роботи (Feedback)**
- Так, поетапне виконання прикладів та використання тестів і coverage є зручним та наочним.  

8. **Побажання щодо покращення (Suggestions)**
- Додати більше прикладів розгалужень у класах та тестах.  
- Додати вправи на покриття коду при різних сценаріях OOP.  
- Включити приклади генерації HTML-звітів безпосередньо з Jupyter Notebook.
