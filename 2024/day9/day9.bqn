ToNat ⇐ {(10⊸×⊸+˜´∘⌽-⟜'0')𝕩}
Split ⇐ {𝕨((⊢-˜+`×¬)∘=⊔⊢)𝕩}
diskmap ← ToNat •file.Lines "./input.txt"
numbers ← (¬2|↕∘≠)⊸/diskmap
spaces ← (2|↕∘≠)⊸/diskmap
ids ← ↕≠numbers
# I'll make a list with ⟨numbers, spaces, ids⟩

NumberHigher ← {
  numbers ← ⊑𝕩
  spaces ← 1⊑𝕩
  ids ← 2⊑𝕩
  fns ← ⊑⊑/○⥊⟜(↕≢) spaces > 0
  space ← fns⊑spaces
  numbers ((-space)⊸+)⌾(¯1⊸⊑) ↩
  numbers (fns+1)⊸(↓{𝕩∾space∾𝕨}↑) ↩ 
  spaces 0⌾(fns⊸⊑) ↩
  spaces fns⊸(↓{𝕩∾0∾𝕨}↑) ↩ 
  ids ↩ (fns+1)⊸(↓{𝕩∾(¯1⊑ids)∾𝕨}↑) ids
  ⟨numbers, spaces, ids⟩
}

SpaceHigher ← {
  numbers ← ⊑𝕩
  spaces ← 1⊑𝕩
  ids ← 2⊑𝕩
  fns ← ⊑⊑/○⥊⟜(↕≢) spaces > 0
  space ← fns⊑spaces
  number ← ¯1⊑numbers
  spaces (space-number)⌾(fns⊸⊑) ↩
  spaces fns⊸(↓{𝕩∾0∾𝕨}↑) ↩ 
  numbers (fns+1)⊸(↓{𝕩∾number∾𝕨}↑) ↩ 
  numbers ¯1⊸↓ ↩
  ids ¯1⊸↓ ↩ (fns+1)⊸(↓{𝕩∾(¯1⊑ids)∾𝕨}↑) ids
  ⟨numbers, spaces, ids⟩
}

OneMove ← {
  numbers ← ⊑𝕩
  spaces ← 1⊑𝕩
  ids ← 2⊑𝕩
  #first nonzero space
  fns ← ⊑⊑/○⥊⟜(↕≢) spaces > 0
  ((fns⊑spaces) ≥ (¯1⊸+∘≢)⊸⊑ numbers)◶NumberHigher‿SpaceHigher 𝕩
}

# Solution to part 1
+´ (↕≠)⊸× (⊑/2⊸⊑) OneMove •_while_ {∨´((≠2⊸⊑)↑1⊸⊑)𝕩} numbers‿spaces‿ids 

# Part 2 doesn't work. I resorted to doing it in python

OneMove2 ← {
  numbers‿spaces‿ids‿current_id ← 𝕩
  #•Show current_id
  #spaces ← 1⊑𝕩
  #•Show spaces
  #ids ← 2⊑𝕩,
  #current_id ← 3⊑𝕩 
  #first nonzero space
  size ← numbers⊸(⊑˜) id_pos ← ⊑⊑/○⥊⟜(↕≢) current_id = ids
  •Show "size"
  •Show size
  •Show "id_pos"
  •Show id_pos
  slots ← (id_pos)⊸>⊸/ ⥊> /○⥊⟜(↕≢) spaces ≥ size
  #•Show slots
  slot ← (⊑⊑)⎊¯1 slots
  #•Show "slot"
  •Show slot
  
  (¯1≠slot)◶{numbers‿spaces‿ids‿(current_id-1)}‿{
    ⟨(slot+1)⊸(↓{𝕩∾size∾𝕨}↑) id_pos⊸(↑∾1⊸+⊸↓) numbers, 
     slot⊸(↑{𝕨∾0∾𝕩}↓) ((slot⊑spaces)-size)⌾((slot)⊸⊑) (id_pos-1)⊸(↑∾1⊸+⊸↓) (size+(id_pos⊑spaces)+((id_pos-1)⊑spaces))⌾((id_pos)⊸⊑) spaces
    (slot+1)⊸(↓{𝕩∾current_id∾𝕨}↑) id_pos⊸(↑∾1⊸+⊸↓) ids, 
    current_id-1⟩} 𝕩
}


≠numbers

numbersf‿spacef‿idsf‿pos ← OneMove2 •_while_{0≤3⊑𝕩}numbers‿(spaces∾0)‿ids‿(¯1+≠numbers)
+´ +´¨ idsf × (+`0»spacef) + {(𝕩⊸/↕≠𝕩)⊸⊔↕+´𝕩} numbersf
{(𝕩⊸/↕≠𝕩)⊸⊔↕+´𝕩} numbersf

