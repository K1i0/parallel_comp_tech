#include <mpi.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

#define NUM_RUN 10
#define ROOT_RANK 0
#define RECV_RANK 1
#define MB 1024 * 1024

//arg[1] == size
int main (int argc, char *argv[])
{
    if (argc < 2) {
        return -1;
    }

    int size = atoi(argv[1]);
    int commsize, rank;

    double tsend = 0.0;
    double trecv = 0.0;

    double total_time; //total process operations time

    MPI_Init (&argc, &argv);
    MPI_Comm_size (MPI_COMM_WORLD, &commsize);
    MPI_Comm_rank (MPI_COMM_WORLD, &rank);

    int count = MB * size;
    uint8_t *buffer = (uint8_t*)calloc(count, sizeof(uint8_t));

    MPI_Request req;

    for(int i = 0; i < NUM_RUN; i++) {
        if (rank == ROOT_RANK) {
            tsend = MPI_Wtime();
            MPI_Isend(buffer, count, MPI_UINT8_T, 1, 0, MPI_COMM_WORLD, &req);
            tsend = (MPI_Wtime() - tsend);
            printf("----->>>%d - %d  Время отправки: %.10f\n", i, rank, tsend);
            total_time += tsend;
        } else if (rank == RECV_RANK) {
            trecv = MPI_Wtime();
            MPI_Irecv(buffer, count, MPI_UINT8_T, 0, 0, MPI_COMM_WORLD, &req);
            trecv = (MPI_Wtime() - trecv);
            printf("%d - %d  Время получения: %.10f<<<------\n", i, rank, trecv);
            total_time += trecv;
        }
        MPI_Waitall(1, &req, MPI_STATUS_IGNORE);
    }

    double global_time = 0.0; //global all processes operations time
    MPI_Reduce(&total_time, &global_time, 1, MPI_DOUBLE, MPI_SUM, ROOT_RANK, MPI_COMM_WORLD);
    if (rank == ROOT_RANK) {
        printf("Общее время (send/recv): %.10f (кол-во передач: %d)\n", global_time, NUM_RUN);
        printf("Среднее время выполнения операции обмена (send+recv): %.10f\n", global_time / NUM_RUN);
    }

    free(buffer);
    MPI_Finalize();
    return 0;
}