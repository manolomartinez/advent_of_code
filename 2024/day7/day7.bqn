Split ⇐ {𝕨((⊢-˜+`×¬)∘=⊔⊢)𝕩}
ToNat ⇐ {(10⊸×⊸+˜´∘⌽-⟜'0')𝕩}

equations ← (ToNat¨ ' ' Split {':'≠𝕩}⊸/)¨ •file.Lines "./input.txt" 

Op ← {
  ⟨(⊑𝕨) (1⊑𝕨)◶+‿× ⊑𝕩, 1⊑𝕩⟩
}

Operate ← { 
 # 𝕨 is the vector of operations
 # 𝕩 is the vector of operands
 ⊑Op´ ⌽<˘⍉>𝕩‿(0∾𝕨)
}

BruteForce ← {
  target ← ⊑𝕩
  operands ← 1↓𝕩
  operations ← ¯1 + ≠operands
  sequences ← ∘‿1 ⥊ 0‿1(∾⌜˜)⍟(operations - 1) 0‿1 # permutations
  ∨´⥊target = operands⊸(Operate˜)¨ sequences
}

+´ ⊑¨ BruteForce¨⊸/ equations # Solution to Part 1

# Part 2

Concat ← {
  𝕨 + 𝕩 × 10 ⋆ ⌊1+•math.Log10 1⌈| 𝕨
}

Op2 ← {
  ⟨(⊑𝕨) (1⊑𝕨)◶+‿×‿Concat ⊑𝕩, 1⊑𝕩⟩
}

Operate2 ← { 
 # 𝕨 is the vector of operations
 # 𝕩 is the vector of operands
 ⊑Op2´ ⌽<˘⍉>𝕩‿(0∾𝕨)
}

BruteForce2 ← {
  target ← ⊑𝕩
  operands ← 1↓𝕩
  #•Show operands
  operations ← ¯1 + ≠operands
  sequences ← ∘‿1 ⥊ 0‿1‿2(∾⌜˜)⍟(operations - 1) 0‿1‿2 # permutations
  #•Show sequences
  ∨´⥊target = operands⊸(Operate2˜)¨ sequences
}

+´ ⊑¨ BruteForce2¨⊸/ equations # Solution to Part 2
