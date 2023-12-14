# Part 1
almanac ← ((0⊸≠∘≠)¨⊸/)¨ ⊔˜⟜(+` 0 = ≠¨) •file.Lines "./input.txt" 
seeds ←  •ParseFloat¨ 1↓ ' '((¬-˜⊢×·+`»⊸>)∘≠⊔⊢) ⊑⊑ almanac
ParseMap ← >{•ParseFloat¨ ' '((¬-˜⊢×·+`»⊸>)∘≠⊔⊢)𝕩}¨∘(1⊸↓)
maps ← ParseMap¨ 1↓ almanac
InRange ← {(1⊑˘𝕩⊸≤ ∧ ((1⊸⊑˘+ 2⊸⊑˘)𝕩)⊸>) 𝕨}
MapsTo ← {
  in_range ← 𝕨 InRange 𝕩 
  map ← 𝕩
  {𝕩 + (⊑-1⊸⊑) ⥊ in_range / map} ⍟ (∨´ in_range) 𝕨
}
•Show ⌊´ MapsTo˜´⟜(⌽maps)¨ seeds

# Part 2

seeds +`˘∘(∘‿2⊸⥊) ↩
seeds -⟜1⌾(¯1⊸(↑˘)) ↩
seeds ↩ ∾(<<˘seeds)‿⟨⟨⟩⟩
OneSeedOneMap ← { 
  overlap ← ⍉((⊑𝕨)⌈1⊑𝕩) ≍ (1⊑𝕨)⌊((1⊸⊑ + 2⊸⊑)𝕩) - 1
  complement ← ⟨⟨⊑𝕨,(1⊑𝕨)⌊(1-˜1⊑𝕩)⟩,⟨⊑𝕨⌈(1⊸⊑ + 2⊸⊑)𝕩, 1⊑𝕨⟩⟩
  map ← 𝕩
  images ← {overlap + (⊑ - 1⊸⊑) map} ⍟ (≤´ overlap) ⟨⟩ # images in the overlap
  ⟨((≤´¨ complement) / complement), ⟨images⟩⟩
}
VariousSeedsOneMap ← {
  ⟨⟨⟩,b⟩𝕊𝕩: 𝕨;
  ⟨seeds, images⟩ ← 𝕨
  ⟨new_seeds, new_images⟩ ← ∾¨´OneSeedOneMap⟜𝕩¨ seeds
  ⟨new_seeds, images ∾ new_images⟩
}
VariousSeedsVariousMaps ← {
  ((0⊸<≠¨)⊸/ (∾´ (𝕨 VariousSeedsOneMap˜´ <˘𝕩)))‿⟨⟩
}
•Show  ⊑⊑∧⊏¨⥊>⊏ seeds VariousSeedsVariousMaps˜´ ⌽maps
