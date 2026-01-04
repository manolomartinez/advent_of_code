a ← •Import "../../../Project Euler/aux.bqn"
s‿p←30(↑⋈↓)•Flines "./input.txt" #shapes and presents
s {'#'⊸=¨¨¨¯1⊸↓¨1⊸↓¨5(⌊∘÷˜⟜(↕≠)⊔⊢)𝕩}↩
z ← a.StrtoNat¨¨('x'⊸a.Split∘⊑)¨':'⊸a.Split¨ p # sizes
c ← a.StrtoNat¨¨' '⊸a.Split¨ 1⊸↓¨1⊸⊑¨ ':'⊸a.Split¨ p # catalog
n ← +´¨c×¨<areas ← +´⍟2¨s # area needed
aa ← ×´¨z # available area
# These are the initially possible problems (the others don't have enough area)
z‿c (aa ≥ n)⊸/¨ ↩ 

# Now I calculate the more or less trivial problems (those that have enough
# space to simply put the 3x3 presents side by side, without fitting)
(≠z)=+´(×´¨z) ≥¨ +´¨(6/⋈9)⊸×¨c
# So, it seems that rectangular packing should be enough for many of these
# problems, or all.

# Do the total number of presents (I'm going to think of them as equal squares
# for the time being) fit?
•Show +´ (×´¨⌊¨¨÷⟜3¨¨z) ≥ +´¨c # part 1

