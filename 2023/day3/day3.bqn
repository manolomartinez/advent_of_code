map ← •file.Lines "./test.txt"
map_arr ← 10‿10⥊∾map

# Part 1

Pad ← ⊢↑˝·≍⟜¬2+≢ # zeros all around
nums ← (0⊸≤∧10⊸>) map_arr - '0'
symbols ← (¬nums) ∧ ¯2⊸≠ map_arr - '0'
padded_symbols ← Pad symbols
sym_windows ← <⎉2 3‿3↕padded_symbols
next_to_symbol ← (∨´ ⥊)¨ sym_windows
groups ← nums × {(+` ⌈´˘ 𝕩) +˘ 𝕩}(+`˘) ¬nums
•Show +´ •ParseFloat¨ (∨´¨ groups ⊔ nums ∧ next_to_symbol) / groups ⊔ map_arr

# Part 2

stars ← ¯6 = map_arr - '0'
padded_nums ← Pad nums
num_windows ← <⎉2 3‿3↕padded_nums
how_many_numbers ← {+´ (1 ≤ +´˘ 𝕩) + 𝕩 ∧˝∘=⎉1 1‿0‿1}¨ num_windows
gears ← stars ∧ how_many_numbers = 2 
# gear_windows ← <⎉2 3‿3↕ Pad gears
#next_to_gear ← (∨´ ⥊)¨ gear_windows
#+´ ×´˘ ∘‿2 ⥊ •ParseFloat¨ (∨´¨ groups ⊔ nums ∧ next_to_gear) / groups ⊔ map_arr
gear_idx ← ⍉ (⌊ (/ ⥊ gears) ÷ 10) ≍ 10 | (/ ⥊ gears)
each_gear ← {1⌾(𝕩⊸⊑) 10‿10⥊<0}¨<˘gear_idx
gear_windows ← (<⎉2 3‿3↕ Pad)¨ each_gear
next_to_gear ← (∨´ ⥊)¨¨ gear_windows
•Show +´ ×´¨ {•ParseFloat¨ (∨´¨ groups ⊔ nums ∧ 𝕩) / groups ⊔ map_arr}¨ next_to_gear
