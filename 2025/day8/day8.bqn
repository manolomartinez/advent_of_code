a ← •Import "../../../Project Euler/aux.bqn"
junctions ← a.StrToNat¨¨ ','⊸a.Split¨ •FLines "./test.txt" 
pairs ← ⍷ ∧¨ 2 a.Permutations ≠junctions
(+´∘⋆⟜2-´) ⟨1‿2‿3, 4‿5‿6⟩
#⍋(+´∘⋆⟜2-´)¨pairs ⊏¨ <junctions
(<junctions) ⊏˜¨ pairs ⊏˜ ⍋(+´∘⋆⟜2-´)¨pairs ⊏¨ <junctions
(+´⋆⟜2 ⊣-⊢)⌜˜ junctions
