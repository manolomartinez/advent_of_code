lines ← •file.Lines "./input.txt"
instructions ← ⊑lines
size ← ≠instructions 
ParseLine ← {
  ⟨a,b,c,d⟩ ← 𝕩 ⊔˜ +` ∨´ 𝕩⊸=¨ '('‿','‿')' 
  ⟨3↑a,¯3↑b, ¯3↑c⟩
}
graph ← >˘ParseLine¨ 2↓lines

# Part 1

FindNext ← {
  ⥊(𝕨⊸≡¨ ⊏˘graph) /  (𝕩='R')⊑˘ 1↓˘graph
}
NextInst ← {
  ⟨counter, node⟩ ← 𝕩
  ⟨counter + 1, node FindNext (size | counter) ⊑ instructions⟩
}
•Show ⊑ NextInst •_while_ {(1⊑𝕩) ≢ "ZZZ"} ⟨0, "AAA"⟩

# Part 2

Cycles ← {
  ⟨counter, node⟩ ← 𝕩
  ⟨counter + 1, node FindNext (size | counter) ⊑ instructions⟩
}

•Show •math.LCM´ ⊑¨ (Cycles •_while_ {'Z' ≠ ¯1⊑¯1⊑𝕩})¨ ⥊ 0 ∾¨ <¨('A' = ¯1⊸⊑)¨⊸/ ⊏˘graph
