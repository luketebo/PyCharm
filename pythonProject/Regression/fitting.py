from sklearn.preprocessing import PolynomialFeatures

featurizer_3 = PolynomialFeatures(degree=3)
# x = -3 -2 -1 0 1 2 3
x_3 = featurizer_3.fit_transform(-3)
# x_p = -2.5 -1.5 -0.5 0.5 1.5 2.5
x_p_3 = featurizer_3.transform(-2.5)
