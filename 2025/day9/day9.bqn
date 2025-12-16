a ← •Import "../../../Project Euler/aux.bqn"
coords ← a.StrToNat¨¨ ','⊸a.Split¨ •FLines "./input.txt" 
•Show ⌈´⥊(×´1+-)⌜˜coords # part 1
cc ← ((∧∘⍷⊸⊐⊑¨)⋈¨(∧∘⍷⊸⊐1⊸⊑¨))coords # coordinate compression

Fillx ← {
  𝕊c:
  xs ← {(⊑⊑𝕩)⊸⋈¨(⌊´⋈⌈´)1⊸⊑¨𝕩}¨((⍷⊑¨c)=¨<(⊑¨c)){𝕨⊸/𝕩}¨<c
  ∾´{(⊑⊑𝕩)⊸⋈¨(⊑+(↕1+1⊸⊑-⊑))1⊸⊑¨𝕩}¨xs 
}

Filly ← {
  𝕊c:
  ys ← {(⊑1⊸⊑¨𝕩) ⋈˜¨(⌊´⋈⌈´)⊑¨𝕩}¨((⍷1⊸⊑¨c)=¨<(1⊸⊑¨c)){𝕨⊸/𝕩}¨ <c
  ∾´{⋈¨⟜(1⊑⊑𝕩)(⊑+(↕1+1⊸⊑-⊑))⊑¨𝕩}¨ys 
}
filled ← (∨Filly∘Fillx) cc
FullSquare ← {
  a‿b𝕊c‿d:
  maxbd‿minbd ← ∨b‿d
  maxac‿minac ← ∨a‿c
  top←maxac⋈¨minbd + ↕1+maxbd-minbd 
  bottom←minac⋈¨minbd + ↕1+maxbd-minbd 
  right←maxbd⋈˜¨minac + ↕1+maxac-minac 
  left←minbd⋈˜¨minac + ↕1+maxac-minac 
  ∧´(⍷∾´ top‿bottom‿right‿left) ∊ filled
}
sorted←(⍒⥊(×´1+-)⌜˜coords)⊑¨<⥊⋈⌜˜cc
•Show (×´1+-)´(<coords) ⊑˜¨cc⊐sorted⊑˜1⊸+•_while_{¬FullSquare´ 𝕩⊑sorted} 0 # part2
