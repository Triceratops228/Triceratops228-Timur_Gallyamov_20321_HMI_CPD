impl Solution {
    pub fn length_of_last_word(s: String) -> i32 {
        let words = s.trim().split(' ').collect::<Vec<_>>();

        if words.is_empty() {
            return 0;
        }

        words.last().unwrap().len() as i32
    }
}