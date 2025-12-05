a ← •Import "../../../Project Euler/aux.bqn"
t ← •file.Lines "./input.txt"
ranges ← ∧ a.StrToNat¨¨ '-'⊸a.Split¨ (>'-'⊸∊¨)⊸/t
ingredients ← a.StrToNat¨ 1↓ (¬∘>'-'⊸∊¨)⊸/t
•Show +´∨´˘ ingredients {((⊑𝕩)⊸≤∧(1⊑𝕩)⊸≥)𝕨}⌜ ranges # part 1
final_ranges ← ⟨⟩
Fuse ← {
  ⟨a,b⟩𝕊⟨c,d⟩:(a⊸≤∧b⊸≥)c? ⟨a,⌈´b‿d⟩;
  final_ranges (⋈𝕨)⊸∾↩
  𝕩
}
•Show +´ 1⊸+ -˜´¨ final_ranges (⋈¯1⊑Fuse` ranges)⊸∾↩ # part 2
