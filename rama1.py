from sklearn.metrics import accuracy_score, precision_score, f1_score, recall_score

#matriz de confusión
TP = 40 
TN = 30 
FP = 20 
FN = 10  


verdaderos = [1] * TP + [0] * FN + [1] * FP + [0] * TN  # Verdaderos (1 para positivos, 0 para negativos)
predicciones = [1] * TP + [1] * FP + [0] * FN + [0] * TN  # Predicciones (1 para positivos, 0 para negativos)


exactitud = accuracy_score(verdaderos, predicciones)
precision = precision_score(verdaderos, predicciones)
recall = recall_score(verdaderos, predicciones)  
f1 = f1_score(verdaderos, predicciones)


print(f'Exactitud: {exactitud:.2f}')
print(f'Precisión: {precision:.2f}')
print(f'Recall: {recall:.2f}')
print(f'F1-Measure: {f1:.2f}')
