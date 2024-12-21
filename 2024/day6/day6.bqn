# padded with "e" for "end" and another layer of objects
map ←' '(⊢+=×'#'-⊣) (⊢↑˝·≍⟜¬2+≢) ' '(⊢+=×'.'-⊣) (⊢↑˝·≍⟜¬2+≢) > •file.Lines "./input.txt"  

# Part 1
MoveUp ← {⟨1,0⟩ + ⊑(⌈´⊸= ⊑¨)⊸/𝕨⊸{𝕨((>○⊑)∧(=○(1⊸⊑)))𝕩}¨⊸/𝕩}# going up
Move ← {
  map ← 𝕩 
  objects ← /○⥊⟜(↕≢) map = '#'
  cursor ← ⊑/○⥊⟜(↕≢) map = '^'
  newcursor ← cursor MoveUp objects
  map ↩ '^'(⊢+=×'X'-⊣) map
  map ↩ '^' ⌾(newcursor⊸⊑) map
  trail ← (1⊑cursor) ∾˜¨ (↕(⊑cursor⊸-))⊸+⊑newcursor + 1
  ⌽⍉ map {'X' ⌾(𝕨⊸⊑) 𝕩 }´ trail
}

Inside ← {
  cursor ← ⊑/○⥊⟜(↕≢) '^' = 𝕩 # this is the one
  ¬ ∨´∨´˘ cursor =⌜ 1≍(⊑≢map) - 2
}

+´ ⥊  'X' = Move •_while_ Inside map # Solution to Part 1

# Part 2

Move2 ← {
  map ← ⊑𝕩 
  cursors ← 1⊑𝕩
  objects ← /○⥊⟜(↕≢) map = '#'
  cursor ← ⊑/○⥊⟜(↕≢) '^' = map 
  newcursor ← cursor MoveUp objects
  cursors {𝕩 ∾ <newcursor} ↩
  map {'^'⌾(newcursor⊸⊑) 𝕩} ↩ 
  map ↩ ¬∘(cursor ≢ newcursor)◶{'.'⌾(cursor⊸⊑) 𝕩}‿{𝕩} map
  ⟨⌽⍉ map, cursors⟩
}

initcursor ← ⊑/○⥊⟜(↕≢) map = '^'
empty ← /○⥊⟜(↕≢) map = '.'
maps ← {'#' ⌾(𝕩⊸⊑) map }¨ empty

Loop ← {
  data ← ⟨𝕩, ⟨initcursor⟩⟩
  {2 < ⌈´⊒1⊑𝕩} Move2 •_while_ ({2 ≥ ⌈´⊒1⊑𝕩} ∧ Inside∘⊑) data
}
+´ Loop¨ maps # Solution to part 2---takes forever

