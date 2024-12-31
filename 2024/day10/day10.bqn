Split ⇐ {𝕨((⊢-˜+`×¬)∘=⊔⊢)𝕩}
ToNat ⇐ {(10⊸×⊸+˜´∘⌽-⟜'0')𝕩}

Inside ← {
  (∧´ 𝕩 ≥ 0) ∧ (∧´ 𝕩 ≤ (≢map) - 1)
}

Contiguous ← {
  Inside¨⊸/ 𝕩⊸+¨ ⟨⟨1, 0⟩, ⟨0, 1⟩, ⟨¯1, 0⟩, ⟨0, ¯1⟩⟩
}

map ← -1 × >'0'- •file.Lines "./input.txt" 

# Part 1
zeros ← /○⥊⟜(↕≢) map = 0
Step ← {
  ⍷∾´𝕨{((𝕨+1) = map ⊑˜ Contiguous 𝕩) / Contiguous 𝕩}¨𝕩}
FullStep ← {
  ⟨1+⊑𝕩,Step´𝕩⟩}

+´≠¨(1⊸⊑FullStep⍟9)¨ (0⋈{⟨𝕩⟩})¨zeros # Solution to part 1

# Part 2
Step2 ← {
  𝕨{((𝕨+1) = map ⊑˜ Contiguous 𝕩) / Contiguous 𝕩}¨𝕩}

FullStep2 ← {
  height‿ratings‿cells ← 𝕩
  unique ← ⍷∾´new_cells ← height Step2 cells
  new_ratings ← ⥊+´˘(∨´⎊0)¨˘ratings (×⎉1) unique≡⚇1⌜new_cells
  ⟨1+height, new_ratings, unique⟩}

+´+´¨ 1⊸⊑¨ (FullStep2⍟9)¨ (0∾⟨1⟩⋈{⟨𝕩⟩})¨zeros # Solution to part 2
