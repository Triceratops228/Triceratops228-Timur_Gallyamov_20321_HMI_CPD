# Задание

Вам будет предоставлен массив целых чисел height длины n. Здесь n нарисованы вертикальные линии таким образом, что двумя конечными точками ith линии являются (i, 0) и (i, height[i]).

Найдите две линии, которые вместе с осью x образуют контейнер таким образом, чтобы в контейнере было наибольшее количество воды.

Возвращайте максимальное количество воды, которое может вместить емкость.

Обратите внимание, что нельзя наклонять емкость.

# Результат работы

# Листинг

``` rs
impl Solution {
    pub fn max_area(height: Vec<i32>) -> i32 {
            let mut left = 0;
    let mut right = height.len() - 1;
    let mut max_area = 0;

    while left < right {
        let current_area = height[left].min(height[right]) * (right as i32 -    left as i32);
        max_area = max_area.max(current_area);

        if height[left] < height[right] {
            left += 1;
        } else {
            right -= 1;
        }
    }

    max_area
    }
}
```