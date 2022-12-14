import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image
import matplotlib.pyplot as plt
from collections import Counter

image = Image.open('dna.jpg')

st.image(image, use_column_width=True)

st.write("""
# DNA Nucleotide Count

This app EDAs the Genomic Sequence

***
""")

st.header('Enter DNA Sequence')

sequence_input = ">DNA Query\n ATGCGCGTAGCGCTCAGCATCAGACTCA"
sequence = st.text_area("Sequence Input", sequence_input, height=250)
sequence = sequence.splitlines()
sequence = ''.join(sequence)

st.write('''***''')

st.header("Input DNA Query")
sequence

st.header("Output")

st.subheader('1. Print Dictionary')
def DNA_nucleotide(seq):
	d = dict([('A', seq.count('A')),('T',seq.count('T')),('G',seq.count('G')),('C',seq.count('C'))])
	return d

X = DNA_nucleotide(sequence)
X
#X_label = list(X)
#X_values = list(X.values())
length = len(sequence)
count_G = sequence.count("G")
count_C = sequence.count("C")

st.subheader('2. Print Text')
st.write('There are ' + str(X['A']) + ' adenine (A)')
st.write('There are ' + str(X['T']) + ' adenine (T)')
st.write('There are ' + str(X['G']) + ' adenine (G)')
st.write('There are ' + str(X['C']) + ' adenine (C)')

st.subheader('3. Displat Dataframe')
df = pd.DataFrame.from_dict(X, orient='index')
df = df.rename({0:'count'}, axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns = {'index':'nucleotide'})
st.write(df)

st.subheader('4 Display Bar Chart')
p = alt.Chart(df).mark_bar().encode(x='nucleotide',y='count')
p = p.properties(width = alt.Step(80))
st.write(p)

st.subheader('5 GC Content')
gc_content = ((count_G + count_C)/length)*100
st.write('The GC content of the query sequence is ', gc_content)

nuc_frequency = Counter(sequence)
plt.figure(figsize=(18,10))
plt.plot(nuc_frequency.keys(), nuc_frequency.values(), color='green', linewidth=2.0)
plt.xlabel("Nucleotide Bases", fontsize=20)
plt.ylabel("Frequency", fontsize=20)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.show()

