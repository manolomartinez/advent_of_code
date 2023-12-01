# Day 1

# Part 1
10⊸>⊸/ # Takes numbers from a string made of number chars and other characters
(10⊸×∘⊑+¯1⊸⊑) #  multiply first one by ten and last

+´ (10⊸×∘⊑+¯1⊸⊑)¨ (10⊸>⊸/)¨ '0' -˜ •file.Lines "./input.txt" # This is the result of part 1
# Part 2

num_strings ← ⟨"one"‿'1', "two"‿'2', "three"‿'3', "four"‿'4', "five"‿'5', "six"‿'6', "seven"‿'7', "eight"‿'8', "nine"‿'9'⟩
test ← "9sixsevenz3"
+´ {(10⊸×∘⊑+¯1⊸⊑) 10⊸>⊸/ ⌊´ '0' -˜ 𝕩⊸({(¯1⊑𝕨)¨⌾(((⊑𝕨) (≢∘⊢↑⍷) 𝕩)⊸/)𝕩}˜)¨num_strings}¨ •file.Lines "./input.txt" # This is the result of part 1
