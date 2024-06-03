# Задание

Вам предоставляется n x n 2Dmatrix-изображение, поверните изображение на 90 градусов (по часовой стрелке).

Вы должны поворачивать изображение на месте, что означает, что вы должны изменять входную 2D-матрицу напрямую. НЕ выделяйте другую 2D-матрицу и выполняйте поворот.

# Результат работы

# Листинг

``` rs
impl Solution {
    pub fn rotate(matrix: &mut Vec<Vec<i32>>) {
        let n = matrix.len();
        let mut matrix3 = vec![vec![0; n]; n];

        for j in 0..n {
            let mut matrix2 = vec![];
            for row in matrix.iter() {
                matrix2.push(row[j]);
            }
            matrix2.reverse();
            matrix3[j] = matrix2;
        }

        *matrix = matrix3;
    }
}
```