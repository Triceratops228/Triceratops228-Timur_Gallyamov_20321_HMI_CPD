# Задание

Напишите функцию для поиска самой длинной строки общего префикса среди массива строк.

Если общего префикса нет, верните пустую строку "".

# Результат работы

# Листинг

``` rs
impl Solution {
    pub fn longest_common_prefix(strs: Vec<String>) -> String {
        if strs.is_empty() {
            return String::new();
        }

        let mut pre = strs[0].clone();

        for s in strs.iter().skip(1) {
            while !s.starts_with(&pre) {
                pre.pop();
            }
        }

        pre
    }
}
```