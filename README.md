
# 🍎 FoodVision: Identificação de Frutas e Estimativa Calórica com Visão Computacional

Este projeto propõe uma solução tecnológica para automatizar o registro nutricional por meio da **visão computacional**. Utilizando a arquitetura **YOLOv8**, treinada com mais de 15 mil imagens, o sistema é capaz de **identificar frutas em fotos** e **estimar seu valor calórico médio**, oferecendo uma abordagem prática para o monitoramento alimentar.

---

## 🎯 Objetivo do Projeto

Registrar alimentos manualmente pode ser tedioso e impreciso. A proposta deste protótipo é facilitar esse processo ao:

- Detectar frutas em imagens com alta precisão
- Estimar as calorias por unidade de alimento
- Integrar saúde e tecnologia com uma interface simples e funcional

---

### 🔍 Detecção de Alimentos com YOLOv8

- Utiliza **Redes Neurais Convolucionais (CNNs)** para reconhecer objetos em imagens.
- Treinado com imagens anotadas via **LabelImg** no formato YOLO.
- Capaz de localizar múltiplas frutas em uma única imagem com bounding boxes.

### 🔢 Estimativa Calórica por Unidade

- Baseada em valores médios por fruta da **Tabela TACO** e **USDA**.
- Método prático e eficaz para frutas inteiras.
- Multiplica a quantidade detectada pelo valor calórico médio.

---


### 📸 Dataset

- Mais de **15.000 imagens** coletadas do **Roboflow** e **Kaggle**
- Frutas variadas em diferentes condições visuais
- Anotações feitas com **LabelImg** (`<classe> <x_centro> <y_centro> <largura> <altura>`)

### 🧪 Divisão de Dados

| Conjunto   | Percentual |
|------------|------------|
| Treinamento| 70%        |
| Validação  | 15%        |
| Teste      | 15%        |

---

## 🍓 Valores Nutricionais por Fruta

| Fruta    | Calorias | Proteína | Carboidratos | Gordura |
|----------|----------|----------|--------------|---------|
| Maçã     | 95 kcal  | 0,5 g    | 25 g         | 0,3 g   |
| Banana   | 105 kcal | 1,3 g    | 27 g         | 0,3 g   |
| Kiwi     | 42 kcal  | 0,8 g    | 10 g         | 0,4 g   |
| Limão    | 17 kcal  | 0,6 g    | 5,4 g        | 0,2 g   |
| Laranja  | 62 kcal  | 1,2 g    | 15 g         | 0,2 g   |
| Morango  | 4,8 kcal | 0,11 g   | 1,15 g       | 0,045 g |

> Para alimentos com massa variável (ex: arroz), recomenda-se estimativas por peso (100g).

---

## 🖥️ Interface do Sistema

- O usuário envia uma imagem
- O modelo detecta e identifica as frutas presentes
- O sistema exibe as **informações nutricionais** com base na contagem e nos valores calóricos por unidade

---

## 🔬 Abordagens Consideradas

| Abordagem                          | Pontos Fortes       | Limitações                        |
|-----------------------------------|----------------------|------------------------------------|
| CNNs com classificação direta     | Simples e rápidas    | Não detectam múltiplos objetos     |
| Sensores 3D para volume           | Alta precisão        | Exigem hardware adicional          |
| Estimativa por peso (gramas)      | Precisa em laboratório | Impraticável em imagens 2D      |
| Estimativa por unidade (usada)    | Prática e eficaz     | Menor precisão para frutas irregulares |

---

## 🧾 Resultados

- Precisão na detecção: **97% (mAP@0.5)** com YOLOv8
- Estimativa calórica por unidade revelou-se **eficiente e viável** para frutas
- Interface simples e funcional para uso direto

---

## 📌 Conclusão e Melhorias Futuras

Este protótipo confirma que é possível aplicar visão computacional no contexto nutricional com bons resultados. Para versões futuras, sugere-se:

- 🔢 Estimativa por volume usando objetos de escala
- 🧠 Segmentação instance-level com **Mask R-CNN** ou **SAM**
- 📡 Integração com **APIs de dados nutricionais**
- 📈 Histórico alimentar para monitoramento contínuo

---

## 🤝 Contribuições

Quer melhorar este projeto? Fique à vontade 

---

## 📬 Contato

Dúvidas, sugestões ou colaborações? Entre em contato com **[Seu Nome ou Equipe]**.

---
