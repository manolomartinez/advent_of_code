wordsearch ← (⊢↑˝·≍⟜¬2+≢)⍟3 > •file.Lines "./input.txt"  # padded
# Solution to part 1
+ ´ wordsearch⊸{+´ "XMAS"⊸≡¨((((3⥊⟨𝕩⟩)⊸(+`˜))⊸(∾˜))¨ <¨/○⥊⟜(↕≢) 'X' = 𝕨)⊑𝕨}¨⟨1‿0, ¯1‿0, 0‿1, 0‿¯1, 1‿1, 1‿¯1, ¯1‿1, ¯1‿¯1⟩

# Solution to Part 2
+´ {∧´∨´˘ 𝕩 ≡⌜ ⟨"SAM", "MAS"⟩}¨ wordsearch⊸{(𝕩⊸+¨¨ ⟨⟨1‿1, 0‿0, ¯1‿¯1⟩, ⟨¯1‿1, 0‿0, 1‿¯1⟩⟩) ⊑ 𝕨}˜¨ { /○⥊⟜(↕≢) 'A' = 𝕩}wordsearch

