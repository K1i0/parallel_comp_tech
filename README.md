# Параллельные вычислительные технологии
> Используемые функции MPI

| Функция | Аргументы |
| ------ | ------ |
| MPI_Init() | |
| MPI_Commsize() |  |
| MPI_Comm_rank() |  |
| MPI_Isend(const void *buf, int count, MPI_Datatype datatype, int dest, int tag, MPI_Comm comm, MPI_Request *request) | buf - начальный адрес буфера, count - количество элементов в буфере, datatype - тип данных в буфере, dest - ранг получателя, tag - тэг сообщения, comm - коммуникатор, в котором выполняется обмен, request - запрос, необходимый для отслеживания состояния обмена  |
| MPI_Irecv() |  |
| MPI_Waitall() |  |

> [Документация MPI](https://curc.readthedocs.io/en/latest/programming/MPI-C.html)
> Больше информации об интерфейсе передачи сообщений.

## Оформление результатов выполнения работы
> Для оформления результатов работы (построения графиков) используется библиотека [Matplotlib](https://matplotlib.org/stable/)

### Пример построенного графика
![Пример графика](/doc/exchange_time/result.png)
### Установка
```sh
pip install matplotlib
```