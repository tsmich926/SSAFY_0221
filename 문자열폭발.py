ss = input()
key = input()
st = []
for i in range(len(ss)):
    if st:
        for j in range(len(key)):
            if ss[i] == key[j]:
                st.pop()
    else:
        st.append(ss[i])
