import pandas as pd

class Carregador:

    def carregar_dados(self, url: str):
        """ Carrega e retorna um DataFrame. Há diversos parâmetros 
        no read_csv que poderiam ser utilizados para dar opções 
        adicionais.
        """
        
        dataset = pd.read_csv(url, delimiter=',') # Esses dois parâmetros são próprios para uso deste dataset. Talvez você não precise utilizar
        
        dataset['Sex'] = dataset['Sex'].map({'F': 0, 'M': 1});
        dataset['ExerciseAngina'] = dataset['ExerciseAngina'].map({'N': 0, 'Y': 1});
        dataset = pd.get_dummies(dataset, columns=['ST_Slope'], prefix='ST_Slope');
        dataset = pd.get_dummies(dataset, columns=['ChestPainType'], prefix='ChestPain');
        dataset = pd.get_dummies(dataset, columns=['RestingECG'], prefix='Resting');
    
        return dataset