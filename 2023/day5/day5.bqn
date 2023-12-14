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
# •Show ⌊´ MapsTo˜´⟜(⌽maps)¨ seeds

# Part 2

seeds +`˘∘(∘‿2⊸⥊) ↩
seeds -⟜1⌾(¯1⊸(↑˘)) ↩
seeds ↩ ∾(<<˘seeds)‿⟨⟨⟩⟩
seeds

OneSeedOneMap ← { 
  # •Show "𝕩"
  # •Show 𝕩
  # •Show "𝕨"
  # •Show 𝕨
  overlap ← ⍉((⊑𝕨)⌈1⊑𝕩) ≍ (1⊑𝕨)⌊((1⊸⊑ + 2⊸⊑)𝕩) - 1
  # •Show overlap
  complement ← ⟨⟨⊑𝕨,(1⊑𝕨)⌊(1-˜1⊑𝕩)⟩,⟨⊑𝕨⌈(1⊸⊑ + 2⊸⊑)𝕩, 1⊑𝕨⟩⟩
  # •Show complement
  map ← 𝕩
  images ← {overlap + (⊑ - 1⊸⊑) map} ⍟ (≤´ overlap) ⟨⟩ # images in the overlap
  ⟨((≤´¨ complement) / complement), ⟨images⟩⟩
}
VariousSeedsOneMap ← {
  ⟨⟨⟩,b⟩𝕊𝕩: 𝕨;
  # •Show 𝕩
  # •Show 𝕨
  ⟨seeds, images⟩ ← 𝕨
  # •Show OneSeedOneMap⟜𝕩¨ seeds 
  # •Show ≠ OneSeedOneMap⟜𝕩¨ seeds 
  # •Show "seeds"
  # •Show seeds

  result ← OneSeedOneMap⟜𝕩¨ seeds 
  # •Show "result"
  # •Show result
  # ⟨new_seeds, new_images⟩ ← {<˘((>⊏¨)𝕩) ≍ (>1⊸⊏¨)𝕩}result
  ⟨new_seeds, new_images⟩ ← ∾¨´result
  # •Show "⟨new_seeds, new_images⟩"
  # •Show ⟨new_seeds, new_images⟩
  ⟨new_seeds, new_images⟩
}
VariousSeedsVariousMaps ← {
  # •Show "VariousSeedsVariousMaps"
  •Show ((0⊸<≠¨)⊸/ (∾´ (𝕨 VariousSeedsOneMap˜´ <˘𝕩)))‿⟨⟩
  ((0⊸<≠¨)⊸/ (∾´ (𝕨 VariousSeedsOneMap˜´ <˘𝕩)))‿⟨⟩
  # ∾´((1⊑(𝕨 VariousSeedsOneMap˜´ <˘𝕩)))‿⟨⟩
}
# seeds VariousSeedsVariousMaps (⊑maps)
 # ⟨77,80⟩OneSeedOneMap⟨68,78,1⟩
 # seeds
# ((seeds VariousSeedsVariousMaps ⊑maps) VariousSeedsVariousMaps 1⊑maps) VariousSeedsVariousMaps 2⊑maps
# ⥊⟨⟨1, 2, 3⟩⟩
# OneSeedOneMap⟜⟨68,78,1⟩¨⟨⟨77,80⟩⟩
# testseeds ← ⟨⟨⟨82,82⟩⟩,⟨⟩⟩
# result ← OneSeedOneMap⟜firstmap¨ testseeds 
# seeds
# maps
# testseeds VariousSeedsOneMap firstmap
seeds VariousSeedsVariousMaps˜´ ⌽maps
result ← ∧⊏¨⥊>⊏ seeds VariousSeedsVariousMaps˜´ ⌽maps
