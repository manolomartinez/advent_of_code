# Day 1

# Part 1

ids ← •file.Lines "./input.txt" 
mask ← 0‿0‿0‿0‿0‿¯1‿¯1‿¯1‿1‿1‿1‿1‿1
+´|-´<˘∧˘⍉{+´(10⊸⋆⌽∘↕∘≠)⊸×-⟜'0'𝕩}¨>mask⊸⊔¨ids # Answer to part 1
# Part 2

lists ← ⍉{+´(10⊸⋆⌽∘↕∘≠)⊸×-⟜'0'𝕩}¨>mask⊸⊔¨ids
+´ (+´1⊏lists⊸=)¨⊸× 0⊏lists # Answer to part 2
