Split ⇐ {𝕨((⊢-˜+`×¬)∘=⊔⊢)𝕩}
ToNat ⇐ {(10⊸×⊸+˜´∘⌽-⟜'0')𝕩}
Where ⇐ {⊑(𝕨⊸=/↕∘≠)𝕩} # Index of first 𝕨 in 𝕩

reports ← •file.Lines "./input.txt" 
Parse ⇐ {ToNat¨¨ 𝕨⊸Split¨ (∨´¨𝕨⊸=¨)⊸/𝕩}

rules ← '|' Parse reports
updates ← ',' Parse reports
# Part 1
+´ ((⌊0.5×≠)⊸⊑)¨ {∧´<´¨𝕩⊸(Where˜)¨⎊⟨1,2⟩¨ rules}¨⊸/ updates # Solution of part 1
# Part 2
Sorted ← {𝕨=⊑⊑(∧´˘∨´˘ rules =⌜ 𝕨‿𝕩)⊸/ rules}
+´ ((⌊0.5×≠)⊸⊑)¨ (updates⊸(≢¨))⊸/ ((∾∾⊔˜1∾Sorted¨)˝¨) updates # Solution to part 2

