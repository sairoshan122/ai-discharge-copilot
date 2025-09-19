
import streamlit as st
from utils import load_patients, load_knowledge

st.set_page_config(page_title="AI Discharge Copilot", layout="wide")

patients = load_patients("data/patients.csv")
sop = load_knowledge("knowledge/sop_general.md")

st.title("🏥 AI Discharge Copilot")
st.write("### Patients")
st.dataframe(patients)

st.write("### Discharge SOP (General)")
st.markdown(sop)
