use std::collections::HashSet;
impl Solution {
    pub fn remove_duplicates(nums: &mut Vec<i32>) -> i32 {
        let mut unique_nums = HashSet::new();
        let mut i = 0;

        while i < nums.len() {
            if !unique_nums.contains(&nums[i]) {
                unique_nums.insert(nums[i]);
                i += 1;
            } else {
                nums.remove(i);
            }
        }

        nums.len() as i32
    }
}