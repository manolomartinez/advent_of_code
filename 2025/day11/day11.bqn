a ← •Import "../../../Project Euler/aux.bqn"
m ← •Import "/home/manolo/Software/BQN_cosas/bqn-libs/matrix.bqn"
G ← {
# Create the graph, using 𝕩 as starting node
# g is the graph as a hashmap, to each node corresponds a list of children, a
# list of parents, a distance, and a list of parents that have already shared
# their message
  aux ← •Hashmap´((¯1↓⊑)¨⋈1⊸↓¨)' '⊸a.Split¨ •FLines "./input.txt"
  aux.Keys 0
  aux.Get¨ aux.Keys 0
  "out" aux.Set ⟨⟩
  r ← ⟨⟩ # relevant nodes, we will delete the rest
  {o←⍷∾´aux.Get¨ 𝕩⋄r↩⍷r∾o⋄o}•_while_(0<≠) ⋈𝕩 # relevant nodes
  r ⟨𝕩⟩⊸∾↩
  n‿c ←  ⟨r,aux.Get¨r⟩ # nodes, children
  p←n⊸{𝕩/𝕨}¨<˘⍉c{∨´𝕩⊸≡¨𝕨}⌜n # parents
  g←n•Hashmap(c⋈¨p)∾¨<⟨0,⟨⟩⟩ 
  𝕩 g.Set ⟨(⊑g.Get 𝕩),⟨"dummy"⟩,1,⟨"dummy"⟩⟩
  g
}
Add ← { 
  # Add your distance to your children in graph 𝕨
  g𝕊n: # graph and node
  n
  c‿p‿d‿v←g.Get n # distance and children
  {c2‿p2‿d2‿v2←g.Get 𝕩⋄𝕩 g.Set (⋈c2)∾(⋈p2)∾(d+d2)∾(⋈⍷v2∾⋈n)}¨c
  n g.Set ⟨c,p,d,⟨⟩⟩
}
Msg ← {
  # A node 𝕩 sends its distance to its children in graph 𝕨, but only if 𝕩 has
  # received every distance from its parents alrçeady
  c‿p‿d‿v ← 𝕨.Get 𝕩
  (∧´p∊v)◶⟨⊢,𝕨⊸Add⟩ 𝕩 # Has the node received all message from parents?
  ⍷c
}
you ← G "you"
you⊸(∾´Msg¨)•_while_(0<≠) ⋈"you"
•Show 2⊑you.Get "out" # part 1
svr ← G "svr"
dac ← G "dac"
fft ← G "fft"
{⍷∾´svr⊸Msg¨𝕩}•_while_(0<≠) ⋈"svr"
{⍷∾´dac⊸Msg¨𝕩}•_while_(0<≠) ⋈"dac"
{⍷∾´fft⊸Msg¨𝕩}•_while_(0<≠) ⋈"fft"
sf←2⊑svr.Get "fft"
fd←2⊑fft.Get "dac"
do←2⊑dac.Get "out"
•Show sf×fd×do # part 2
