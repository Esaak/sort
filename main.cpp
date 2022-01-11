#include <iostream>
#include <chrono>
#include <fstream>
#include <chrono>
#include <random>
#include <algorithm>
#include <iomanip>
const int  MAX_MASS =  15000;
const int  MAX = 1000;
const int MIN = 0;
const int Nmal = 5;
const int MIN_MASS = 10000;


int rand_uns(int min, int max) {
    unsigned seed = std::chrono::steady_clock::now().time_since_epoch().count();
    static std::default_random_engine e(seed);
    std::uniform_int_distribution<int> d(min, max);
    return d(e);
}
double get_time() {
    return std::chrono::duration_cast<std::chrono::microseconds>
                   (std::chrono::steady_clock::now().time_since_epoch()).count()/1e6;
}
using namespace std;
double sort_bubble(int *arr, int N){
    double time_begin = get_time();
    for(int i=0; i<N-1; i++){
        for(int j=0; j<N-1; j++){
            if(arr[j+1]<arr[j]){
                int tmp = arr[j];
                arr[j]=arr[j+1];
                arr[j+1]=tmp;
            }
        }
    }
    double time_end = get_time();
    double work_time = time_end-time_begin;
    return work_time;
}
double sort_insertion(int *arr, int N){
    double time_begin = get_time();
    for(int i=1; i < N; i++) {
//for(int j=i;j>0 && arr[j-1]>arr[j];j--)
        for (int j = i; j >= 0; j--) {
            if (arr[j - 1] > arr[j])                // пока j>0 и элемент j-1 > j, x-массив int
                swap(arr[j - 1], arr[j]);
        }
    }
    double time_end = get_time();
    double work_time = time_end-time_begin;
    return work_time;
}
double sort_quick(int *mas, int size) {
    double time_begin = get_time();
    int i = 0;
    int j = size - 1;
    double mid = mas[size / 2];
    do{
        while(mas[i] < mid) {
            i++;
        }
        while(mas[j] > mid) {
            j--;
        }
        if (i <= j) {
            int tmp = mas[i];
            mas[i] = mas[j];
            mas[j] = tmp;

            i++;
            j--;
        }
    } while (i <= j);
    if(j > 0) {
        //"Левый кусок"
        sort_quick(mas, j + 1);
    }
    if (i < size) {
        //"Првый кусок"
        sort_quick(&mas[i], size - i);
    }
    double time_end = get_time();
    double work_time = time_end-time_begin;
    return work_time;
}
void merge(int *arr, int low, int high, int mid)
{
    int i, j, k, c[15000];
    i = low;
    k = low;
    j = mid + 1;
    while (i <= mid && j <= high) {
        if (arr[i] < arr[j]) {
            c[k] = arr[i];
            k++;
            i++;
        }
        else  {
            c[k] = arr[j];
            k++;
            j++;
        }
    }
    while (i <= mid) {
        c[k] = arr[i];
        k++;
        i++;
    }
    while (j <= high) {
        c[k] = arr[j];
        k++;
        j++;
    }
    for (i = low; i < k; i++)  {
        arr[i] = c[i];
    }
}
double sort_merge(int *arr, int low, int high){
    double time_begin = get_time();
    int mid;
    if (low < high){
        //divide the array at mid and sort independently using merge sort
        mid=(low+high)/2;
        sort_merge(arr,low,mid);
        sort_merge(arr,mid+1,high);
        //merge or conquer sorted arrays
        merge(arr,low,high,mid);
    }
    double time_end = get_time();
    double work_time = time_end-time_begin;
    return work_time;
}
void heapify(int *arr, int n, int i)
{
    int largest = i;
// Инициализируем наибольший элемент как корень
    int l = 2*i + 1; // левый = 2*i + 1
    int r = 2*i + 2; // правый = 2*i + 2

    // Если левый дочерний элемент больше корня
    if (l < n && arr[l] > arr[largest])
        largest = l;

    // Если правый дочерний элемент больше, чем самый большой элемент на данный момент
    if (r < n && arr[r] > arr[largest])
        largest = r;

    // Если самый большой элемент не корень
    if (largest != i)
    {
        swap(arr[i], arr[largest]);

// Рекурсивно преобразуем в двоичную кучу затронутое поддерево
        heapify(arr, n, largest);
    }
}

double sort_heap(int *arr, int size){
    double time_begin = get_time();
    // Построение кучи (перегруппируем массив)
    for (int i = size / 2 - 1; i >= 0; i--)
        heapify(arr, size, i);

    // Один за другим извлекаем элементы из кучи
    for (int i=size-1; i>=0; i--)
    {
        // Перемещаем текущий корень в конец
        swap(arr[0], arr[i]);

        // вызываем процедуру heapify на уменьшенной куче
        heapify(arr, i, 0);
    }
    double time_end = get_time();
    double work_time = time_end-time_begin;
    return work_time;

}

double sort_selection(int *arr, int N){
    double time_begin = get_time();
    for(int i=0; i<N-1; ++i){
        int minn=i;
        for(int j=i+1; j<N; j++){
            if(arr[j]<arr[i])
                minn=j;
        }
        swap(arr[i],arr[minn]);
    }
    double time_end = get_time();
    double work_time = time_end-time_begin;
    return work_time;
}
int main() {
    ofstream f ("O01_sort_merge.txt");
    int arr[MAX_MASS];
    double num[Nmal];
    double summ=0;
    f << fixed << setprecision(10);
    for(int j=MIN_MASS; j<MAX_MASS; j+=20){
        for(int n=0; n<Nmal; n++){
            for(int i=0; i<j; i++){ //заполнение массива
                arr[i]=rand_uns(MIN,MAX);
            }
            //num[n] = sort_bubble(arr, j); //сортировка пузырьком
            //num[n]=sort_insertion(arr, j);//сортировка вставками
            //num[n]=sort_selection(arr, j);//сортировка выбором
            num[n]=sort_quick(arr, j);//быстрая сортировка
            //num[n]=sort_merge(arr, 0, j);//сортировка слиянием
            //num[n]=sort_heap(arr,j);//сортировка кучей

        }
        summ=0;
        for(int i=0; i<Nmal; i++){ //нахождение средне арифметичексого
            summ+=num[i];
        }
        double time = summ/Nmal;
        f<<endl;
        f<<time<<"; "<<j<<endl;
    }
    f.close();
    return 0;
}
