def validityCheck(st):
    if 'flood' in st:
        return True
    if 'water' in st:
        return True
    if 'drown' in st:
        return True
    return False

def processIgnored(st):
    print("invalid input")

import process
st="the Half of my car's wheels have drowned."

st=st.lower()
proceed = validityCheck(st)
if proceed:
    st=process.process(st)
else:
    processIgnored(st)
#Work on this: The water has reached 3. 4.5 is the number
