def mean_inference_time_func(estimator, X, y=None):
    t_predict = np.zeros(len(X))
    for m in range(len(t_predict)):
        start_time = time.time()
        pred = estimator.predict(X[m, :].reshape(1, -1))
        end_time = time.time()
        t_predict[m] = end_time - start_time

    #Devuelve la media del tiempo de inferencia como métrica principal
    return np.mean(t_predict)

def std_inference_time_func(estimator, X, y=None):
    t_predict = np.zeros(len(X))
    for m in range(len(t_predict)):
        start_time = time.time()
        pred = estimator.predict(X[m, :].reshape(1, -1))
        end_time = time.time()
        t_predict[m] = end_time - start_time
    std_inference_time = np.std(t_predict)
    return std_inference_time

def max_inference_time_func(estimator, X, y=None):
    t_predict = np.zeros(len(X))
    for m in range(len(t_predict)):
        start_time = time.time()
        pred = estimator.predict(X[m, :].reshape(1, -1))
        end_time = time.time()
        t_predict[m] = end_time - start_time
    inference_time = np.max(t_predict)
    return inference_time

def min_inference_time_func(estimator, X, y=None):
    t_predict = np.zeros(len(X))
    for m in range(len(t_predict)):
        start_time = time.time()
        pred = estimator.predict(X[m, :].reshape(1, -1))
        end_time = time.time()
        t_predict[m] = end_time - start_time
    inference_time = np.min(t_predict)
    return inference_time