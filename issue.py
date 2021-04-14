import pandas as pd
import io

A = pd.read_csv(io.StringIO("""
A
Rheumatoid Arthritis
Breast Feeding, Exclusive
HIV/AIDS
Pre Hypertension
Hepatocellular Cancer
Gastrointestinal Cancer
Immunosuppression
Alzheimer Disease
Dementia
Hip Fractures
yash patil
"""), sep=r"\s{2,}", engine='python')

B = pd.read_csv(io.StringIO("""
B
Rheumatoid Arthritis
Breast Feeding Exclusive
AIDS/HIV
Pre-hypertension
Cancer, Hepatocellular
Leukemia, Myeloid
leukemia (Acute Myeloid)
leukemia (Acute Myeloid)
Breast Cancer,
Cancer of Breast
Rheumatoid Arthritis
Rheumatoid Arthritis
Injuries and Wounds
Wounds Injuries
Jaundice Neonatal
Jaundice Neonatal
Binge Eating Disorder
Binge Eating Disorder
Plasma Cell Neoplasms
Neoplasm, Plasma Cell
patil yash
"""), sep=r"\s{2,}", engine='python')


A["temp"] = A["A"].str.replace(r"\W+", " ", regex=True).str.lower().str.strip().str.split()


B["temp"] = B["B"].str.replace(r"\W+", " ", regex=True).str.lower().str.strip().str.split()
 


for x in A.index:
   for y in B.index:
     if(sorted(A["temp"][x])==sorted(B["temp"][y])): 
       B["B"][y] = B["B"][y].replace(B["B"][y],A["A"][x])
       B_matched = B.merge(A, how="inner", left_on="B", right_on="A")[["B"]]
     else:
       B_non = B[~B["B"].isin(B_matched["B"])].rename(columns={"B": "non"})



