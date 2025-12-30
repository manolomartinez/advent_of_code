a ← •Import "../../../Project Euler/aux.bqn"
m ← •Import "/home/manolo/Software/BQN_cosas/bqn-libs/matrix.bqn"

Parse ← {
  l1‿l2‿l3 ← ∾´((⋈⊑)⋈((¯1⊸↓⋈¯1⊸⊑)1⊸↓))𝕩
  l1↩'#'⊸=¨('.'⊸=∨'#'⊸=)⊸/l1
  l2↩(↕∘≠l1)⊸∊¨(a.StrtoNat¨',' a.Split('('⊸≠∧')'⊸≠)⊸/)¨ l2
  l3↩a.StrtoNat¨',' a.Split('{'⊸≠∧'}'⊸≠)⊸/ l3
  l1‿l2‿l3
}

machines ← Parse¨ ' '⊸a.Split¨ •FLines "./input.txt" 

Doable ← {
  𝕨𝕊l1‿l2‿l3:
  ∨´(𝕨 <˘∘a.Combinations ≠l2){l1≡2|+´𝕨⊏𝕩}¨<l2 
}

•Show +´{𝕊m:1⊸+•_while_ {¬𝕩 Doable m} 1}¨ machines # part 1
