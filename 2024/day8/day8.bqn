map ← >•file.Lines "./input.txt"
types ←  '.'⊸≠⊸/ {1⊸< +´¨ ⥊¨ map⊸=¨ 𝕩}⊸/ ∊⊸/⥊map

# Part 1

Antinodes ← {
  ⟨(2×𝕨) - 𝕩, (2×𝕩) - 𝕨⟩
}

Inside ← {
  (∧´ 𝕩 ≥ 0) ∧ (∧´ 𝕩 ≤ (≢map) - 1)
}

# Solution to part 1
≠ Inside¨⊸/ ∊⊸/ ∾´⍟2 {Antinodes´¨ ≢´¨⊸/ ⥊(<˘)¨ ≍⌜˜ 𝕩}¨ {/○⥊⟜(↕≢) map = 𝕩}¨ types

# Part 2

Antinodes2 ← {
  distance ← 𝕩-𝕨
  maxima ← ⌈´⌊|50 ÷ distance
  Inside¨⊸/ ∊⊸/ ((𝕩⊸-¨)∾(𝕩⊸+¨)) distance⊸×¨ ↕maxima
}

≠ ∊⊸/ ∾´⍟2 {Antinodes2´¨ ≢´¨⊸/ ⥊(<˘)¨ ≍⌜˜ 𝕩}¨ {/○⥊⟜(↕≢) map = 𝕩}¨ types
