reports ← •file.Lines "./input.txt" 
Split ⇐ {((¯1+⊢×·+`»⊸<)¬𝕩=𝕨)⊔𝕩}
parsed ← {⍉{+´(10⊸⋆⌽∘↕∘≠)⊸×-⟜'0'𝕩}¨' 'Split 𝕩}¨ reports
# Part 1
Monotonous ← ((¯1 + ≠)≡{|+´×1(↓--⊸↓)𝕩})
Limits ← ∧´∘(1⊸≤∧3⊸≥)∘|1⊸(↓--⊸↓)
safe ← +´(Monotonous¨∧Limits¨) parsed # Solution to part 1

# Part 2

# This is just brute force

dampened ← {∨´(Monotonous¨∧Limits¨)(<˘¬=⌜˜↕≠𝕩) /¨ <𝕩}¨parsed
not_dampened ← (Monotonous¨∧Limits¨) parsed # Solution to part 1
+´ dampened ∨ not_dampened # Solution to part 2
