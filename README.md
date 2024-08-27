# Algoritms_LessonOD02
 Стеки и очереди. Деревья и графы

✅ Стек (Stack) — это структура данных, работающая по принципу "последний пришел, первый ушел" (Last In, First Out, LIFO).

Стеки можно сравнить со стопкой тарелок: мы кладем тарелку наверх, и когда начинаем разбирать стопку, первая уходит верхняя тарелка. Примеры использования стеков на компьютере включают отмену действий (Ctrl-Z), когда последнее действие оказывается наверху стека.


Основные операции со стеком:

push — добавление элемента в стек,
pop — удаление верхнего элемента,
peek — получение верхнего элемента без удаления,
is_empty — проверка, пуст ли стек.

✅ Очередь (Queue) — это структура данных, работающая по принципу "первый пришел — первый ушел" (First In, First Out).

Это похоже на очереди в обычной жизни, например, в магазине: первый, кто стоял в очереди, обслуживается первым и уходит первым.


Очереди используются в системах с множеством задач, где необходимо обрабатывать их в порядке поступления. Примером может быть принтер: документы печатаются в порядке их поступления. Также очереди часто используются для обработки событий в играх или приложениях: пользователь совершает действия, которые программа обрабатывает в порядке поступления.

Для работы с очередями существуют три основные операции:

добавление элемента в конец очереди;
удаление элемента из начала очереди;
проверка на пустоту очереди.
Очереди также создаются на основе списков.

✅ Очередь (Queue) — это структура данных, работающая по принципу "первый пришел — первый ушел" (First In, First Out).

Корневой узел называется root node, его потомки — дети, и они также могут быть родителями для других узлов.


Деревья могут использоваться в файловых системах, где файлы и папки на компьютере организованы как дерево. Например, у нас есть корневая папка, внутри которой находятся другие файлы и папки, которые также могут содержать файлы и папки.

Деревья также часто используются для поиска и сортировки. Существует такое понятие как бинарное дерево поиска, которое помогает быстро находить данные, например, в базах данных или поисковых системах.

✅ Бинарное дерево — это вид дерева, в котором каждый узел имеет не более двух потомков.

В этом уроке мы будем писать код для реализации бинарного дерева поиска. У этой структуры есть свой специфика.

Представим, что мы создаем корневой узел с числом 45.

Помня, что у бинарного дерева не может быть больше двух потомков, создадим два потомка для этого числа: левую и правую ветку. Значение левого потомка всегда меньше родительского узла, а правого — больше.

Таким образом, если мы хотим добавить в дерево значение “30”, оно станет левой ветвью, так как это значение меньше, чем 45.

Если же мы хотим добавить значение “56”, оно будет добавлено в правую ветвь, так как 56 больше, чем 45.

Представим, что теперь мы хотим добавить в дерево значение “20”. Оно меньше, чем 45 и меньше, чем 30. Таким образом, мы отправляем это значение в левую сторону.

Теперь добавим число 35. Оно меньше, чем 45, но больше, чем 30: значит, оно добавится в правую ветку от числа 30.

Таким же образом число 50 встанет левее числа 56.

Число 73 следует разместить справа от числа 56.

✅ Граф — это структура данных, состоящая из множества узлов, то есть вершин, и множества рёбер, которые соединяют пары узлов.

Графы похожи на карту дорог: у нас есть города, которые представляют собой узлы, точки, вершины, а дороги между ними — это рёбра.


Графы часто применяются в навигации, например, GPS-системы используют графы для поиска кратчайших путей между двумя точками.

Также графы применяются в социальных сетях. Например, в социальной сети ВКонтакте пользователи — это узлы, а их дружеские связи — это рёбра.

Помимо этого, графы часто используются для оптимизации путей передачи данных между серверами и для анализа маршрутов в интернете с использованием различных алгоритмов.
