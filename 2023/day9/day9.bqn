lines ← •file.Lines "./input.txt"
histories ← ' '{•ParseFloat¨ 𝕨⊸≠¨⊸/¨ (+` 𝕨⊸= 𝕩 ) ⊔ 𝕩}¨ lines

# Part 1
Triangle ← {
  ((¯1↓𝕩)∾¯1⊑¯1⊑𝕩)∾⟨(1⊸↓-¯1⊸↓) ¯1⊑𝕩⟩
}
•Show +´ (+´ ¯1↓ Triangle •_while_ {∨´ 0≠ ¯1⊑𝕩}∘(0⊸∾)∘<)¨ histories

# Part 2

OtherTriangle ← {
  ((¯1↓𝕩)∾⊑¯1⊑𝕩)∾⟨(1⊸↓-¯1⊸↓) ¯1⊑𝕩⟩
}
•Show ¯1× +´ (-´ ¯1↓ OtherTriangle •_while_ {∨´ 0≠ ¯1⊑𝕩}∘(0⊸∾)∘<)¨ histories
