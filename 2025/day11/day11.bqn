a ← •Import "../../../Project Euler/aux.bqn"
m ← •Import "/home/manolo/Software/BQN_cosas/bqn-libs/matrix.bqn"
g←(⊑¨•HashMap 1⊸⊑¨)((¯1↓⊑)⋈1⊸↓)¨' '⊸a.Split¨ •FLines "./input.txt" # graph

#g←(⊑¨•HashMap 1⊸⊑¨)((¯1↓⊑)⋈1⊸↓)¨' '⊸a.Split¨ •FLines "./test2.txt" # graph
"out" g.Set ⟨⟩

p ← t •Hashmap k⊸{𝕩/𝕨}¨ <˘⍉ c {∨´𝕩⊸≡¨𝕨}⌜ t ← ⍷∾´ c← g.Get¨ k←g.Keys 0 # parents
{c ← g.Get 𝕩⋄𝕩 g.Set 0⋈c }¨g.Keys 0 # add a counter
#{n‿c←g.Get 𝕩⋄nc←≠p.Get 𝕩⋄𝕩 g.Set ⟨nc+n,c⟩}¨ p.Keys 0
"you" g.Set 1⋈1⊑ g.Get "you"
Add ← { # Add your distance to your children
  d‿c←g.Get 𝕩 # distance and children
  {d2‿c2←g.Get 𝕩⋄𝕩 g.Set (d+d2)⋈c2}¨c
}

Step ← {
  Add¨𝕩
  ⍷∾´1⊸⊑¨g.Get¨𝕩
}

Step•_while_(0<≠) ⋈"you"
•Show ⊑g.Get "out" # Part 1
Paths ← {
# Create the graph, using 𝕩 as starting node
  #g←(⊑¨•HashMap 1⊸⊑¨)((¯1↓⊑)⋈1⊸↓)¨' '⊸a.Split¨ •FLines "./input.txt" # graph
  g←(⊑¨•HashMap 1⊸⊑¨)((¯1↓⊑)⋈1⊸↓)¨' '⊸a.Split¨ •FLines "./test3.txt" # graph
  "out" g.Set ⟨⟩
  {c ← g.Get 𝕩⋄𝕩 g.Set 0⋈c }¨g.Keys 0 # add a counter
  𝕩 g.Set 1⋈1⊑ g.Get 𝕩
  g
}
Add2 ← { 
  # Add your distance to your children in graph 𝕨
  g𝕊n: # graph and node
  d‿c←g.Get n # distance and children
  {d2‿c2←g.Get 𝕩⋄𝕩 g.Set (d+d2)⋈c2}¨c
}

Step2 ← {
  # Step in graph 𝕨
  𝕨⊸Add2¨𝕩
  •Show 𝕨.Get¨ 𝕨.Keys 0
  •Show ⍷∾´1⊸⊑¨𝕨.Get¨𝕩
}

Step3 ← {
  # Step in graph 𝕨
  g𝕊n: #graph and node
  d‿c←(⊑¨⋈1⊸⊑¨)g.Get¨n # original distances and sets of children
  d{od𝕊sc:{d2‿c2←g.Get 𝕩⋄𝕩 g.Set (od+d2)⋈c2}¨sc}¨c
  •Show 𝕨.Get¨ 𝕨.Keys 0
  •Show ⍷∾´1⊸⊑¨𝕨.Get¨𝕩
}

svr ← Paths "svr"
svr.Get "fft"
dac ← Paths "dac"
dac.Get "fft"
fft ← Paths "fft"
fft.Get "out"


•Show svr.Get¨ svr.Keys 0
svr⊸Step3•_while_(0<≠) ⋈"svr"
dac⊸Step3•_while_(0<≠) ⋈"dac"
fft⊸Step3•_while_(0<≠) ⋈"fft"
sd←⊑svr.Get "dac"
sf←⊑svr.Get "fft"
fd←⊑fft.Get "dac"
df←⊑dac.Get "fft"
do←⊑dac.Get "out"
fo←⊑fft.Get "out"

sf
do
×´sf‿fd‿do
a.Mult´ a.NumtoList¨ sf‿fd‿do
