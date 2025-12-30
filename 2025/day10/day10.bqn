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
#machines ← Parse¨ ' '⊸a.Split¨ •FLines "./test.txt" 

Doable ← {
  𝕨𝕊l1‿l2‿l3:
  ∨´(𝕨 <˘∘a.Combinations ≠l2){l1≡2|+´𝕨⊏𝕩}¨<l2 
}

•Show +´{𝕊m:1⊸+•_while_ {¬𝕩 Doable m} 1}¨ machines # part 1

# For part 2 we need to look into the minimum number of presses to get each
# joltage value.
# Take for example {60,61,248,220,221,242,246}
# Here we need to use combos that contain 0 60 times, combos that contain 1 61
# times, etc.
# This seems to point to a system of equations: 
# The combos for that line are (0,1,4,5,6) (1,4,6) (0,1,2,5) (1,2,3) (0,2,3,5,6) (0,1,3,6) (2,3,4,5,6) (0,1,2,4,5,6)
# lets call the variables for the combes c0, c1, .. c7, so:
# c0 + c2 + c4 + c5 + c7 = 60
# c0 + c1 + c2 + c3 + c5 + c7 = 61
# etc.
# And there's an extra equation that we can use to calculate the minimum. We
# start with the maximum joltaje j and say
# c0 + ... + c7 = j
# and if there is no all-natural-numbers inverse we move on to j+1, etc


#⌈´⌊´¨ 2⊸⊑¨ machines
#⌈´≠¨ 1⊸⊑¨ machines
#
# Bell number
{⊑(+`⊢´⊸∾)⍟𝕩⥊1} 3
# Like a restricted Bell number
# 1 1 1 1
# 1 2 3 4
# 1 3 6 10
# 1 4 10 20

Pn←{
#  number of partitions of 𝕩 of size 𝕨
  ¯1⊸⊑(+`⊢)⍟(𝕨-1)(𝕩+1)/⋈1
}

pahash ← ⟨⟨1,1⟩⟩ •HashMap ⋈⋈1
Pa←{
  pahash.Has 𝕨‿𝕩?pahash.Get 𝕨‿𝕩;
  #  Actual partitions of 𝕩 of size 𝕨
  1𝕊𝕩: 1‿𝕩 pahash.Set ⋈⋈𝕩⋄pahash.Get 1‿𝕩;
  𝕨‿𝕩 pahash.Set ∾´{(⊑𝕩)⊸∾¨1⊸⊑𝕩}¨((𝕩⊸-)⋈¨((𝕨-1)⊸𝕊¨))(↕𝕩+1)
  pahash.Get 𝕨‿𝕩 
}


Pa_old←{
  #  Actual partitions of 𝕩 of size 𝕨
    1𝕊𝕩:⋈⋈𝕩;
    ∾´{(⊑𝕩)⊸∾¨1⊸⊑𝕩}¨((𝕩⊸-)⋈¨((𝕨-1)⊸𝕊¨))(↕𝕩+1)
}

1 Pa 1
sumhash ← ⟨1⟩ •HashMap ⟨⋈⋈1⟩
WaystoSum_aux ← {
  S 1:⋈⋈1;
  ways ← {(𝕩⊸-⋈⊢)¨1+↕⌊÷⟜2𝕩}𝕩
  𝕩 sumhash.Set ∾´⟨⋈⋈𝕩⟩∾{a‿b← 𝕩⋄⥊(sumhash.Get a)∾⌜sumhash.Get b}¨ways
  sumhash.Get 𝕩
  }
WaystoSum ⇐ {∧⍷∧¨¯1⊸⊑ WaystoSum_aux¨1⊸+∘↕ 𝕩}


≠ 5 Pa 7

l1‿l2‿l3 ← ⊑machines
l2
l3
⍉>l2
#+´ l3 m.MP (m.Inverse >l2) 
#(↕≠l3)⊸∊˘ >l2 


{l1‿l2‿l3 ← 𝕩⋄(+´˘⍉>l2)Pn¨l3}¨machines
⌊´{l1‿l2‿l3 ← 𝕩⋄⌊´l3}¨machines


Step ← {
# Step gets a list of previous button pushes, an l2 and l3; and returns a list
# of lists, were each member is a list of button pushes, a new l2 and a new l2
  𝕊⟨⟩:⟨⟩;
  𝕊p‿⟨⟩‿⟨0⟩:⋈𝕩;
  𝕩
  p‿l2‿l3 ← 𝕩
  l2 (0<l3)⊸/¨↩
  l3 (0<⊢)⊸/↩
  # n the number to match
  # c for candidates, the buttons that can contribute
  c←{(↕≠l2)/˜𝕩⊸⊑¨l2} n←⊑⍋(+´˘⍉>l2)Pn¨l3
  m ← ⌊´¨l2 /¨ <l3 # max button presses per button
  b←(≠c)Pa((n⊑l3)⌈n⊑m) # button presses
  l3s ← (<l3) -¨ +´¨b ×¨ <c ⊏ l2
  f ← ∧´¨0⊸≤¨ l3s ((↕≠l3)≠⌜n)⊸/¨ ↩
  l2 (∧´˘(↕≠l2)≠⌜c)⊸/↩
  l2 ((↕≠l3)≠⌜n)⊸/¨ ↩
  l3s (∧´¨0⊸=¨(0⊸=¨+´l2)⊸/¨l3s)⊸/↩
  {f⊸/ ∾´¨((<p)+¨+´¨b)⋈¨(<l2)⋈¨𝕩}⎊⟨⟩ l3s
}

machines2 ← {𝕊·‿l2‿l3: ⋈0‿l2‿l3}¨machines
Step 0‿l2‿l3
((↕≠l3)≠6)

