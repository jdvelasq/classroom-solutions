#
# Implementación de un regresor lineal que usa el metodo del
# gradiente descendente estocastico
# ==================================================================================
#
# En este ejercicio usted debe implmentar un regresor lineal basado en el metodo
# del gradiente descendente estocastico. La implementacion es similar,pero mas
# simple, a la existente en la libreria sklearn.
#
# El objetivo de este punto es que usted domine las tecnicas de optimizacion
# usadas en el gradiente descendente estocastico, las cuales son la fundamentacion
# para muchos otros algoritmos y metodologias
#
# Con el fin de que se familiarice con la libreria scikit-learn, se concervaron los
# textos explicativos en ingles de los parametros.
#
# Debe completar el codigo presentado hasta que se pasen todas las pruebas de
# implementacion. Tenga en cuenta que los detalles matemáticos de la metodología
# han sido discutidos previamente en clase a traves de multiples ejemplos. Este
# ejercicio unifica todos los conceptos presentados para el caso de regresion
#

import numpy as np
import random


class Regressor:
    """Linear model fitted by minimizing a regularized empirical loss with SGD.

    Parameters
    ----------
    loss : str, default='squared_loss'
        The loss function to be used. The possible values are 'squared_loss',
        'huber', 'epsilon_insensitive', or 'squared_epsilon_insensitive'

        The 'squared_loss' refers to the ordinary least squares fit.
        'huber' modifies 'squared_loss' to focus less on getting outliers
        correct by switching from squared to linear loss past a distance of
        epsilon. 'epsilon_insensitive' ignores errors less than epsilon and is
        linear past that; this is the loss function used in SVR.
        'squared_epsilon_insensitive' is the same but becomes squared loss past
        a tolerance of epsilon.

    penalty : {'l2', 'l1', 'elasticnet'}, default='l2'
        The penalty (aka regularization term) to be used. Defaults to 'l2'
        which is the standard regularizer for linear SVM models. 'l1' and
        'elasticnet' might bring sparsity to the model (feature selection)
        not achievable with 'l2'.

    alpha : float, default=0.0001
        Constant that multiplies the regularization term. The higher the
        value, the stronger the regularization.
        Also used to compute the learning rate when set to `learning_rate` is
        set to 'optimal'.

    l1_ratio : float, default=0.15
        The Elastic Net mixing parameter, with 0 <= l1_ratio <= 1.
        l1_ratio=0 corresponds to L2 penalty, l1_ratio=1 to L1.
        Only used if `penalty` is 'elasticnet'.

    fit_intercept : bool, default=True
        Whether the intercept should be estimated or not. If False, the
        data is assumed to be already centered.

    max_iter : int, default=1000
        The maximum number of passes over the training data (aka epochs).

    tol : float, default=1e-3
        The stopping criterion. If it is not None, training will stop
        when (loss > best_loss - tol) for ``n_iter_no_change`` consecutive
        epochs.

    shuffle : bool, default=True
        Whether or not the training data should be shuffled after each epoch.

    verbose : int, default=0
        The verbosity level.

    epsilon : float, default=0.1
        Epsilon in the epsilon-insensitive loss functions; only if `loss` is
        'huber', 'epsilon_insensitive', or 'squared_epsilon_insensitive'.

        For 'huber', determines the threshold at which it becomes less
        important to get the prediction exactly right.

        For epsilon-insensitive, any differences between the current prediction
        and the correct label are ignored if they are less than this threshold.

    random_state : int, RandomState instance, default=None
        Used for shuffling the data, when ``shuffle`` is set to ``True``.
        Pass an int for reproducible output across multiple function calls.

    learning_rate : string, default='invscaling'
        The learning rate schedule:

        - 'constant': `eta = eta0`
        - 'optimal': `eta = 1.0 / (alpha * (t + t0))`
          where t0 is chosen by a heuristic proposed by Leon Bottou.
        - 'invscaling': `eta = eta0 / pow(t, power_t)`
        - 'adaptive': eta = eta0, as long as the training keeps decreasing.
          Each time n_iter_no_change consecutive epochs fail to decrease the
          training loss by tol or fail to increase validation score by tol if
          early_stopping is True, the current learning rate is divided by 5.

    eta0 : double, default=0.01
        The initial learning rate for the 'constant', 'invscaling' or
        'adaptive' schedules. The default value is 0.01.

    power_t : double, default=0.25
        The exponent for inverse scaling learning rate.

    early_stopping : bool, default=False
        Whether to use early stopping to terminate training when validation
        score is not improving. If set to True, it will automatically set aside
        a fraction of training data as validation and terminate
        training when validation score returned by the `score` method is not
        improving by at least `tol` for `n_iter_no_change` consecutive
        epochs.

    validation_fraction : float, default=0.1
        The proportion of training data to set aside as validation set for
        early stopping. Must be between 0 and 1.
        Only used if `early_stopping` is True.

    n_iter_no_change : int, default=5
        Number of iterations with no improvement to wait before early stopping.

    warm_start : bool, default=False
        When set to True, reuse the solution of the previous call to fit as
        initialization, otherwise, just erase the previous solution.

    Attributes
    ----------
    coef_ : ndarray of shape (n_features,)
        Weights assigned to the features.

    intercept_ : ndarray of shape (1,)
        The intercept term.

    """

    def __init__(
        self,
        loss="squared_loss",
        penalty="l2",
        alpha=0.0001,
        l1_ratio=0.15,
        fit_intercept=True,
        max_iter=1000,
        tol=0.00001,
        shuffle=True,
        verbose=0,
        epsilon=0.1,
        random_state=None,
        learning_rate="invscaling",
        eta0=0.001,
        power_t=0.25,
        early_stopping=False,
        validation_fraction=0.1,
        n_iter_no_change=5,
        warm_start=False,
    ):
        self.loss = loss
        self.penalty = penalty
        self.alpha = alpha
        self.l1_ratio = l1_ratio
        self.fit_intercept = fit_intercept
        self.max_iter = max_iter
        self.tol = tol
        self.shuffle = shuffle
        self.verbose = verbose
        self.epsilon = epsilon
        self.random_state = random_state
        self.learning_rate = learning_rate
        self.eta0 = eta0
        self.power_t = power_t
        self.early_stopping = early_stopping
        self.validation_fraction = validation_fraction
        self.n_iter_no_change = n_iter_no_change
        self.warm_start = warm_start
        self.coef_ = None
        self.intercept_ = None

    def predict(self, X):
        X = np.array(X)
        X = np.matmul(X, np.array(self.coef_))
        X = X + np.array(self.intercept_)
        return np.asarray(X).reshape(-1)

    def initialize_weights(self, n_features):
        if self.warm_start is False or (self.coef_ is None or self.intercept_ is None):
            self.coef_ = np.zeros(n_features)
            self.intercept_ = 0.0

    def compute_loss(self, y_real, y_pred):

        if self.loss == "squared_loss":
            return 0.5 * (y_real - y_pred) * (y_real - y_pred)

        if self.loss == "huber":
            if np.abs(y_real - y_pred) <= self.epsilon:
                return 0.0
            return self.epsilon * np.abs(y_real - y_pred) - 0.5 * np.power(
                self.epsilon, 2
            )

        if self.loss == "epsilon_insensitive":
            return max(0.0, np.abs(y_real - y_pred) - self.epsilon)

        if self.loss == "squared_epsilon_insensitive":
            return max(0.0, np.power(np.abs(y_real - y_pred) - self.epsilon, 2))

    def compute_loss_gradient(self, x, y_real):

        y_pred = sum(self.coef_ * x) + self.intercept_
        e = y_real - y_pred

        if self.loss == "squared_loss":
            g_coef = -2 * e * x
            g_intercept = -2 * e if self.fit_intercept is True else 0.0

        if self.loss == "huber":
            if np.abs(e) <= self.epsilon:
                g_coef = -e * x
                g_intercept = -e if self.fit_intercept is True else 0.0
            else:
                g_coef = -self.epsilon * x
                g_intercept = -self.epsilon if self.fit_intercept is True else 0.0
                if e < 0.0:
                    g_coef = -g_coef
                    g_intercept = -g_intercept if self.fit_intercept is True else 0.0

        if self.loss == "epsilon_insensitive":
            if np.abs(e) <= self.epsilon:
                g_coef = 0.0
                g_intercept = 0.0
            else:
                if e > 0.0:
                    g_coef = -x
                    g_intercept = -1.0 if self.fit_intercept is True else 0.0
                else:
                    g_coef = x
                    g_intercept = 1.0 if self.fit_intercept is True else 0.0

        if self.loss == "squared_epsilon_insensitive":
            if np.abs(e) <= self.epsilon:
                g_coef = 0.0
                g_intercept = 0.0
            else:
                if e > 0.0:
                    g_coef = -2 * (y_real - y_pred - self.epsilon) * x
                    g_intercept = (
                        -2 * (y_real - y_pred - self.epsilon)
                        if self.fit_intercept is True
                        else 0.0
                    )
                else:
                    g_coef = +2 * (y_pred - y_real - self.epsilon) * x
                    g_intercept = (
                        +2 * (y_pred - y_real - self.epsilon)
                        if self.fit_intercept is True
                        else 0.0
                    )

        return g_coef, g_intercept

    def compute_penalty_gradient(self):

        if self.penalty == "l2":
            return self.coef_.copy()

        if self.penalty == "l1":
            return np.sign(self.coef_)

        if self.penalty == "elasticnet":
            rho = self.l1_ratio
            g_l2 = self.coef_.copy()
            g_l1 = np.sign(self.coef_)
            return rho * g_l2 + (1 - rho) * g_l1

    def compute_gradient(self, x, y_real):
        g_loss_coef, g_loss_intercept = self.compute_loss_gradient(x=x, y_real=y_real)
        g_penalty_coef = self.compute_penalty_gradient()
        return g_loss_coef + self.alpha * g_penalty_coef, g_loss_intercept

    def compute_eta(self, t):
        if self.learning_rate == "optimal":
            self.eta = 1.0 / (self.alpha * (self.optimal_init + t - 1))
        if self.learning_rate == "invscaling":
            self.eta = self.eta0 / np.power(t, self.power_t)

    def improve(self, x, y):
        """Implement delta rule"""
        g_coef, g_intercept = self.compute_gradient(x, y)
        self.coef_ = self.coef_ - self.eta * g_coef
        self.intercept_ = self.intercept_ - self.eta * g_intercept

    def compute_initial_eta(self):
        self.eta = self.eta0
        if self.learning_rate == "optimal":
            a = np.sqrt(1.0 / np.sqrt(self.alpha))
            initial_eta0 = a / max(1.0, self.compute_loss(-a, 1.0))
            self.optimal_init = 1.0 / (initial_eta0 * self.alpha)

    def fit(self, X, y):
        """Encuentra los parametros optimos del modelo para `X` y `y`."""

        if not isinstance(X, np.ndarray):
            X = np.matrix(X)

        if not isinstance(y, np.ndarray):
            y = np.array(y)

        n_samples, n_features = X.shape

        self.initialize_weights(n_features)

        self.compute_initial_eta()

        if self.random_state is not None:
            random.seed(self.random_state)

        samples_index = list(range(n_samples))
        t = 1.0
        best_loss = np.Infinity

        if self.early_stopping is True:
            validation_size = int(self.validation_fraction * n_samples)
            training_size = n_samples - validation_size
            is_validation_sample = [False] * training_size + [True] * validation_size
            random.shuffle(is_validation_sample)
        else:
            is_validation_sample = [False] * n_samples

        for epoch in range(self.max_iter):

            sumloss = 0.0

            if self.shuffle is True:
                random.shuffle(samples_index)

            for i_sample in range(n_samples):
                position = samples_index[i_sample]
                x = np.asarray(X[position]).reshape(-1)
                y_pred = sum(self.coef_ * x) + self.intercept_
                y_real = y[position]

                if self.early_stopping is True:
                    if is_validation_sample[position] is True:
                        sumloss += self.compute_loss(y_real=y_real, y_pred=y_pred)
                        continue
                else:
                    sumloss += self.compute_loss(y_real=y_real, y_pred=y_pred)
                self.compute_eta(t)
                self.improve(x=x, y=y_real)
                t += 1.0

            if sumloss > best_loss - self.tol * n_samples:
                no_improvement_count += 1
            else:
                no_improvement_count = 0

            if sumloss < best_loss:
                best_loss = sumloss

            if no_improvement_count >= self.n_iter_no_change:
                if self.learning_rate == "adaptive" and self.eta > 1e-6:
                    self.eta = self.eta / 5.0
                    no_improvement_count = 0
                else:
                    break
