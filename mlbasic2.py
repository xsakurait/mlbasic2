クラスタリング　最初にハイパーパラメータのクラス多数を決め、
重心をクラス多数と同等のカズ適当に置き、そこから重心の距離でクラスタ分けしていく。
終わったらクラスタの重心を再度決めもう１度クラスタ分けするそれを繰り返し
最終的にクラスタの要素が１つも変わらなくなった時に終了する

主成分分析　次元削減（変数の数を減らす）の１つの手法
次元削減で変数を減らしたときの新たな変数を　潜在変数（新たな変数）という

潜在変数は人間側で調整する＝ハイパーパラメータ
次元削減の使う用途としては、工場のセンサーなどがある
物体の気温や形などの変数がいっぱいあり区別するのが大変だから使う

次元削減のイメージは　多くのデータを表現（近似）できるようにすることが大事
第１主成分＝分散（データの散らばり）が最大になった軸をとること