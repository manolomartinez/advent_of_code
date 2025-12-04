a ← •Import "../../../Project Euler/aux.bqn"
p ← •Import "/home/manolo/Software/BQN_cosas/bqn-libs/primes.bqn"
ranges ← '-'⊸a.Split¨ ',' a.Split ¯2↓ •file.Chars "./input.txt" 
Odd ← (⌊≠⊢)÷⟜2

FixRange ← {
  𝕨𝕊𝕩: (Odd⊑≢𝕨)∧(Odd⊑≢𝕩)? 0‿0;
  𝕨𝕊𝕩: (Odd⊑≢𝕨)∧(¬Odd⊑≢𝕩)? ⟨•Repr 10⋆-⟜1⊑≢𝕩,𝕩⟩;
  𝕨𝕊𝕩: (¬Odd⊑≢𝕨)∧(Odd⊑≢𝕩)? ⟨𝕨,•Repr -⟜1 10⋆⊑≢𝕨⟩;
  ⟨𝕨,𝕩⟩
}

ranges1 ← FixRange´¨ ranges
FindIDs ← {
  0𝕊0: ⟨⟩;
  start ← a.StrToNat (÷⟜2∘⊑≢)⊸↑𝕨
  end ← a.StrToNat (÷⟜2∘⊑≢)⊸↑𝕩
  (≥⟜(a.StrToNat 𝕨))⊸/(≤⟜(a.StrToNat 𝕩))⊸/a.StrToNat¨ (⊑≢𝕩)⊸⥊¨•Repr¨ start + ↕1+end-start
}


•Show +´∾´ FindIDs´¨ ranges1 # Part 1

FixRange2 ← {
  𝕨𝕊𝕩: 𝕨≠○(⊑≢)𝕩? ⟨⟨𝕨,•Repr -⟜1 10⋆⊑≢𝕨⟩,⟨•Repr 10⋆-⟜1⊑≢𝕩,𝕩⟩⟩;
  ⟨⟨𝕨,𝕩⟩⟩
}

ranges2 ← ∾´ FixRange2´¨ ranges


FindAux ← {
  n𝕊⟨s,e⟩:
  start ← a.StrToNat n↑s
  end ← a.StrToNat n↑e
  (≥⟜(a.StrToNat s))⊸/(≤⟜(a.StrToNat e))⊸/a.StrToNat¨ (⊑≢s)⊸⥊¨•Repr¨ start + ↕1+end-start
}

FindIDs2 ← {
  s𝕊e:
  candidates ← ↕⊸(⊣/˜0=|)⊑≢𝕨
  {𝕩 FindAux s‿e}¨ candidates
}

•Show +´⍷∾´∾´ FindIDs2´¨ ranges2 # Part 2
