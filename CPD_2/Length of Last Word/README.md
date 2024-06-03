# Задание

Учитывая строку, s состоящую из слов и пробелов, верните длину последнего слова в строке.

Слово - это максимальное подстрока состоит только из символов, не содержащих пробелов.

# Результат работы

# Листинг

``` rs
impl Solution {
    pub fn length_of_last_word(s: String) -> i32 {
        let words = s.trim().split(' ').collect::<Vec<_>>();

        if words.is_empty() {
            return 0;
        }

        words.last().unwrap().len() as i32
    }
}
```