Combs ← {l2‿l3 ← 𝕩⋄⊑⍋(<+´˘⍉>l2)Pn¨l3}

Step2 ← {
# Step gets a list of previous button pushes, an l2 and a list of l3; and
# returns a list of lists, were each member is a list of button pushes, a new l2
# and a new list of l3s
  #𝕊⟨⟩:⟨⟩;
  #𝕊p‿⟨⟩‿⟨0⟩:⋈𝕩;
  p‿l2‿l3 ← 𝕩
  #l2 (0<l3)⊸/¨↩
  •Show l3 (∨´0<⊢)⊸/¨↩
  # n the number to match
  # c for candidates, the buttons that can contribute
  c←{(↕≠l2)/˜𝕩⊸⊑¨l2} n←⊑⍋(+´˘⍉>l2)Pn¨⊑l3
  #c←{(↕≠l2)/˜𝕩⊸⊑¨l2} n←{⊑⍋+´˘⍉>𝕩}l2
  b←(≠c)Pa(n⊑⊑l3) # button presses
  l3s ← ∾´{(<𝕩)-¨+´¨b×¨<c⊏l2}¨ l3
  #f ← ∧´¨0⊸≤¨ l3s((↕∘≠⊑l3)≠n)⊸/¨ ↩
  l3s((↕∘≠⊑l3)≠n)⊸/¨ ↩
  l2(∧´˘(↕≠l2)≠⌜c)⊸/↩
  •Show l2 ((↕≠⊑l3)≠n)⊸/¨ ↩
  •Show l3s (∧´¨0⊸=¨(0⊸=¨+´l2)⊸/¨l3s)⊸/↩
  •Show l3s (∨´0<⊢)⊸/¨ ↩
  #l3s (0=≠l3s)◶⟨l3s,⋈"none"⟩ ↩
  #{∾⊸/ ∾´¨((<p)+¨+´¨b)⋈¨(<l2)⋈¨𝕩}⎊⟨⟩ l3s
  ∾´¨(n⊑⊑l3)⋈¨(<l2)⋈¨{𝕩⊔˜⊐Combs l2‿𝕩}l3s
}



#machines2 ← {𝕊·‿l2‿l3: ⋈0‿l2‿l3}¨machines
#{⌊´⊑¨(∾´Step2¨)•_while_{∨´0⊸≠≠¨1⊸⊑¨𝕩}𝕩}¨ machines2
l2

#(∾´Step¨)•_while ⋈0‿l2‿l3


Step3 ← {
  # Step gets an "object" (list). In this object there id: 
  # * p: A number of previous button pushes 
  # * l2: A list of button codes
  # * l3s: A iist of lists of joltages
  # It r⋈turns a list of objects of the same kind.
  𝕊·‿⟨⟩‿·:𝕩;
  p‿l2‿l3s ← •Show 𝕩
  # We first choose one member of l3, the one with the most zeros, no negatives,
  # and the smallest other numbers
  #•Show l3 ← {𝕩/˜•Show(⌊´=⊢)•Show +´¨𝕩}{𝕩/˜(⌈´=⊢)+´¨(0⊸=)¨𝕩}(∧´0⊸≤)¨⊸/l3s
  l3 ← ⊑l3s/˜(⌈´=⊢) +´¨0⊸=¨l3s # Which members of any l3 are zero?
  z ← /0⊸=l3 # Which members of any l3 are zero?
  # n the number to match
  # c for candidates, the buttons that can contribute
  •Show c←{(↕≠l2)/˜𝕩⊸⊑¨l2} •Show n←⊑(¬∘∊)⟜z⊸/⍋(+´˘⍉>l2)Pn¨•Show l3
  b←(≠c)Pa(n⊑l3) # button presses
  l3n ← ∾´{(<𝕩)-¨+´¨b ×¨<c⊏l2}¨l3s # the new l3s
  l2 (∧´˘(↕≠l2)≠⌜c)⊸/↩
  ⟨p++´⊑b,l2,l3n⟩
}

Pick ← {
  # Pick the best l3 to follow
  l2‿l3 ← 𝕩
  z←0≤⊑l3 # Which members of any l3 are positive?
  m ← ⌊´ ∾´ c ←{(+´˘⍉>l2)Pn¨𝕩}¨l3 # c for counts, m for minima
}

Regroup ← {
  𝕊·‿⟨⟩‿·:𝕩;
  𝕊p‿l2‿l3:
  l3 (∧´0⊸≤)¨⊸/ ↩
  l3s←l3⊔˜⊐{Combs l2‿𝕩}¨l3
  {p‿l2‿𝕩}¨l3s
}



{Step3•_while_{0⊸≠≠1⊸⊑𝕩}𝕩}¨ machines2


Replace ← {b𝕊a:⌊´a{𝕨⌾(𝕩⊸⊑)(≠b)/⋈∞}¨(↕≠b)/˜b}
((⍋≠¨)⊏⊢)
Compatible ← ∧´(=∨{(∞⊸=𝕨)∨(∞⊸=𝕩)})¨
Compose ← {⍷(0⊸≠≠)¨⊸/∾´<˘𝕨(Compatible◶⟨⟨⟩,(=◶⌊‿⊢)¨⟩)⌜𝕩}
Calc ← {
  ·‿l2‿l3←𝕩
  ⌊´+´¨Compose´ ((⍒≠¨)⊏⊢)(<˘⍉>l2){𝕨⊸Replace¨𝕩}¨(+´˘⍉>l2)Pa¨l3
}


# Possible presses per joltage
(<˘⍉>l2){𝕨⊸Replace¨𝕩}¨(+´˘⍉>l2)Pa¨l3
