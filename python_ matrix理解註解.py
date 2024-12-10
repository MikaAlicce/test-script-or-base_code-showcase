'''
備註者：Mika
備註日期：2023/05

嘗試理解網路上高手寫的程式碼
※ code不是我寫的 ※
「#」備註是我用來理解每段程式碼

code來源 : https://github.com/TheAlgorithms/Python
'''
from typing import Any
import numpy as np

    # numpy 支持維度數組與矩陣運算
def _is_matrix_spd(matrix : np.ndarray) -> bool :           # 參數matrix 輸入類型為 np.ndarray 屬性 bool；該方法為"判斷輸入的矩陣是否為正定矩陣"
    assert np.shape(matrix)[0] == np.shape(matrix)[1]       # shape 返回一個元組(a, b)，元組長度 = 維度。ex : ([1,2,3],[4,5,6]) ===> (2,3)
                                                            # assert 是判斷條件是否為真，若不為真拋出AssertionError；[0]代表行數(橫i)、[1]代表列數(縱j)，判斷行列(i, j)是否一樣

    if np.allclose(matrix, matrix.T) is False :             # allclose(a矩陣, b矩陣, 誤差值, equal_nan = Flase)
        return False                                        # allclose = 兩個矩陣誤差範圍內，回傳True；誤差預設值 : 1.0e-5(0.00001) <<<
                                                            # 如果matrix 與 matrix.T(轉置) 兩矩陣比較過後是"非對稱矩陣"，則回傳False(此判斷為正定矩陣條件之一)

    eigen_value, _ = np.linalg.eigh(matrix)                 # 取特徵值(eigen_value)不取得特徵向量
                                                            # numpy.linalg.eigh 是返回 Hermitian矩陣的特徵值和特徵向量

    return bool(np.all(eigen_value > 0))                    # 回傳布林值；當數組元素較多時，使用all()來比對矩陣所有特徵值是否都大於"0"(此判斷為正定矩陣條件之一)




def _create_spd_matrix(dimension : int) -> Any :            # 參數dimension 輸入類型為 int 屬性Any(任何)；隨機生成矩陣並呼叫_is_matrix_spd判斷是否為正定矩陣
    random_matrix = np.random.randn(dimension, dimension)   # 隨機生成矩陣，維度為dimension x dimension。
    spd_matrix = np.dot(random_matrix, random_matrix.T)     # np.dot()兩個矩陣相乘得點積(若是矩陣，同矩陣乘法)；且矩陣 * 轉置矩陣 會得到方形矩陣
                                                            # ( [1 2 3          [1 4          [(14 32
                                                            #    4 5 6]    x     2 5      =     32 77])
                                                            #                    3 6])
    assert _is_matrix_spd(spd_matrix)                       # 呼叫_is_matrix_spd判斷spd_matrix是否為正定矩陣
    return spd_matrix                                       # 若是正定矩陣，則回傳spd_matrix




def conjugate_gradient(                                     # 需要先理解「共軛梯度法」。
        spd_matrix : np.ndarray,                            # 參數spd_matrix 輸入類型 np.ndarray (矩陣)
        load_vector : np.ndarray,                           # 參數load_vector 輸入類型 np.ndarray (矩陣)
        max_iterations : int = 1000,                        # 參數max_iterations 輸入類型 int = 1000
        tol : float = 1e-8                                  # 參數tol 輸入類型 1e-8 ; 1e-8 = 0.00000001
) -> Any :                                                  # 屬性 Any

    assert np.shape(spd_matrix)[0] == np.shape(spd_matrix)[1]    # np.shape()返回一個元組(a, b)(維度); ex: ([1,2,3],[4,5,6]) >>> shape(2,3)
                                                                 # assert判斷 np.shape(spd_matrix)[0] 與 np.shape(spd_matrix)[1] 行列是否一樣
                                                                 # 結果Flase則拋出 AssertionError
                                                                 # ex : spd_matrix : (2,) == spd_matrix(,2) 行數列數相同

    assert np.shape(load_vector)[0] == np.shape(spd_matrix)[0]   # np.shape回傳一組元組(x, y)；assert判斷load_vector的行數與spd_matrix行數是否一致
                                                                 # ex : load_vector(2, ) == spd_matrix(2, )，[0]代表行數

    assert _is_matrix_spd(spd_matrix)                            # 呼叫_is_matrix_spd 判斷 spd_matrix是否為正定矩陣

    x0 = np.zeros((np.shape(load_vector)[0], 1))                 # np.shape返回 load_vector的行數後，使用 np.zeros 返回以0填充且固定列數為1的矩陣。
                                                                 # ex : load_vector返回數值為 3
                                                                 # [(0,
                                                                 #   0,
                                                                 #   0)]

    r0 = np.copy(load_vector)                                    # 複製 load_vector 矩陣
    p0 = np.copy(r0)                                             # 複製 r0 矩陣 (load_vector)

    error_residual = 1e9                                         # 1e9 = 1000000000
    error_x_solution = 1e9
    error = 1e9

    iterations = 0                                               # 紀錄迭代次數，檢查有沒有超過 max_iterations 的次數

    while error > tol :
        w = np.dot(spd_matrix, p0)                               # np.dot 計算spd_matrix 與 p0(複製的矩陣) 的點積(若是矩陣，同矩陣乘法)

        alpha = np.dot(r0.T, r0) / np.dot(p0.T, w)               # 計算出第一組(r0.T, r0)的點積以及第二組(p0.T, w)的點積(若是矩陣，同矩陣乘法)
                                                                 # 矩陣 * 轉置矩陣 會得到一個方形矩陣

        x = x0 + alpha * p0                                      # alpha * p0 (load_vector矩陣)
                                                                 # x0 (load_vector 為用0填充且列數為1的矩陣)

        r = r0 - alpha * w                                       # w  * alplga
                                                                 # r0 (load_vector矩陣)

        beta = np.dot(r.T, r) / np.dot(r0.T, r0)                 

        p = r + beta * p0

        error_residual = np.linalg.norm(r - r0)
        error_x_solution = np.linalg.norm(x - x0)
        error = np.maximum(error_residual, error_x_solution)

        x0 = np.copy(x)
        r0 = np.copy(r)
        p0 = np.copy(p)

        iterations += 1
        if iterations > max_iterations :
            break
    return x
