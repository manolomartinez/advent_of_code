# Part 1

races ←  •ParseFloat¨¨ 1↓¨ ' '((¬-˜⊢×·+`»⊸>)∘≠⊔⊢)¨ •file.Lines "./input.txt" 
Options ← ⌽⊸× 1+↕∘-⟜1
•Show ×´ +´¨ (Options¨∘⊑ >¨ 1⊸⊑) races

# Part 2

⟨time, distance⟩ ←  •ParseFloat¨ ∾´¨ 1↓¨ ' '((¬-˜⊢×·+`»⊸>)∘≠⊔⊢)¨ •file.Lines "./input.txt" 

Lowest ← {(𝕨 - √(𝕨⋆2) - 4×𝕩) ÷ 2}
Highest ← {(𝕨 + √(𝕨⋆2) - 4×𝕩) ÷ 2}

1 + (⌊time Highest distance) - ⌈time Lowest distance 
