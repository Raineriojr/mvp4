from model.avaliador import Avaliador
from model.carregador import Carregador
from models.model import Model
from model.preprocessador import PreProcessador

# Instanciação das Classes
carregador = Carregador()
modelo = Model()
avaliador = Avaliador()
processador = PreProcessador()

# Parâmetros
url_dados = "database/heart.csv"
# Carga dos dados
dataset = carregador.carregar_dados(url_dados)

# Separando em dados de entrada e saída

X_train, X_test, Y_train, Y_test = processador.pre_processar(dataset, 0.20, 7)

X = X_train.astype(int)
Y = Y_train.astype(int)
# Método para testar o modelo de Regressão Logística a partir do arquivo correspondente


def test_modelo_lr():
    # Importando o modelo de regressão logística
    lr_path = 'ml_model/modelo.pkl'
    modelo_lr = Model.load_model(lr_path)

    # Obtendo as métricas da Regressão Logística
    acuracia_lr, recall_lr, precisao_lr, f1_lr = avaliador.avaliar(
        modelo_lr, X, Y)

    # Testando as métricas da Regressão Logística
    # Modifique as métricas de acordo com seus requisitos
    assert acuracia_lr >= 0.75
    assert recall_lr >= 0.7
    assert precisao_lr >= 0.7
    assert f1_lr >= 0.7

# Método para testar modelo KNN a partir do arquivo correspondente


def test_modelo_knn():
    # Importando modelo de KNN
    knn_path = 'ml_model/modelo.pkl'
    modelo_knn = Model.load_model(knn_path)

    # Obtendo as métricas do KNN
    acuracia_knn, recall_knn, precisao_knn, f1_knn = avaliador.avaliar(
        modelo_knn, X, Y)

    # Testando as métricas do KNN
    # Modifique as métricas de acordo com seus requisitos
    assert acuracia_knn >= 0.75
    assert recall_knn >= 0.7
    assert precisao_knn >= 0.7
    assert f1_knn >= 0.7
