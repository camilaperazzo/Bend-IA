import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
from sklearn import tree
from sklearn.metrics import accuracy_score

from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
import seaborn as sns

# Carregar o arquivo CSV
column_names = [
    'Sample code number', 'Clump Thickness', 'Uniformity of Cell Size',
    'Uniformity of Cell Shape', 'Marginal Adhesion', 'Single Epithelial Cell Size',
    'Bare Nuclei', 'Bland Chromatin', 'Normal Nucleoli', 'Mitoses', 'Class'
]
df = pd.read_csv('breast-cancer-wisconsin.csv', names=column_names)

df.dtypes

with open('breast-cancer-wisconsin.names', 'r') as f:
    content = f.read()
print(content)

df.head(10)

# Tratar os valores ausentes
df.replace('?', pd.NA, inplace=True)  # Substituir '?' por NA
df['Bare Nuclei'] = pd.to_numeric(df['Bare Nuclei'], errors='coerce')  # Converter para numérico

# Calcular a média da coluna 'Bare Nuclei'
mean_bare_nuclei = df['Bare Nuclei'].mean()

# Preencher os valores ausentes com a média
df['Bare Nuclei'].fillna(int(mean_bare_nuclei), inplace=True)

# Converter as colunas para os tipos adequados
df = df.astype({
    'Sample code number': int,
    'Clump Thickness': int,
    'Uniformity of Cell Size': int,
    'Uniformity of Cell Shape': int,
    'Marginal Adhesion': int,
    'Single Epithelial Cell Size': int,
    'Bare Nuclei': int,
    'Bland Chromatin': int,
    'Normal Nucleoli': int,
    'Mitoses': int,
    'Class': int
})

# Separar os dados em atributos e rótulos
X = df.drop('Class', axis=1)
y = df['Class']

# Dividir os dados em conjuntos de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Contar a quantidade de casos benignos e malignos
counts = df['Class'].value_counts()

# Plotar o gráfico de barras
plt.bar(counts.index, counts.values)
plt.xlabel('Classe')
plt.ylabel('Quantidade')
plt.title('Quantidade de Casos Benignos e Malignos')
plt.xticks([2, 4], ['Benigno', 'Maligno'])
plt.show()

# Filtrar casos benignos e malignos
df_benign = df[df['Class'] == 2]
df_malignant = df[df['Class'] == 4]

# Calcular matriz de correlação para casos benignos
corr_benign = df_benign.corr()

# Calcular matriz de correlação para casos malignos
corr_malignant = df_malignant.corr()

# Plotar matriz de correlação para casos benignos
plt.figure(figsize=(10, 8))
sns.heatmap(corr_benign, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title('Matriz de Correlação - Casos Benignos')
plt.show()

# Plotar matriz de correlação para casos malignos
plt.figure(figsize=(10, 8))
sns.heatmap(corr_malignant, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title('Matriz de Correlação - Casos Malignos')
plt.show()

# Criar o classificador da árvore de decisão
classifier = DecisionTreeClassifier(random_state=42)
classifier.fit(X_train, y_train)

# Fazer a previsão no conjunto de teste
y_pred = classifier.predict(X_test)

# Criar a matriz de confusão
cm = confusion_matrix(y_test, y_pred)

# Plotar a matriz de confusão usando Seaborn
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.xlabel('Predicted')
plt.ylabel('True')
plt.title('Confusion Matrix')
plt.show()

# Calcular a acurácia das previsões
accuracy = accuracy_score(y_test, y_pred) * 100
print(f'Accuracy: {accuracy:.2f}%')

# Selecionar o ramo que deseja plotar
sub_tree = classifier.tree_.children_left[0], classifier.tree_.children_right[0]

# Plotar a árvore de decisão com o ramo selecionado
fig, ax = plt.subplots(figsize=(12, 12))
tree.plot_tree(classifier, ax=ax, max_depth=1, feature_names=X.columns, class_names=['benign', 'malignant'],
               node_ids=[0, sub_tree[0], sub_tree[1]])
plt.show()

# Escrever os scores da árvore de decisão
print('Scores da árvore de decisão:')
for feature, score in zip(X.columns, classifier.feature_importances_):
    print(f'{feature}: {score:.4f}')

# Função para realizar a previsão e calcular a precisão
def predict_sample(sample_code, thickness, size_uniformity, shape_uniformity, adhesion, epithelial_size,
                   bare_nuclei, chromatin, nucleoli, mitoses):
    sample = [sample_code, thickness, size_uniformity, shape_uniformity, adhesion, epithelial_size,
              bare_nuclei, chromatin, nucleoli, mitoses]
    predicted_class = classifier.predict([sample])[0]
    prediction_prob = classifier.predict_proba([sample])[0]
    prediction_prob_percent = max(prediction_prob) * 100

    if predicted_class == 2:
        result = 'benign'
    else:
        result = 'malignant'

    return result, prediction_prob_percent

# Exemplo de uso
sample_code = 101702
thickness = 1
size_uniformity = 1
shape_uniformity = 1
adhesion = 1
epithelial_size = 1
bare_nuclei = 1
chromatin = 1
nucleoli = 1
mitoses = 1

result, accuracy = predict_sample(sample_code, thickness, size_uniformity, shape_uniformity, adhesion,
                                 epithelial_size, bare_nuclei, chromatin, nucleoli, mitoses)

print(f'Result: {result}')
print(f'Accuracy: {accuracy:.2f}%')