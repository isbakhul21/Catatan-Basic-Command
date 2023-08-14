Ketika menggunakan filter DATE, harus menggunnakan DATE 'YYYY-MM-DD'  , 
HAL INI KARENA TIPE DATA DATE INI BERBEDA BEDA TERGANTUNG LOCAL SERVERNYA
CONTOH SALAH SELECT * FROM EMPLOYEE WHERE BITHDATE < '01-01-2021'
CONTOH BENAR SELECT * FROM EMPLOYEE WHERE BITHDATE < DATE '01-01-2021'

Penggunaan Order by itu artinya memprioritaskan yang paling kiri
misal 
SELECT * FROM EMPLOYEE ORDER BY DEPARTMENT_ID, SALARY
artinya department_id nya dulu yang diurutkan, kemudian baru salary,
its mean jika ada departmen_id yang sama akan diurutkan oleh salary nya


CONTOH PENGGUNAAN ROWNUMBER, RANK, DENSE_RANK
COBA LIHAT PERBEDAANYA

SELECT PRODUCT_NAME,
    PRICE,
    ROW_NUMBER() OVER (ORDER BY PRICE DESC) AS ROW_NUMBER,
    RANK() OVER (ORDER BY PRICE DESC ) AS RANK,
    DENSE_RANK() OVER (ORDER BY PRICE DESC) AS DENSE_RANK
FROM PRODUCTS
ORDER BY PRICE DESC;

PRODUCT_NAME     PRICE   ROW_NUMBER   RANK   DENSE_RANK
Insulin	         25	      1	          1	     1
Penicillin	     10	      2	          2	     2
Amoxicillin	     8	      3	          3	     3
Acetaminophen	   5	      4	          4	     4
Aspirin	         5	      5	          4	     4
WATER	           1	      6	          6	     5

JIKA RANGKINGNYA 1 2 3 TIDAK ADA MASALAH, TETAPI JIKA RANGKINGNYA 1-4 ATAU 1-5 BISA JADI BERBEDA.

