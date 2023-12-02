# Day 2

# Part 1

games ← •file.Lines "./input.txt" 
ParseGame ← {';'((⊢-˜¬×+`)∘=⊔⊢) {2 + > 𝕩 ⊐ ':'} ⊸ ↓ 𝕩}
ParseTurn ← {' '((¬-˜⊢×·+`»⊸>)∘≠⊔⊢)¨ ','((⊢-˜¬×+`)∘=⊔⊢) 𝕩}
TurnArray ← {⟨0, 0, 0⟩{(•ParseFloat ⊑𝕨) ⌾ ((⊑"rgb"⊐⊑1⊑𝕨)⊸⊑)𝕩}´ 𝕩}
games_array ← ((TurnArray∘ParseTurn)¨ ParseGame)¨ games
+´ 1 + / (∧´⟨12, 13, 14⟩≥⌈´)¨games_array # This is the result of part 1

# Part 2

+´(×´⌈´)¨games_array # This is the result of part 2
