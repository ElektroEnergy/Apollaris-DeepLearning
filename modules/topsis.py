# Attribution and Credits to Anthonius Bimo
# https://medium.com/@anthonius.bimo/topsis-in-python-sharing-insights-on-effective-decision-making-a54e9c2bc28f

import numpy as np

class Topsis():
    def __init__(self, criteria_matrix, criteria_weight, criteria_preferences):
        # Inputs
        self.criteria_matrix = criteria_matrix
        self.criteria_weight = criteria_weight
        self.criteria_preferences = criteria_preferences  
        
        self.normalized_matrix = []
        self.weighted_matrix = []
        self.positive_separation = []
        self.negative_separation = []
        self.positive_ideal = []
        self.negative_ideal = []
        
        self.relative_similarity = []  

    # Normalization of the decision matrix aka. the decision matrix.
    def normalize_decision_matrix(self):
        criteria_rows = len(self.criteria_matrix)
        criteria_columns = len(self.criteria_matrix[0])
        column_sums= [0] * criteria_columns

        for j in range(criteria_columns):
            for i in range(criteria_rows):
                column_sums[j] += self.criteria_matrix[i][j] ** 2
        column_sums = [value ** 0.5 for value in column_sums]

        for i in range(criteria_rows):
            normalized_matrix_rows = []
            for j in range(criteria_columns):
                normalized_matrix_rows.append(self.criteria_matrix [i][j]/column_sums[j])
            self.normalized_matrix.append(normalized_matrix_rows)
    
        return self.normalized_matrix
    
    # Calculate the decision matrix with the respective weights for the criterias
    def calculate_weighted_matrix(self):
        normalized_rows = len(self.normalized_matrix)
        normalized_columns = len(self.normalized_matrix[0])
    
        for i in range(normalized_rows):
            weighted_matrix_rows = []
            for j in range(normalized_columns):
                weighted_matrix_rows.append(self.normalized_matrix [i][j]* self.criteria_weight[j])
            self.weighted_matrix.append(weighted_matrix_rows)
    
        return self.weighted_matrix
    
    def ideal_best_worst(self):
        weighted_column = len(self.weighted_matrix[0])

        for j in range(weighted_column):
            max_value = self.weighted_matrix[0][j]
            min_value = self.weighted_matrix[0][j]

            for i in range(len(self.weighted_matrix)):
                if self.weighted_matrix[i][j] > max_value:
                    max_value = self.weighted_matrix [i][j]
                if self.weighted_matrix[i][j] < min_value:
                    min_value = self.weighted_matrix [i][j]
            if self.criteria_preferences[j] == 1:  
                self.positive_ideal.append(max_value)
                self.negative_ideal.append(min_value)
            else:  
                self.positive_ideal.append(min_value)
                self.negative_ideal.append(max_value)

        return self.positive_ideal, self.negative_ideal
    
    def separation_from_ideal_point(self):
        weighted_rows = len(self.weighted_matrix)

        for i in range(weighted_rows):
            pos_sep = 0
            neg_sep = 0
            for j in range(len(self.positive_ideal)):
                pos_sep += (self.weighted_matrix[i][j] - self.positive_ideal[j]) ** 2
                neg_sep += (self.weighted_matrix[i][j] - self.negative_ideal[j]) ** 2
            self.positive_separation.append(pos_sep ** 0.5)
            self.negative_separation.append(neg_sep ** 0.5)
            
        return self.positive_separation,self.negative_separation
    
    def similarities_to_PIS(self):
        num_rows = len(self.positive_separation)

        for i in range(num_rows):
            pos_sep = self.positive_separation[i]
            neg_sep = self.negative_separation[i]
            similarity = neg_sep/(pos_sep + neg_sep)
            self.relative_similarity.append(similarity)
        
        print(self.relative_similarity)
        return self.relative_similarity
    
    
    def decision_making(self):
        self.normalize_decision_matrix()
        self.calculate_weighted_matrix()
        self.ideal_best_worst()
        self.separation_from_ideal_point()
        
        return np.argmax(self.similarities_to_PIS())