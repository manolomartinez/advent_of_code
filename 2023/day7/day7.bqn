# Part 1
hands ← > •ParseFloat⌾(1⊸⊑)¨ ' '((¬-˜⊢×·+`»⊸>)∘≠⊔⊢)¨ •file.Lines "./input.txt" 
types ← ⟨⟨5⟩, ⟨1, 4⟩, ⟨2, 3⟩, ⟨1, 1, 3⟩, ⟨1, 2, 2⟩, ⟨1, 1, 1, 2⟩, ⟨1, 1, 1, 1, 1⟩⟩
strenghts ← "AKQJT98765432"
types_in_hands ← (∧/⁼∘⊐)¨ ⊏˘hands
•Show +´ (-⟜↕ ≠⊏˘hands) × 1⊏˘hands ⊏˜ ((⊏˘hands)⊸⊐) ∾´ ((⍋ strenghts⊸⊐¨)⊸⊏)¨ {(𝕩⊸≡¨ types_in_hands) / ⊏˘hands}¨types

# Part 2

strenghts ↩ "AKQT98765432J"

AddJ ← {
  ⟨⟩: ⟨5⟩;
  (5 - +´𝕩)⊸+ ⌾ (¯1⊸⊑) 𝕩
}

types_in_hands ↩ AddJ¨ (∧/⁼∘⊐)¨ ('J'⊸≠)⊸/¨ (⊏˘hands)
•Show +´ (-⟜↕ ≠⊏˘hands) × 1⊏˘hands ⊏˜ ((⊏˘hands)⊸⊐) ∾´ ((⍋ strenghts⊸⊐¨)⊸⊏)¨ {(𝕩⊸≡¨ types_in_hands) / ⊏˘hands}¨types
