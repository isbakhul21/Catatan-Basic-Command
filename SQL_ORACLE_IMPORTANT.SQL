Ketika menggunakan filter DATE, harus menggunnakan DATE 'YYYY-MM-DD'  , 
HAL INI KARENA TIPE DATA DATE INI BERBEDA BEDA TERGANTUNG LOCAL SERVERNYA
CONTOH SALAH SELECT * FROM EMPLOYEE WHERE BITHDATE < '01-01-2021'
CONTOH BENAR SELECT * FROM EMPLOYEE WHERE BITHDATE < DATE '01-01-2021'

Penggunaan Order by itu artinya memprioritaskan yang paling kiri
misal 
SELECT * FROM EMPLOYEE ORDER BY DEPARTMENT_ID, SALARY
artinya department_id nya dulu yang diurutkan, kemudian baru salary,
its mean jika ada departmen_id yang sama akan diurutkan oleh salary nya
