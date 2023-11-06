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

### Компиляция и запуск
```sh
mpicc -o main ./src/exchange_time/extime.c
```

> Более подробное описание параметров MPI можно посмотреть [туть](https://www.open-mpi.org/doc/v4.1/man1/mpiexec.1.php) или [вот туть](https://docs.open-mpi.org/en/v5.0.x/man-openmpi/man1/mpirun.1.html#label-schizo-ompi-map-by)

| Параметр | Описание |
| ------ | ------ |
| --report-bindings | Визуализация привязок процессов (к узлам, сокетам, ядрам) |
| -np | Регулировка количества запущенных процессов |
| sinfo | Просмотр информации о кластере |
| -host | Выбор узлов, на которых запускается программа |
| --map-by | Выбор способа привязкип процессов (к ядрам, сокетам) |
| squeue | Просмотр очереди задач на кластере |

>  Запуск на кластере (на уровне оперативной памяти, межпроцессорной шины, сетевом), где size - размер передаваемого сообщения в МБ


```sh
mpiexec --report-bindings -np 2 -host oak-cn3.ipa.csc.sibsutis.ru:2 --map-by core ./main <size>
mpiexec --report-bindings -np 2 -host oak-cn3.ipa.csc.sibsutis.ru:2 --map-by socket ./main <size>
mpiexec --report-bindings -np 2 -host oak.cnl.ipa.csc.sibsutis.ru,oak-cn3.ipa.csc.sibsutis.ru ./main <size>
```