import pandas as pd
dulieu = pd.read_csv(r'D:\Đồ án CSN Naivebayes\data.csv')
# Tính P(c1) và P(c2)
Pc1 = dulieu[dulieu['Cot5'] == 'Yes'].shape[0] / dulieu.shape[0]
Pc2 = dulieu[dulieu['Cot5'] == 'No'].shape[0] / dulieu.shape[0]
# Tính P(Age=Young|c1), P(Income=Meidum|c1), P(Student=Yes|c1), P(Credit_Rating=Fair|c1)
PAgeYoung_c1 = dulieu[(dulieu['Cot1'] == 'Young') & (dulieu['Cot5'] == 'Yes')].shape[0] / dulieu[dulieu['Cot5'] == 'Yes'].shape[0]
PIncomeMedium_c1 = dulieu[(dulieu['Cot2'] == 'Medium') & (dulieu['Cot5'] == 'Yes')].shape[0] / dulieu[dulieu['Cot5'] == 'Yes'].shape[0]
PStudentYes_c1 = dulieu[(dulieu['Cot3'] == 'Yes') & (dulieu['Cot5'] == 'Yes')].shape[0] / dulieu[dulieu['Cot5'] == 'Yes'].shape[0]
PCreditRatingFair_c1 = dulieu[(dulieu['Cot4'] == 'Fair') & (dulieu['Cot5'] == 'Yes')].shape[0] / dulieu[dulieu['Cot5'] == 'Yes'].shape[0]
# Tính P(Age=Young|c2), P(Income=Medium|c2), P(Student=Yes|c2), P(Credit_Rating=Fair|c2)
PAgeYoung_c2 = dulieu[(dulieu['Cot1'] == 'Young') & (dulieu['Cot5'] == 'No')].shape[0] / dulieu[dulieu['Cot5'] == 'No'].shape[0]
PIncomeMedium_c2 = dulieu[(dulieu['Cot2'] == 'Medium') & (dulieu['Cot5'] == 'No')].shape[0] / dulieu[dulieu['Cot5'] == 'No'].shape[0]
PStudentYes_c2 = dulieu[(dulieu['Cot3'] == 'Yes') & (dulieu['Cot5'] == 'No')].shape[0] / dulieu[dulieu['Cot5'] == 'No'].shape[0]
PCreditRatingFair_c2 = dulieu[(dulieu['Cot4'] == 'Fair') & (dulieu['Cot5'] == 'No')].shape[0] / dulieu[dulieu['Cot5'] == 'No'].shape[0]
#tính P(x|c1) 
Px_c1 = PAgeYoung_c1 * PIncomeMedium_c1 * PStudentYes_c1 * PCreditRatingFair_c1
#tính P(x|c2)
Px_c2 = PAgeYoung_c2 * PIncomeMedium_c2 * PStudentYes_c2 * PCreditRatingFair_c2
#tính P(c1)*P(x|c1) và P(c2)*P(x|c2)
Pc1_x =Pc1 * Px_c1
Pc2_x =Pc2 * Px_c2 
print(dulieu.to_string())
# In kết quả P yes no  của nhãn Buy Computer                    
print(f"P(c1) = {Pc1:.3f}")
print(f"P(c2) = {Pc2:.3f}")
# in kết quả của xác suất sự kiện khi biết nhãn c1 đã xảy ra
print(f"P(Age=Young|c1) = {PAgeYoung_c1:.3f}")
print(f"P(Income=Meidum|c1) = {PIncomeMedium_c1:.3f}")
print(f"P(Student=Yes|c1) = {PStudentYes_c1:.3f}")
print(f"P(Credit_Rating=Fair|c1) = {PCreditRatingFair_c1:.3f}")
# in kết quả của xác suất sự kiện khi biết nhãn c2 đã xảy ra
print(f"P(Age=Young|c2) = {PAgeYoung_c2:.3f}")
print(f"P(Income=Medium|c2) = {PIncomeMedium_c2:.3f}")
print(f"P(Student=Yes|c2) = {PStudentYes_c2:.3f}")
print(f"P(Credit_Rating=Fair|c2) = {PCreditRatingFair_c2:.3f}")
#in kết quả P(x/c1)
print(f"P(x|c1) = {Px_c1:.6f}")
#in kết quả P(x/c2)
print(f"P(x|c2) = {Px_c2:.6f}")
#in kết quả P(c1)*P(x|c1) và P(c2)*P(x|c2)
print(f"P(c1).P(x|c1) = {Pc1_x:.6f}")
print(f"P(c2).P(x|c2) = {Pc2_x:.6f}")
# Xác định phân lớp có thể nhất
nhan_co_the_xay_ra_nhat = 'c1' if Pc1_x > Pc2_x else 'c2'
print("Suy ra x sẽ mua máy tính" if nhan_co_the_xay_ra_nhat == 'c1' else "Suy ra x sẽ không mua máy tính")
