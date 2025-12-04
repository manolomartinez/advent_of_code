a ← •Import "../../../Project Euler/aux.bqn"
l←-⟜12⊑≢⊑ banks←-⟜'0'˜¨¨ •file.Lines "./input.txt" 
•Show +´a.ListtoNum¨({s←(-⟜1 ⊑∘≢)⊸≠⊸/𝕩⋄(⊑s)⋈⊑(⊑s)⊸<⊸/𝕩}⍒)⊸⊏¨banks # Part 1
•Show +´a.ListtoNum¨{𝕊b:¯1 {⊑((𝕨+1)⊸≤∧𝕩⊸≥)⊸/⍒b}`(l+↕12)}⊸⊏¨banks # Part 2
