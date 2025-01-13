Split ⇐ {𝕨((⊢-˜+`×¬)∘=⊔⊢)𝕩}
ToNat ⇐ {(10⊸×⊸+˜´∘⌽-⟜'0')𝕩}

stones ←  ' 'Split ⊑•file.Lines "./input.txt" 

# Part 1
Change ← {
  𝕊 "0": "1";
  𝕊 a: (⊢=⌊)0.5×≠a? •Fmt ¨ToNat¨(0.5×≠)⊸(↑⋈↓)a;
  •Fmt 2024 × ToNat 𝕩
}

≠{∾⋈⍟(1=≡)¨Change¨𝕩}⍟25 stones # Solution to part 1

# Part 2

Change2 ← {
  𝕊 ⟨"0"⟩: ⟨"1"⟩;
  𝕊 a: (⊢=⌊)0.5×≠⊑a? •Fmt ¨ToNat¨(0.5×≠)⊸(↑⋈↓)⊑a;
  ⟨•Fmt 2024 × ToNat ⊑𝕩⟩
}

counter_stones ← ((⟨1⟩/˜≠)⋈⊢){⟨𝕩⟩}¨stones

Full ← {
  counters‿strings ← 𝕩
  multipliers ← ≠¨ newstrings ← Change2¨ strings
  uniques ← ∊⊸/  newstrings ∾´ ↩ 
  ({+´(𝕩⊸≡¨ newstrings)⊸/(multipliers / counters)}¨⋈{⟨𝕩⟩}¨) uniques
 } 

+´⊑Full⍟75 counter_stones # Solution to part 2


