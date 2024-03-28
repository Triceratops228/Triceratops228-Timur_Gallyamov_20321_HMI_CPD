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