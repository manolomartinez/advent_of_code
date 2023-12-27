lines ← •file.Lines ("./input.txt") 
columns ← ≠lines
rows ← ≠⊑lines
map ← columns‿rows⥊∾ lines
init_coords ← ⥊> /○⥊⟜↕⟜≢ 'S' = map
pipes ← "|-LJ7F"
movements ← ⟨⟨⟨¯1, 0⟩, ⟨1, 0⟩⟩, ⟨⟨0, 1⟩, ⟨0, ¯1⟩⟩, ⟨⟨¯1, 0⟩, ⟨0, 1⟩⟩, ⟨⟨¯1, 0⟩, ⟨0, ¯1⟩⟩, ⟨⟨1, 0⟩, ⟨0, ¯1⟩⟩, ⟨⟨1, 0⟩, ⟨0, 1⟩⟩, ⟨⟩⟩
manhattan ← <˘(⌽˘⊸∾)¯1⊸×⊸≍⟨1, 0⟩ # Manhattan neighborhood

# Part 1
Connected ← {
  pipe ← 𝕩 ⊑ map
 ((⊑⥊ pipes ⊐ pipe) ⊑ movements) + <𝕩
}
# This is one beginning of the loop
beginning ← init_coords {⟨𝕨⟩∾<⊑(>(<𝕨)⊸∊¨ Connected¨ 𝕩 + <𝕨) / 𝕩 + <𝕨} manhattan
NextStep ← {
  counter‿path ← 𝕩
  ⟨≠path, path ∾ (¬(Connected ¯1⊑path) ∊ path) / (Connected ¯1⊑path)⟩
}
⟨counter,loop⟩ ← NextStep •_while_ {(⊑𝕩) < ≠¯1⊑𝕩} 0‿beginning
•Show ⌊÷⟜2 counter

# Part 2

loop_in_map ← ¬(↕≢map) ∊ loop
not_in_loop ← (¬∘∊⟜loop)⊸/(⥊↕≢map)
operations ← ⟨⥊∘<∘⊢, ⥊∘<∘⊢, <˘∘(⊢≍-∘⌽), <˘∘(⊢≍⌽), <˘∘(⊢≍-∘⌽), <˘∘(⊢≍⌽)⟩
# follow the inside of the loop
# First, make the loop start after the first '-' tile
first_horizontal ← (⊑ (loop ⊑ map) ⊐ '-') # position of the first '-' tile 
one_end ← first_horizontal ↓ loop # from first_horizontal to one end of the loop
other_end ← ⌽1↓ (first_horizontal + 1) ↑ loop # from first_horizontal to the other end of the loop, without the S

Complete ← {
 {⟨≠1⊑𝕩, ⍷ ∊⟜not_in_loop⊸/ ((1⊑𝕩) ∾ ⥊ (1⊑𝕩) +⌜ manhattan)⟩} •_while_ {⊑𝕩 < ≠1⊑𝕩} 0∾<𝕩
}

ChangeOrientation ← {
  (⊑pipes⊐𝕩)◶operations ¯1⊑𝕨
}

FollowLoopOne ← {
  ∾´ 𝕩 <⊸+¨ (<⟨⟨¯1, 0⟩⟩) ChangeOrientation` 𝕩 ⊑ map
}
FollowLoopOther ← {
  ∾´ 𝕩 <⊸+¨ (<⟨⟨1, 0⟩⟩) ChangeOrientation` 𝕩 ⊑ map
}

one ← (↕≢map) ∊1⊑ Complete /○⥊⟜(↕≢) (loop_in_map ∧ (↕≢map) ∊ other_end ∾○FollowLoopOne one_end) 
other ← (↕≢map) ∊1⊑ Complete /○⥊⟜(↕≢) (loop_in_map ∧ (↕≢map) ∊ other_end ∾○FollowLoopOther one_end) 
some_outer_tiles ← {∨´ ⟨∧`𝕩, ⌽∧`⌽ 𝕩, ⍉∧`⍉ 𝕩, ⌽˘⍉∧`⍉⌽˘ 𝕩⟩}loop_in_map
•Show +´+˝ (∨´∨˝ other ∧ some_outer_tiles) ⊑ ⟨other, one⟩
