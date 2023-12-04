# Day 2

# Part 1

games ← •file.Lines "./input.txt" 
ParseList ← {•ParseFloat¨ ' '((¬-˜⊢×·+`»⊸>)∘≠⊔⊢) 𝕩}
ParseGame ← {ParseList¨ '|'((⊢-˜¬×+`)∘=⊔⊢) {2 + > 𝕩 ⊐ ':'} ⊸ ↓ 𝕩}
parsed_games ← ParseGame¨ games
matches ← +´¨ {(1⊑𝕩) ∊ ⊑𝕩}¨ parsed_games
•Show +´ {(2⋆ 1-˜𝕩) × 𝕩 > 0}matches

# Part 2

copies ← 192 ⥊<1
NewCopies ← {{(𝕩⊑copies)⊸+¨⌾((𝕩⊑matches)↑(1+𝕩)↓⊢)copies}𝕩}
{copies ↩ NewCopies 𝕩}¨↕192
•Show +´ copies
