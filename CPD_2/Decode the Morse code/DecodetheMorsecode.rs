mod preloaded;
use preloaded::MORSE_CODE;
// MORSE_CODE is `HashMap<String, String>`. e.g. ".-" -> "A".

fn decode_morse(encoded: &str) -> String {
    let words: Vec<&str> = encoded.trim().split("   ").collect();
    let mut complete_word = String::new();

    for word in words {
        let letters: Vec<&str> = word.split(" ").collect();
        let mut decoded_word = String::new();

        for letter in letters {
            if let Some(char_value) = MORSE_CODE.get(letter) {
                decoded_word.push_str(char_value);
            }
        }

        complete_word.push_str(&decoded_word);
        complete_word.push(' ');
    }

    complete_word.trim().to_string()
}