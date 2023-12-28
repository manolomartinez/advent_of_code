map ← '#' = >•file.Lines ("./input.txt")
# Part 1
Expand ← {
  n ← 1⊑≢𝕩
  {𝕨 ∾ ((0¨↕n)⊸∾) 𝕩}´ (+`(¬∨´˘))⊸⊔ 𝕩
}
•Show +´+˝ (<⌜˜↕∘≠)⊸× (+´|∘-)⌜˜ /○⥊⟜(↕≢) ⍉ Expand ⍉ Expand map 

# Part 2
NewExpand ← {
  (⊑𝕩) ∾ +` ((𝕨 - 1) × ×⊸1⊸<)⊸+ (1⊸↓ - ¯1⊸↓) 𝕩
}
rows ← ⊑˘ >/○⥊⟜(↕≢) map
new_rows ← 1000000 NewExpand rows
sort_cols ← ⍋cols ← 1⊑˘ >/○⥊⟜(↕≢) map
new_cols ← 1000000 NewExpand sort_cols ⊏ cols
•Show +´+˝ (<⌜˜↕∘≠)⊸× (+´|∘-)⌜˜ new_rows ∾¨ new_cols
